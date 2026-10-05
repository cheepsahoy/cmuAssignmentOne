import os

import instructor
from dotenv import load_dotenv
from pydantic import BaseModel

## load secrets
load_dotenv()
apiKey = os.getenv("LLM_API_KEY")
if not apiKey:
    raise ValueError("No LLM_API_KEY set in .env")
provider = os.getenv("LLM_PROVIDER")
if not provider:
    raise ValueError("No LLM_PROVIDER set in .env")
model = os.getenv("LLM_MODEL")
if not model:
    raise ValueError("no LLM_MODEL set in .env")

## load client
client = instructor.from_provider(
    f"{provider}/{model}", api_key=apiKey, async_client=True
)

## call context
CONTEXT = """
## Problem Description
We are developing a feature for dashcams that uses dashcam footage to locate children reported missing.

## System Considerations
--Dashcams don't have internet access, but can communicate over USB, Bluetooth or Wifi with phones, cars, and wifi-hotspots.
--Dashcams are powered by the car's battery power supply.
--Dashcam processing power varies model by model.
--Users may be cautious about privacy and network data costs.
--Computation may be possible on dashcam through edge computing.
"""


async def callLLM(prompt: str, responseModel: type[BaseModel]) -> BaseModel:
    """
    Calls the LLM in the specified way.
    Args:
        prompt: the prompt sent to the LLM.
        responseModel: structured pydantic model, see schemas.py in /utils/ for intended uses.
    Returns:
        Validated response of the selected responseModel.
    """
    response = await client.create(
        response_model=responseModel,
        reasoning_effort="none",
        messages=[
            {"role": "system", "content": CONTEXT},
            {"role": "user", "content": prompt},
        ],
    )
    return response
