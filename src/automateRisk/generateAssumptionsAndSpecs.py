import asyncio

from ..utils.callLLM import callLLM
from ..utils.schemas import (
    RequirementAnalysis,
    RequirementAnalysisReport,
    RequirementAnalysisResult,
    StakeholderRiskReport,
)
from ..utils.writeAndLoad import (
    loadStructuredOutput,
    saveStructuredOutput,
)


async def generateAssumptionsAndSpecs() -> None:
    """
    Generates assumptions and specifications for every requirement
    """

    riskReport = loadStructuredOutput(
        "stakeholderRiskAnalysis",
        StakeholderRiskReport,
    )

    results: list[RequirementAnalysisResult] = []

    # Count requirements first so we can show progress
    totalRequirements = sum(
        len(loss.requirements)
        for stakeholderResult in riskReport.stakeholders
        for goal in stakeholderResult.analysis.goals
        for loss in goal.losses
    )

    currentRequirement = 0

    for stakeholderResult in riskReport.stakeholders:
        stakeholder = stakeholderResult.stakeholder

        for goal in stakeholderResult.analysis.goals:
            for loss in goal.losses:
                for requirement in loss.requirements:
                    currentRequirement += 1

                    print(
                        f"Analyzing requirement "
                        f"{currentRequirement}/{totalRequirements}: "
                        f"{requirement.description}"
                    )

                    prompt = f"""
                    Analyze the following requirement for the dashcam
                    missing-child detection system.

                    STAKEHOLDER:
                    {stakeholder.name}

                    STAKEHOLDER TYPE:
                    {stakeholder.stakeholderType}

                    STAKEHOLDER GOAL/VALUE:
                    {goal.description}

                    LOSS:
                    {loss.description}

                    REQUIREMENT:
                    {requirement.description}

                    Generate between 3 and 5 assumption/specification pairs.

                    For each pair:

                    ASSUMPTION:
                    Identify a plausible assumption about the environment that
                    must hold for this requirement to be established.

                    SPECIFICATION:
                    Identify a software responsibility that draws on the
                    associated assumption to establish the requirement.

                    Specifications must describe only the interface between
                    the software and its environment, including information
                    the software receives, produces, stores, transmits, or exposes.

                    Do not describe internal implementation details.

                    Each specification should clearly rely on its paired assumption.
                    Avoid redundant assumption/specification pairs.
                    """

                    analysis = await callLLM(
                        prompt,
                        RequirementAnalysis,
                    )

                    result = RequirementAnalysisResult(
                        stakeholder=stakeholder,
                        goal=goal.description,
                        loss=loss.description,
                        requirement=requirement,
                        analysis=analysis,
                    )

                    results.append(result)

    report = RequirementAnalysisReport(
        requirements=results,
    )
    print(f"Finished analyzing {len(results)} requirements.")

    saveStructuredOutput(
        report,
        "requirementAnalysis",
    )

    print("Saved to src/modelOutputs/requirementAnalysis.json")


if __name__ == "__main__":
    asyncio.run(generateAssumptionsAndSpecs())
