import asyncio

from ..utils.callLLM import callLLM
from ..utils.schemas import (
    StakeholderList,
    StakeholderRiskAnalysis,
    StakeholderRiskReport,
    StakeholderRiskResult,
)
from ..utils.writeAndLoad import loadStructuredOutput, saveStructuredOutput


async def analyzeStakeholders() -> None:
    """
    Loads the reviewed stakeholder list and generates goals, losses,
    and requirements for each stakeholder.
    """

    stakeholderList = loadStructuredOutput(
        "generatedStakeholderList",
        StakeholderList,
    )

    results: list[StakeholderRiskResult] = []

    for stakeholder in stakeholderList.stakeholders:
        print(f"Analyzing stakeholder: {stakeholder.name}")

        prompt = f"""
        Analyze the following stakeholder in relation to the dashcam
        missing-child detection system.

        STAKEHOLDER
        Name: {stakeholder.name}
        Type: {stakeholder.stakeholderType}
        Rationale: {stakeholder.rationale}

        Identify this stakeholder's important goals/values related
        to the system. Only generate 1-2 goals/values per stakeholder.

        Across ALL goals combined, identify a total of 5-10 concrete
        losses that could occur if the system violates those goals.
        Do not generate 5-10 losses for each individual goal.

        For every loss, identify one or more requirements that would
        prevent or reduce that loss.

        Requirements must describe desired conditions in the environment,
        not specific software behaviors.

        Organize each loss under the goal or value that it threatens.
        Avoid redundant goals, losses, or requirements.
        """

        analysis = await callLLM(
            prompt,
            StakeholderRiskAnalysis,
        )

        result = StakeholderRiskResult(
            stakeholder=stakeholder,
            analysis=analysis,
        )

        results.append(result)

    print("Generating StakeholderRiskReport")
    report = StakeholderRiskReport(
        stakeholders=results,
    )

    saveStructuredOutput(
        report,
        "stakeholderRiskAnalysis",
    )
    print("Saved to src/modelOutputs/stakeholderRiskAnalysis.json")


if __name__ == "__main__":
    asyncio.run(analyzeStakeholders())
