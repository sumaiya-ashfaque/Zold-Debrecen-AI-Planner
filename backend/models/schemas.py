from typing import Literal
from pydantic import BaseModel, Field

class ResourceConfig(BaseModel):
    water_liters: int = Field(default=18000, ge=0)
    trucks: int = Field(default=2, ge=0)
    crews: int = Field(default=2, ge=0)
    planting_crew: int = Field(default=1, ge=0)
    workday_minutes: int = Field(default=480, ge=60)
    budget_huf: int = Field(default=8_000_000, ge=0)

class PlanRequest(BaseModel):
    resources: ResourceConfig = ResourceConfig()
    scenario: Literal["base", "rain", "truck_unavailable", "budget_cut", "emergency_dry", "public_priority"] = "base"

class ReplanRequest(BaseModel):
    current_plan_id: str | None = None
    scenario: Literal["rain", "truck_unavailable", "budget_cut", "emergency_dry", "public_priority"]

class DispatchRequest(BaseModel):
    task_id: str
    destination: str = "+36000000000"

class DispatchResponse(BaseModel):
    status: str
    message: str
