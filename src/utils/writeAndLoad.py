from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel

##establish generic input
T = TypeVar("T", bound=BaseModel)


OUTPUT_DIR = Path(__file__).resolve().parent.parent / "modelOutputs"


## Saving data
def saveStructuredOutput(output: BaseModel, filename: str) -> Path:
    """
    Saves a Pydantic model as JSON in src/modelOutputs.

    Args:
        output: Structured LLM output represented as a Pydantic BaseModel.
        filename: Name of the output file.

    Returns:
        Path to the saved file.
    """

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not filename.endswith(".json"):
        filename += ".json"

    filePath = OUTPUT_DIR / filename

    filePath.write_text(
        output.model_dump_json(indent=2),
        encoding="utf-8",
    )

    return filePath


def saveTextOutput(content: str, filename: str) -> Path:
    """
    Saves plain text or Markdown output in src/modelOutputs.
    """

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    filePath = OUTPUT_DIR / filename

    filePath.write_text(
        content,
        encoding="utf-8",
    )

    return filePath


## Absorbing data


def loadStructuredOutput(filename: str, modelType: type[T]) -> T:
    """
    Loads JSON from src/modelOutputs and validates it against
    the provided Pydantic model.

    Args:
        filename: Name of the saved JSON file.
        modelType: Pydantic model class the data should conform to.

    Returns:
        An instance of modelType.
    """

    if not filename.endswith(".json"):
        filename += ".json"

    filePath = OUTPUT_DIR / filename

    if not filePath.exists():
        raise FileNotFoundError(f"No model output found at {filePath}")

    return modelType.model_validate_json(filePath.read_text(encoding="utf-8"))
