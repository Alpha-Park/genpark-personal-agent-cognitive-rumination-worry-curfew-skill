# Personal Agent Cognitive Rumination Worry Curfew Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Borkovec stimulus control worry containment scheduler, pre-sleep cognitive arousal indexer, and intrusive rumination decay modeler.

## Architecture

```mermaid
flowchart TD
    IntrusiveThoughts[Intrusive Thoughts & Severity 1-10] --> TriageEngine[Cognitive Triage & Curfew Engine]
    CurrentTime[Current Time & Target Bedtime] --> TriageEngine
    TriageEngine --> ActionableBranch[Actionable Tasks: Defer to Morning Triage Queue]
    TriageEngine --> HypotheticalBranch[Hypothetical Worries: Defusion & Quarantine]
    TriageEngine --> PSCHIModeler[Pre-Sleep Cognitive Hyperarousal Index: PSCHI]
    PSCHIModeler --> DecaySimulator[60-Min Parasympathetic Decay Simulator]
    DecaySimulator --> DeEscalation[Rapid Pre-Sleep Somatocognitive Recovery]
```

## Quickstart

```python
from client import PersonalAgentCognitiveRuminationWorryCurfew

agent = PersonalAgentCognitiveRuminationWorryCurfew()
res = agent.process_worry_inventory_and_curfew(
    intrusive_thoughts=[{"thought": "Quarterly taxes due", "severity_1_to_10": 8.0, "is_actionable": True}],
    current_time_24h=22.8, bedtime_24h=23.5
)
print(f"PSCHI: {res['pschi_hyperarousal_index']} | Curfew Active: {res['curfew_active']}")
```
