import { useEffect, useState } from "react"
import Dashboard from "./pages/Dashboard"
import { generatePlan } from "./services/api"
import type { Plan, Scenario } from "./types/api"
import "./styles.css"

export default function App() {
  const [plan, setPlan] = useState<Plan | null>(null)
  const [mode, setMode] = useState("overview")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  async function load(scenario: Scenario = "base") {
    setLoading(true)
    setError("")
    try {
      setPlan(await generatePlan(scenario))
    } catch (e) {
      setError(e instanceof Error ? e.message : "Unable to load plan")
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    load()
  }, [])

  return (
    <div className="app-shell">
      <header>
        <div className="brand">
          <div className="brand-mark">🌳</div>
          <div>
            <strong>Zöld Debrecen AI Planner</strong>
            <small>Urban greening operations</small>
          </div>
        </div>
        <div className="header-meta">Debrecen, Hungary</div>
      </header>

      <main>
        {error && <div className="error">{error}</div>}
        <Dashboard
          plan={plan}
          mode={mode}
          onMode={setMode}
          onScenario={load}
          loading={loading}
        />
      </main>
    </div>
  )
}
