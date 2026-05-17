import { useMemo, useState } from 'react'
import './App.css'
import { QUESTIONS } from './questions.js'

const EXAM_SIZE = 30
const LETTERS = ['A', 'B', 'C', 'D']

function shuffle(array) {
  const copy = [...array]
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[copy[i], copy[j]] = [copy[j], copy[i]]
  }
  return copy
}

function makeRound() {
  return shuffle(QUESTIONS).slice(0, Math.min(EXAM_SIZE, QUESTIONS.length))
}

function optionText(question, letter) {
  return question[`option_${letter.toLowerCase()}`]
}

function App() {
  const [roundId, setRoundId] = useState(1)
  const [questions, setQuestions] = useState(() => makeRound())
  const [answers, setAnswers] = useState({})
  const [showAnswers, setShowAnswers] = useState(false)

  const answeredCount = Object.keys(answers).length
  const correctCount = useMemo(
    () => questions.filter((q) => answers[q.id] === q.correct).length,
    [questions, answers],
  )
  const wrongCount = answeredCount - correctCount
  const progress = Math.round((answeredCount / questions.length) * 100) || 0

  function startNewRound() {
    setQuestions(makeRound())
    setAnswers({})
    setShowAnswers(false)
    setRoundId((id) => id + 1)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  function pick(question, letter) {
    if (answers[question.id]) return
    setAnswers((prev) => ({ ...prev, [question.id]: letter }))
  }

  return (
    <div className="app" key={roundId}>
      <header className="hero">
        <div className="hero-badge">Oposición · Diputación de Albacete</div>
        <h1>Test de estudio</h1>
        <p>
          Cada vez que entras o pulsas “Nueva ronda” se cargan {EXAM_SIZE} preguntas aleatorias.
          Responde y verás la corrección al instante.
        </p>
      </header>

      <section className="toolbar" aria-label="Resumen del test">
        <div className="progress-block">
          <strong>{answeredCount}/{questions.length}</strong>
          <span>respondidas</span>
          <div className="progress" aria-hidden="true"><div style={{ width: `${progress}%` }} /></div>
        </div>
        <div className="score-pills">
          <span className="pill ok">{correctCount} bien</span>
          <span className="pill bad">{wrongCount} mal</span>
          <span className="pill muted">{questions.length - answeredCount} pendientes</span>
        </div>
        <button className="btn secondary" onClick={startNewRound}>Nueva ronda</button>
      </section>

      <main className="question-list">
        {questions.map((question, index) => (
          <article className="question-card" key={question.id}>
            <div className="question-meta">
              <span>Pregunta {index + 1}</span>
              <span>Tema {question.topic_num}</span>
            </div>
            <h2>{question.question}</h2>

            <div className="options">
              {LETTERS.map((letter) => {
                const selected = answers[question.id] === letter
                const answered = Boolean(answers[question.id])
                const isCorrect = question.correct === letter
                let className = 'option'
                if (selected) className += ' selected'
                if ((answered || showAnswers) && isCorrect) className += ' correct'
                if (answered && selected && !isCorrect) className += ' wrong'

                return (
                  <button
                    type="button"
                    className={className}
                    key={letter}
                    onClick={() => pick(question, letter)}
                    disabled={answered}
                    aria-pressed={selected}
                  >
                    <span className="letter">{letter}</span>
                    <span>{optionText(question, letter)}</span>
                  </button>
                )
              })}
            </div>

            {(answers[question.id] || showAnswers) && question.explanation && (
              <div className="explanation">
                <strong>Respuesta correcta: {question.correct}.</strong> {question.explanation}
              </div>
            )}
          </article>
        ))}
      </main>

      <footer className="bottom-actions">
        <button className="btn reveal" onClick={() => setShowAnswers((value) => !value)}>
          {showAnswers ? 'Ocultar respuestas' : 'Mostrar respuestas correctas'}
        </button>
        <button className="btn primary" onClick={startNewRound}>Nueva ronda de 30</button>
      </footer>
    </div>
  )
}

export default App
