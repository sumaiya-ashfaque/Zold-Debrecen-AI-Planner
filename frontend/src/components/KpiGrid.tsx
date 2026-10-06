export default function KpiGrid({ plan }: { plan: any }) {
  const k = plan?.kpis || {}
  const cards = [
    ["New trees selected", k.new_trees_selected ?? 0],
    ["Urgent coverage", `${k.urgent_coverage_pct ?? 0}%`],
    ["Water allocated", `${(k.water_used_liters ?? 0).toLocaleString()} L`],
    ["Route distance", `${k.distance_km ?? 0} km`],
  ]
  return (
    <div className="kpi-grid">
      {cards.map(([label, value]) => (
        <div className="card kpi" key={label}>
          <div className="muted">{label}</div>
          <div className="kpi-value">{value}</div>
        </div>
      ))}
    </div>
  )
}
