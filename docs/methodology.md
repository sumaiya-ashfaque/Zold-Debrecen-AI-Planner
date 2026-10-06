# Prototype methodology

The prototype separates predictive and operational tasks.

## Planting score

Each candidate receives a normalized score:

```text
0.28 canopy deficit
0.25 heat exposure
0.20 public benefit
0.17 feasibility
0.10 green connectivity
```

The public-priority scenario increases the public-benefit weight.

## Care prioritization

The care score increases with:

- vegetation stress
- newly planted status
- time since watering

It decreases with:

- recent rainfall
- forecast rainfall

## Execution

The action-selection stage enforces budget and water constraints.

The resource stage assigns crews and vehicles.

The route stage minimizes avoidable travel with a deterministic nearest-neighbour heuristic. OR-Tools is included as a dependency for extension to richer vehicle-routing constraints.

## Replanning

Disruption scenarios change constraints and rerun the same pipeline rather than applying hard-coded presentation outputs.
