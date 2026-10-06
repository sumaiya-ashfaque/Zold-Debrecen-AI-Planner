const agents = [
  "Data Quality",
  "Planting Opportunity",
  "Tree Care",
  "Action Selection",
  "Resource Allocation",
  "Routing & Scheduling",
  "Dispatch & Replanning",
]

export default function AgentFlow() {
  return (
    <div className="card">
      <h3>Multi-agent workflow</h3>
      <div className="agent-flow">
        {agents.map((agent, i) => (
          <div className="agent-step" key={agent}>
            <span>{i + 1}</span>
            <div>{agent}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
