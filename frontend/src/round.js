export const EXAM_SIZE = 30
export const COOLDOWN_MS = 14 * 60 * 60 * 1000
export const SHOWN_AT_STORAGE_KEY = 'diputest:question-shown-at:v1'

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

export function makeRound(questions, { now = Date.now(), storage, random = Math.random } = {}) {
  const shownAt = readShownAt({ storage, now })
  const eligible = uniqueQuestions(questions).filter(
    (question) => shownAt[String(question.id)] == null,
  )

  return shuffle(eligible, random).slice(0, EXAM_SIZE)
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
