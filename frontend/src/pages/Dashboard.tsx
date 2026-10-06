import DebrecenMap from "../components/DebrecenMap"
import KpiGrid from "../components/KpiGrid"
import ScenarioPanel from "../components/ScenarioPanel"
import ActionTable from "../components/ActionTable"
import AgentFlow from "../components/AgentFlow"
import type { Plan, Scenario } from "../types/api"

export default function Dashboard({
  plan,
  mode,
  onMode,
  onScenario,
  loading,
}: {
  plan: Plan | null
  mode: string
  onMode: (mode: string) => void
  onScenario: (scenario: Scenario) => void
  loading: boolean
}) {
  return (
    <>
      <div className="hero">
        <div>
          <div className="eyebrow">DEIK.AI Challenge 2026 prototype</div>
          <h1>Zöld Debrecen AI Planner</h1>
          <p>Where to plant. What to protect. How to execute.</p>
        </div>
        <div className="status">{loading ? "Replanning…" : `Scenario: ${plan?.scenario || "base"}`}</div>
      </div>

      <div className="tabs">
        {["overview", "plant", "protect", "execute"].map((item) => (
          <button key={item} className={mode === item ? "active" : ""} onClick={() => onMode(item)}>
            {item[0].toUpperCase() + item.slice(1)}
          </button>
        ))}
      </div>

      <KpiGrid plan={plan} />

      <div className="main-grid">
        <div className="card map-card">
          <DebrecenMap plan={plan} mode={mode} />
        </div>
        <ScenarioPanel onScenario={onScenario} loading={loading} />
      </div>

      <ActionTable plan={plan} />
      <AgentFlow />

      <div className="disclaimer">
        Demo records are simulated. Map locations use real Debrecen geography but do not represent official municipal decisions.
      </div>
    </>
  )
}
