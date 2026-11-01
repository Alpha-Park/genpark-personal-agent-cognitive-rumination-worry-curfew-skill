---
name: genpark-personal-agent-cognitive-rumination-worry-curfew-skill
version: "1.0.0"
description: "Zero-dependency Borkovec stimulus control worry containment scheduler, pre-sleep cognitive arousal indexer, and intrusive rumination decay modeler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Cognitive Rumination Worry Curfew Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI companions to eliminate bedtime cognitive churn, enforce Borkovec's stimulus control worry containment, calculate the Pre-Sleep Cognitive Hyperarousal Index (PSCHI), and simulate parasympathetic recovery.

## Agent In-Context Capabilities

- **Stimulus Control Worry Curfew**: Enforces an explicit 2.5-hour cognitive curfew prior to target bedtime, parking problem-solving into a dedicated daytime worry window.
- **Cognitive Defusion & Triage**: Separates actionable tasks (scheduled for the following morning) from insoluble existential hypotheticals (quarantined).
- **Hyperarousal Quantification**: Computes PSCHI (0-100) and predicts sleep latency impact.

## Tools Summary

1. `process_worry_inventory_and_curfew`: Ingests intrusive thoughts, flags curfew violations, and calculates PSCHI.
2. `simulate_arousal_decay_trajectory`: Compares 60-minute exponential decay of cognitive arousal under active containment vs. uncontained passive rumination.
