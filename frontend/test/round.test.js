import assert from 'node:assert/strict'
import test from 'node:test'
import {
  COOLDOWN_MS,
  EXAM_SIZE,
  SHOWN_AT_STORAGE_KEY,
  makeRound,
  markQuestionsShown,
} from '../src/round.js'
import { QUESTIONS } from '../src/questions.js'

class MemoryStorage {
  #values = new Map()

  getItem(key) {
    return this.#values.get(key) ?? null
  }

  setItem(key, value) {
    this.#values.set(key, String(value))
  }

  removeItem(key) {
    this.#values.delete(key)
  }
}

const questions = (count) => Array.from({ length: count }, (_, index) => ({ id: index + 1 }))
const ids = (round) => round.map((question) => question.id)

const withConstantRandom = () => 0.5

function seededRandom(seed) {
  let state = seed
  return () => {
    state = (state * 1664525 + 1013904223) % 4294967296
    return state / 4294967296
  }
}

test('never duplicates question IDs within a round', () => {
  const round = makeRound([{ id: 1 }, { id: 1 }, { id: 2 }], { random: withConstantRandom })

  assert.deepEqual(ids(round).sort(), [1, 2])
})

test('never repeats a visible question prompt when records have different IDs', () => {
  const round = makeRound(
    [
      { id: 1, question: '¿Qué hace esta operación?' },
      { id: 2, question: '  ¿qué hace esta operación?  ' },
      { id: 3, question: '¿Qué devuelve esta operación?' },
    ],
    { random: withConstantRandom },
  )

  assert.deepEqual(ids(round).sort(), [1, 3])
})

test('excludes questions shown less than 14 hours ago', () => {
  const now = COOLDOWN_MS * 2
  const storage = new MemoryStorage()
  storage.setItem(SHOWN_AT_STORAGE_KEY, JSON.stringify({ 1: now - COOLDOWN_MS + 1 }))

  const round = makeRound(questions(3), { now, storage, random: withConstantRandom })

  assert.deepEqual(ids(round).sort(), [2, 3])
})

test('makes a question eligible at exactly 14 hours', () => {
  const now = COOLDOWN_MS * 2
  const storage = new MemoryStorage()
  storage.setItem(SHOWN_AT_STORAGE_KEY, JSON.stringify({ 1: now - COOLDOWN_MS }))

  const round = makeRound([{ id: 1 }], { now, storage })

  assert.deepEqual(ids(round), [1])
})

test('restores shown timestamps from session storage', () => {
  const now = COOLDOWN_MS * 2
  const storage = new MemoryStorage()
  const firstRound = makeRound(questions(2), { now, storage })
  markQuestionsShown(firstRound, { now, storage })

  const refreshedRound = makeRound(questions(2), { now, storage })

  assert.deepEqual(ids(refreshedRound), [])
})

test('returns only the eligible questions, including an empty pool', () => {
  const now = COOLDOWN_MS * 2
  const storage = new MemoryStorage()
  storage.setItem(
    SHOWN_AT_STORAGE_KEY,
    JSON.stringify({ 1: now - 1, 2: now - 1, 3: now - 1 }),
  )

  assert.deepEqual(ids(makeRound(questions(3), { now, storage })), [])

  storage.setItem(SHOWN_AT_STORAGE_KEY, JSON.stringify({ 1: now - 1 }))
  assert.deepEqual(ids(makeRound(questions(3), { now, storage })).sort(), [2, 3])
})

test('cleans expired and malformed timestamps while reading storage', () => {
  const now = COOLDOWN_MS * 2
  const storage = new MemoryStorage()
  storage.setItem(
    SHOWN_AT_STORAGE_KEY,
    JSON.stringify({ expired: now - COOLDOWN_MS, malformed: 'yesterday', active: now - 1 }),
  )

  makeRound([{ id: 'active' }, { id: 'expired' }, { id: 'malformed' }], { now, storage })

  assert.deepEqual(JSON.parse(storage.getItem(SHOWN_AT_STORAGE_KEY)), { active: now - 1 })
})

test('falls back safely when session storage contains malformed JSON', () => {
  const storage = new MemoryStorage()
  storage.setItem(SHOWN_AT_STORAGE_KEY, '{not-json')

  assert.deepEqual(ids(makeRound(questions(2), { storage })).sort(), [1, 2])
  assert.equal(storage.getItem(SHOWN_AT_STORAGE_KEY), null)
})

test('returns the normal 30-question round size', () => {
  const round = makeRound(questions(40), { random: withConstantRandom })

  assert.equal(round.length, EXAM_SIZE)
  assert.equal(new Set(ids(round)).size, EXAM_SIZE)
})

test('balances syllabus groups and limits Git questions in every full-bank round', () => {
  for (let seed = 1; seed <= 25; seed += 1) {
    const round = makeRound(QUESTIONS, { random: seededRandom(seed) })
    const topicCounts = new Map()
    for (const question of round) {
      topicCounts.set(question.topic_num, (topicCounts.get(question.topic_num) ?? 0) + 1)
    }

    assert.equal(round.length, EXAM_SIZE)
    assert.equal(new Set(ids(round)).size, EXAM_SIZE)
    const constitutionCount = (topicCounts.get(1) ?? 0) + (topicCounts.get(2) ?? 0)
    assert.equal(constitutionCount, 4, 'Constitution topics should receive four questions')
    for (let topic = 3; topic <= 12; topic += 1) {
      assert.equal(topicCounts.get(topic), 1, `topic ${topic} should be represented once`)
    }
    for (let topic = 36; topic <= 40; topic += 1) {
      assert.equal(topicCounts.get(topic), 1, `topic ${topic} should be represented once`)
    }

    const gitCount = round.filter((question) => question.topic_num >= 33 && question.topic_num <= 35).length
    const blazorCount = round.filter((question) => question.topic_num >= 26 && question.topic_num <= 32).length
    assert.ok(gitCount <= 1, `expected at most one Git question, got ${gitCount}`)
    assert.ok(blazorCount <= 2, `expected at most two Blazor questions, got ${blazorCount}`)
  }
})

test('keeps the Git cap when non-Git topic pools are unavailable', () => {
  const gitOnly = QUESTIONS.filter((question) => question.topic_num >= 33 && question.topic_num <= 35).slice(0, 30)
  const round = makeRound(gitOnly, { random: seededRandom(7) })

  assert.equal(round.length, 1)
  assert.ok(round.every((question) => question.topic_num >= 33 && question.topic_num <= 35))
})
