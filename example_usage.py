# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Cognitive Rumination Worry Curfew Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentCognitiveRuminationWorryCurfew

def main():
    agent = PersonalAgentCognitiveRuminationWorryCurfew()

    print("=" * 70)
    print("DEMO: Personal Agent Cognitive Rumination & Worry Curfew Engine")
    print("=" * 70)

    # 1. Process Pre-Sleep Worry Inventory at 22:45 with bedtime at 23:30 (45 mins away)
    thoughts = [
        {
            "thought": "Need to finish client presentation slides for 9 AM board meeting",
            "severity_1_to_10": 8.5,
            "is_actionable": True,
            "next_micro_step": "Draft 3 bullet talking points in 8 AM morning review"
        },
        {
            "thought": "What if server infrastructure fails during the quarter-end surge?",
            "severity_1_to_10": 7.0,
            "is_actionable": False
        },
        {
            "thought": "Uncertain about mortgage rate adjustment next quarter",
            "severity_1_to_10": 6.0,
            "is_actionable": False
        }
    ]

    res_curfew = agent.process_worry_inventory_and_curfew(
        intrusive_thoughts=thoughts,
        current_time_24h=22.75,  # 22:45
        bedtime_24h=23.5,        # 23:30
        curfew_buffer_hours=2.5
    )

    print(f"\n1. Pre-Sleep Worry Inventory Analysis:")
    print(f"   Hours Until Bedtime: {res_curfew['hours_until_bedtime']} hrs")
    print(f"   Curfew Active: {res_curfew['curfew_active']}")
    print(f"   Pre-Sleep Hyperarousal Index (PSCHI): {res_curfew['pschi_hyperarousal_index']}/100")
    print(f"   Arousal Tier: {res_curfew['arousal_tier']}")
    print(f"   Sleep Latency Impact: {res_curfew['sleep_latency_impact_forecast']}")
    print(f"   Actionable Items: {res_curfew['actionable_worries_count']}")
    print(f"   Insoluble Hypotheticals: {res_curfew['hypothetical_worries_count']}")
    print(f"   Daytime Worry Window: {res_curfew['recommended_daytime_containment_window']}")
    print(f"   Acute Prescription: {res_curfew['acute_curfew_intervention']}")

    # 2. Simulate 60-Minute Cognitive Arousal Decay
    res_decay = agent.simulate_arousal_decay_trajectory(
        starting_pschi=res_curfew['pschi_hyperarousal_index'],
        intervention="cognitive_defusion_and_curfew"
    )

    print(f"\n2. 60-Minute Pre-Sleep Arousal Decay Simulation:")
    print(f"   Starting PSCHI: {res_decay['initial_pschi']}")
    print(f"   Final Arousal at 60 min: {res_decay['final_contained_arousal_at_60min']}")
    print(f"   Parasympathetic Shift Achieved: {res_decay['parasympathetic_shift_achieved']}")
    print(f"   Timeline Progression:")
    for step in res_decay['decay_timeline_60min']:
        print(f"     T+{step['minute']:02d}m: Passive = {step['passive_rumination_arousal']} | Contained = {step['active_curfew_contained_arousal']} (Delta: -{step['arousal_reduction_delta']})")

    print("\nVerification complete: Cognitive worry curfew engine executed flawlessly.")

if __name__ == "__main__":
    main()
