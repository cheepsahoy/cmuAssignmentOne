import asyncio

from ..utils.callLLM import callLLM
from ..utils.schemas import StakeholderList
from ..utils.writeAndLoad import saveStructuredOutput


async def generateStakeholders() -> None:
    """
    Generates stakeholders, 10-20 for the dashcam example
    """

    prompt = """
    Identify 10 stakeholders who could affect or be affected by the
    proposed dashcam missing-child detection system.

    Include both:
    --Direct stakeholders: people or organizations who directly interact
      with or use the system.
    --Indirect stakeholders: people or organizations affected by the system even if they don't use it.

    For each stakeholder:
    1. Give the stakeholder class a concise name.
    2. Classify it as direct or indirect.
    3. Give a one-sentence rationale explaining why the stakeholder is
       relevant and how they may be affected by the system.

    Focus on distinct stakeholder classes rather than individual people.
    Avoid redundant stakeholder categories.
    """

    print("Generating list . . .")
    reply = await callLLM(prompt, StakeholderList)
    print(f"Generated {len(reply.stakeholders)} stakeholders")
    saveStructuredOutput(reply, "generatedStakeholderList")
    print("Saved to src/modelOutputs/generatedStakeholderList.json")


if __name__ == "__main__":
    asyncio.run(generateStakeholders())
