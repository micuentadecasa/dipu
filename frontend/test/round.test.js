import assert from 'node:assert/strict'
import test from 'node:test'
import {
  COOLDOWN_MS,
  EXAM_SIZE,
  SHOWN_AT_STORAGE_KEY,
  makeRound,
  markQuestionsShown,
} from '../src/round.js'

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

test('never duplicates question IDs within a round', () => {
  const round = makeRound([{ id: 1 }, { id: 1 }, { id: 2 }], { random: withConstantRandom })

  assert.deepEqual(ids(round).sort(), [1, 2])
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
