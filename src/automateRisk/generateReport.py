from ..utils.schemas import RequirementAnalysisReport
from ..utils.writeAndLoad import loadStructuredOutput, saveTextOutput


def generateReport() -> None:
    """
    Generates a human-readable Markdown report from the completed
    requirement analysis.
    """

    report = loadStructuredOutput(
        "requirementAnalysis",
        RequirementAnalysisReport,
    )

    lines: list[str] = []

    lines.append("# ML Risk Analysis Report")
    lines.append("")

    currentStakeholder = None
    currentGoal = None
    currentLoss = None

    for result in report.requirements:
        stakeholder = result.stakeholder
        goal = result.goal
        loss = result.loss
        requirement = result.requirement

        # New stakeholder
        if stakeholder.name != currentStakeholder:
            lines.append("---")
            lines.append("")
            lines.append(f"## Stakeholder: {stakeholder.name}")
            lines.append("")
            lines.append(f"**Type:** {stakeholder.stakeholderType}")
            lines.append("")
            lines.append(f"**Why they matter:** {stakeholder.rationale}")
            lines.append("")

            currentStakeholder = stakeholder.name
            currentGoal = None
            currentLoss = None

        # New goal/value
        if goal != currentGoal:
            lines.append(f"### Goal / Value")
            lines.append("")
            lines.append(goal)
            lines.append("")

            currentGoal = goal
            currentLoss = None

        # New loss
        if loss != currentLoss:
            lines.append("#### Potential Loss")
            lines.append("")
            lines.append(loss)
            lines.append("")

            currentLoss = loss

        # Requirement
        lines.append("##### Requirement")
        lines.append("")
        lines.append(requirement.description)
        lines.append("")

        # Assumption / specification pairs
        lines.append("**Engineering implications:**")
        lines.append("")

        for index, pair in enumerate(result.analysis.analyses, start=1):
            lines.append(f"**{index}. Assumption**")
            lines.append("")
            lines.append(pair.assumption.description)
            lines.append("")
            lines.append(f"**Specification**")
            lines.append("")
            lines.append(pair.specification.description)
            lines.append("")

    output = "\n".join(lines)

    filePath = saveTextOutput(
        output,
        "riskReport.md",
    )

    print(f"Report generated: {filePath}")


if __name__ == "__main__":
    generateReport()
