export type Scenario =
  | "base"
  | "rain"
  | "truck_unavailable"
  | "budget_cut"
  | "emergency_dry"
  | "public_priority"

export interface Plan {
  scenario: Scenario
  resources: Record<string, number>
  planting_candidates: any[]
  care_priorities: any[]
  selection: {
    selected_actions: any[]
    budget_used_huf: number
    budget_limit_huf: number
    water_used_liters: number
    water_limit_liters: number
  }
  routes: any[]
  kpis: {
    new_trees_selected: number
    urgent_zones_total: number
    urgent_zones_covered: number
    urgent_coverage_pct: number
    water_used_liters: number
    distance_km: number
  }
}
