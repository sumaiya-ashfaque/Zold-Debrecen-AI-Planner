# Architecture

## Data layer

The demo uses four input families:

- Green Sentinel-style environmental observations
- vegetation and tree-group attributes
- weather context
- real Debrecen coordinates for prototype sites

The data layer is intentionally replaceable so official feeds can be integrated later.

## Agents

### Data Quality Agent

Validates physical ranges, flags missing or invalid measurements, and interpolates small demo gaps.

### Planting Opportunity Agent

Ranks candidate planting sites using:

- canopy deficit
- heat exposure
- public benefit
- preliminary spatial feasibility
- green-network connectivity

### Tree Care Agent

Combines:

- stress score
- age/newly planted status
- days since watering
- recent rainfall
- forecast rainfall

It produces:

- water within 24 hours
- inspect and water
- inspect
- delay and recheck
- no action

### Action Selection Agent

Chooses actions under water and budget constraints.

### Resource Allocation Agent

Assigns selected actions to available crews and watering trucks.

### Routing & Scheduling Agent

Builds a deterministic nearest-neighbour route around the Debrecen demo points.

### Dispatch Agent

Generates low-friction crew instructions suitable for SMS or a municipal task interface.

### Replanning Agent

Modifies constraints for disruption scenarios and reruns the pipeline.

## Trust boundary

The prototype is decision support, not automatic municipal authorization.

Planting locations still require:

- site inspection
- utility checks
- accessibility checks
- planning approval
- arboricultural review
