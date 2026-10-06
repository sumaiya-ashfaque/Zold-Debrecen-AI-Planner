import type { Scenario } from "../types/api"

const scenarios: [Scenario, string][] = [
  ["rain", "Rain forecast changed"],
  ["truck_unavailable", "One truck unavailable"],
  ["budget_cut", "Budget reduced by 25%"],
  ["emergency_dry", "Emergency dry tree group"],
  ["public_priority", "Prioritise schools & transport"],
]

export default function ScenarioPanel({
  onScenario,
  loading,
}: {
  onScenario: (scenario: Scenario) => void
  loading: boolean
}) {
  return (
    <div className="card">
      <h3>Scenario simulator</h3>
      <div className="scenario-grid">
        {scenarios.map(([value, label]) => (
          <button key={value} disabled={loading} onClick={() => onScenario(value)}>
            {label}
          </button>
        ))}
      </div>
    </div>
  )
}
