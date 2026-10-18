export const EXAM_SIZE = 30
export const COOLDOWN_MS = 14 * 60 * 60 * 1000
export const SHOWN_AT_STORAGE_KEY = 'diputest:question-shown-at:v1'

const GIT_TOPIC_NUMS = new Set([33, 34, 35])
const BLAZOR_TOPIC_NUMS = new Set([26, 27, 28, 29, 30, 31, 32])
const MAX_BLAZOR_QUESTIONS = 2
const COMPOSITION_GROUPS = [
  { topicNums: [1, 2], count: 4 },
  { topicNums: [3, 4, 5, 6, 7, 8], count: 6 },
  { topicNums: [9, 10, 11, 12], count: 4 },
  { topicNums: [13, 14, 15, 16, 17], count: 4 },
  { topicNums: [18, 19, 20, 21, 22, 23, 24, 25], count: 4 },
  { topicNums: [26, 27, 28, 29, 30, 31, 32], count: 2 },
  { topicNums: [36, 37, 38, 39, 40], count: 5 },
]

function resolveStorage(storage) {
  if (storage !== undefined) return storage

  try {
    return globalThis.sessionStorage ?? null
  } catch {
    return null
  }
}

function saveShownAt(storage, shownAt) {
  if (!storage) return

  try {
    if (Object.keys(shownAt).length === 0) {
      storage.removeItem(SHOWN_AT_STORAGE_KEY)
    } else {
      storage.setItem(SHOWN_AT_STORAGE_KEY, JSON.stringify(shownAt))
    }
  } catch {
    // Storage can be unavailable or full. The app can still run without it.
  }
}

export function readShownAt({ storage, now = Date.now() } = {}) {
  const target = resolveStorage(storage)
  if (!target) return {}

  let raw
  try {
    raw = target.getItem(SHOWN_AT_STORAGE_KEY)
  } catch {
    return {}
  }

  if (!raw) return {}

  let parsed
  try {
    parsed = JSON.parse(raw)
  } catch {
    saveShownAt(target, {})
    return {}
  }

  if (!parsed || Array.isArray(parsed) || typeof parsed !== 'object') {
    saveShownAt(target, {})
    return {}
  }

  const shownAt = {}
  let changed = false
  for (const [id, timestamp] of Object.entries(parsed)) {
    if (typeof timestamp !== 'number' || !Number.isFinite(timestamp) || timestamp < 0) {
      changed = true
      continue
    }

    if (now - timestamp >= COOLDOWN_MS) {
      changed = true
      continue
    }

    shownAt[id] = timestamp
  }

  if (changed) saveShownAt(target, shownAt)
  return shownAt
}

export function shuffle(array, random = Math.random) {
  const copy = [...array]
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(random() * (i + 1))
    ;[copy[i], copy[j]] = [copy[j], copy[i]]
  }
  return copy
}

function uniqueQuestions(questions) {
  const seenIds = new Set()
  const seenPrompts = new Set()
  return questions.filter((question) => {
    if (!question || question.id == null || seenIds.has(question.id)) return false

    const prompt = typeof question.question === 'string'
      ? question.question.normalize('NFKC').toLocaleLowerCase('es').replace(/\s+/g, ' ').trim()
      : null
    if (prompt !== null && seenPrompts.has(prompt)) return false

    seenIds.add(question.id)
    if (prompt !== null) seenPrompts.add(prompt)
    return true
  })
}

function isSyllabusQuestion(question) {
  return Number.isInteger(question.topic_num) && question.topic_num >= 1 && question.topic_num <= 40
}

function isGitQuestion(question) {
  return GIT_TOPIC_NUMS.has(question.topic_num)
}

function isBlazorQuestion(question) {
  return BLAZOR_TOPIC_NUMS.has(question.topic_num)
}

function appendUniqueQuestions(target, additions, selectedIds) {
  for (const question of additions) {
    if (selectedIds.has(question.id)) continue
    target.push(question)
    selectedIds.add(question.id)
  }
}

function takeFromTopicGroup(topicBuckets, topicNums, count, random, selectedIds) {
  const availableTopics = topicNums.filter((topicNum) =>
    (topicBuckets.get(topicNum) ?? []).some((question) => !selectedIds.has(question.id)),
  )
  const pickedTopics = shuffle(availableTopics, random).slice(0, count)
  const picks = pickedTopics.map((topicNum) => {
    const candidates = (topicBuckets.get(topicNum) ?? []).filter(
      (question) => !selectedIds.has(question.id),
    )
    return shuffle(candidates, random)[0]
  }).filter(Boolean)

  if (picks.length < count) {
    const pickedIds = new Set(picks.map((question) => question.id))
    const remaining = topicNums
      .flatMap((topicNum) => topicBuckets.get(topicNum) ?? [])
      .filter((question) => !selectedIds.has(question.id) && !pickedIds.has(question.id))
    appendUniqueQuestions(picks, shuffle(remaining, random).slice(0, count - picks.length), pickedIds)
  }
  return picks
}

function selectBalancedQuestions(eligible, random) {
  if (!eligible.some(isSyllabusQuestion)) return shuffle(eligible, random).slice(0, EXAM_SIZE)

  const topicBuckets = new Map()
  for (const question of eligible) {
    if (!isSyllabusQuestion(question)) continue
    const bucket = topicBuckets.get(question.topic_num) ?? []
    bucket.push(question)
    topicBuckets.set(question.topic_num, bucket)
  }

  const selected = []
  const selectedIds = new Set()
  for (const group of COMPOSITION_GROUPS) {
    appendUniqueQuestions(
      selected,
      takeFromTopicGroup(topicBuckets, group.topicNums, group.count, random, selectedIds),
      selectedIds,
    )
  }

  const gitQuestions = shuffle(
    eligible.filter((question) => isGitQuestion(question) && !selectedIds.has(question.id)),
    random,
  )
  appendUniqueQuestions(selected, gitQuestions.slice(0, 1), selectedIds)

  const remaining = eligible.filter(
    (question) => !selectedIds.has(question.id) && !isGitQuestion(question),
  )
  const nonBlazor = remaining.filter((question) => !isBlazorQuestion(question))
  if (selected.length < EXAM_SIZE) {
    appendUniqueQuestions(
      selected,
      shuffle(nonBlazor, random).slice(0, EXAM_SIZE - selected.length),
      selectedIds,
    )
  }

  if (selected.length < EXAM_SIZE) {
    const blazor = remaining.filter(
      (question) => isBlazorQuestion(question) && !selectedIds.has(question.id),
    )
    const blazorSlots = Math.min(
      EXAM_SIZE - selected.length,
      Math.max(0, MAX_BLAZOR_QUESTIONS - selected.filter(isBlazorQuestion).length),
    )
    appendUniqueQuestions(selected, shuffle(blazor, random).slice(0, blazorSlots), selectedIds)
  }

  return shuffle(selected, random).slice(0, EXAM_SIZE)
}

export function makeRound(questions, { now = Date.now(), storage, random = Math.random } = {}) {
  const shownAt = readShownAt({ storage, now })
  const eligible = uniqueQuestions(questions).filter(
    (question) => shownAt[String(question.id)] == null,
  )

  return selectBalancedQuestions(eligible, random)
}

export function markQuestionsShown(questions, { now = Date.now(), storage } = {}) {
  const target = resolveStorage(storage)
  if (!target || questions.length === 0) return

  const shownAt = readShownAt({ storage: target, now })
  for (const question of uniqueQuestions(questions)) {
    shownAt[String(question.id)] = now
  }
  saveShownAt(target, shownAt)
}
