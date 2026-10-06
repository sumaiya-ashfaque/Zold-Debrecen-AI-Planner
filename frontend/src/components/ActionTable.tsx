export default function ActionTable({ plan }: { plan: any }) {
  const tasks = (plan?.routes || []).flatMap((route: any) =>
    route.schedule.map((task: any) => ({ ...task, resource: route.resource_id }))
  )

  return (
    <div className="card">
      <h3>Operational plan</h3>
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Time</th><th>Task</th><th>Area</th><th>Resource</th><th>Water</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map((t: any) => (
              <tr key={`${t.resource}-${t.task_id}`}>
                <td>{t.scheduled_time}</td>
                <td>{t.label}</td>
                <td>{t.area}</td>
                <td>{t.resource}</td>
                <td>{t.water_liters ? `${t.water_liters.toLocaleString()} L` : "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
