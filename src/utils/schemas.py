from typing import Literal

from pydantic import BaseModel, Field


## Generating Stakeholders
class Stakeholder(BaseModel):
    name: str = Field(description="Name or role of the stakeholder class")
    stakeholderType: Literal["direct", "indirect"] = Field(
        description="Whether the stakeholder directly uses the dashcam feature or is indirectly affected by it"
    )
    rationale: str = Field(
        description="One sentence explanation justifying why this stakeholder is relevent for the dashcam and how they are affected by it"
    )


class StakeholderList(BaseModel):
    stakeholders: list[Stakeholder] = Field(
        min_length=10,
        max_length=20,
        description="Between 10 and 20 relevant direct and indirect stakeholders. Don't repeat.",
    )


## Risking Stakeholders
class Requirement(BaseModel):
    description: str = Field(
        description="A desired condition in the environment that would prevent or reduce the associated stakeholder loss. Describe what must be true in the world, not a specific software behavior"
    )


class Loss(BaseModel):
    description: str = Field(
        description="A concrete harm that might happen to the stakeholder that violates their stated goal/value"
    )
    requirements: list[Requirement] = Field(
        description="Requirements that would prevent or reduce this loss."
    )


class Goal(BaseModel):
    description: str = Field(
        description="A goal or value that this specified stakeholder wants to pursue or preserve"
    )
    losses: list[Loss] = Field(
        description="Concrete ways that the system could violate this goal/value"
    )


class StakeholderRiskAnalysis(BaseModel):
    goals: list[Goal] = Field(
        description=(
            "Goals and values of the specified stakeholder. Across all goals, identify a total of 5 to 10 concrete losses, with requirements that prevent or reduce each loss."
        )
    )


## Analyzing Requirements
class Assumption(BaseModel):
    description: str = Field(
        description="A plausible assumption about the environment needed for the stated requirement to hold. The assumption should describe phenomena in the environment or how that phenomena become observable to the software."
    )


class Specification(BaseModel):
    description: str = Field(
        description="A specific task way that the software ensures the requirement takes place. The specificaiton must only describe the interface between the software and environment accounting for information the eceives, produces, stores,transmits, or exposes."
    )


class AssumptionSpecificationPair(BaseModel):
    assumption: Assumption
    specification: Specification


class RequirementAnalysis(BaseModel):
    analyses: list[AssumptionSpecificationPair] = Field(
        min_length=3,
        max_length=10,
        description="Between 3 and 10 assumption/specification pairs for the requirement. Each specification should rely on its associated environmental assumption.",
    )
