# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Cognitive Rumination Worry Curfew Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCognitiveRuminationWorryCurfew

mcp = FastMCP("PersonalAgentCognitiveRuminationWorryCurfew")
client = PersonalAgentCognitiveRuminationWorryCurfew()

@mcp.tool()
def process_worry_inventory_and_curfew(
    intrusive_thoughts_json: str,
    current_time_24h: float = 22.5,
    bedtime_24h: float = 23.5,
    curfew_buffer_hours: float = 2.5
) -> str:
    """Processes worry thoughts, checks curfew breach, and calculates pre-sleep hyperarousal index."""
    import json
    thoughts = json.loads(intrusive_thoughts_json) if isinstance(intrusive_thoughts_json, str) else intrusive_thoughts_json
    return json.dumps(client.process_worry_inventory_and_curfew(
        thoughts, current_time_24h, bedtime_24h, curfew_buffer_hours
    ), indent=2)

@mcp.tool()
def simulate_arousal_decay_trajectory(
    starting_pschi: float = 68.0,
    intervention: str = "cognitive_defusion_and_curfew"
) -> str:
    """Simulates 60-minute pre-sleep cognitive arousal decay under active containment vs passive rumination."""
    import json
    return json.dumps(client.simulate_arousal_decay_trajectory(
        starting_pschi, intervention
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
