import { useEffect, useMemo, useState } from 'react'
import './App.css'
import { QUESTIONS } from './questions.js'
import { EXAM_SIZE, makeRound, markQuestionsShown } from './round.js'

const LETTERS = ['A', 'B', 'C', 'D']

function optionText(question, letter) {
  return question[`option_${letter.toLowerCase()}`]
}

function App() {
  const [roundId, setRoundId] = useState(1)
  const [questions, setQuestions] = useState(() => makeRound(QUESTIONS))
  const [answers, setAnswers] = useState({})
  const [showAnswers, setShowAnswers] = useState(false)
  const [showSummary, setShowSummary] = useState(false)

  useEffect(() => {
    markQuestionsShown(questions)
  }, [questions])

  const answeredCount = Object.keys(answers).length
  const correctCount = useMemo(
    () => questions.filter((q) => answers[q.id] === q.correct).length,
    [questions, answers],
  )
  const wrongCount = answeredCount - correctCount
  const progress = Math.round((answeredCount / questions.length) * 100) || 0

  function startNewRound() {
    setQuestions(makeRound(QUESTIONS))
    setAnswers({})
    setShowAnswers(false)
    setShowSummary(false)
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
          Cada vez que entras o pulsas “Nueva ronda” se cargan hasta {EXAM_SIZE} preguntas aleatorias.
          Una pregunta no vuelve a salir hasta que pasan 14 horas. Responde y verás la corrección al instante.
        </p>
      </header>

      <section className={`toolbar ${showSummary ? 'toolbar-open' : ''}`} aria-label="Controles del test">
        {showSummary && (
          <div className="score-panel" id="test-summary">
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
          </div>
        )}
        <button
          className="btn secondary summary-toggle"
          onClick={() => setShowSummary((value) => !value)}
          aria-expanded={showSummary}
          aria-controls="test-summary"
        >
          {showSummary ? 'Ocultar progreso' : 'Ver progreso'}
        </button>
      </section>

      <main className="question-list">
        {questions.map((question, index) => (
          <article className="question-card" key={question.id}>
            <div className="question-meta">
              <span>Pregunta {index + 1}</span>
              <span
                className="question-topic"
                aria-label={`Tema ${question.topic_num}`}
              >
                Tema {question.topic_num}
              </span>
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
          {showAnswers ? 'Ocultar respuestas' : 'Ver respuestas'}
        </button>
        <button className="btn primary" onClick={startNewRound}>Nueva ronda</button>
      </footer>
    </div>
  )
}

export default App
