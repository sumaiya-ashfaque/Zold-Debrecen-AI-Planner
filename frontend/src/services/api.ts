import type { Plan, Scenario } from "../types/api"

const API = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000"

export async function generatePlan(scenario: Scenario = "base"): Promise<Plan> {
  const response = await fetch(`${API}/api/plan/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ scenario }),
  })
  if (!response.ok) throw new Error("Unable to generate plan")
  return response.json()
}

export async function dataQualityReport() {
  const response = await fetch(`${API}/api/data-quality/report`)
  if (!response.ok) throw new Error("Unable to fetch data quality report")
  return response.json()
}
