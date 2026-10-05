## Installing and Dependencies
Set up a working environment
`python3 -m venv .venv`
Then use pip to install the dependencies
`pip install -e .`

Make a `.env` file with three variables:
    `LLM_PROVIDER`,
    `LLM_MODEL`,
    `LLM_API_KEY`. 
Theoretically instructor can run on all the big models, but this thing was only tested with openai. If using openai, reccomended starting configurations are: `LLM_PROVIDER = "openai"`, and `LLM_MODEL = "gpt-6-luna"`.

## Running and WorkFlow
The automateRisk component requires a human-in-the-loop at each stage to look through and verify the ML's output. You can add your own as long as you comport to the structure of the output (read the output / read `utils/schemas.py` to learn more), but its probably safest just to delete.

From project root run:

`python -m src.automateRisk.generateStakeholders`

This will generate a file called `generatedStakeholderList.json` in `src/modelOutputs`. Inspect the output.

Then, from root, run:
` ython -m src.automateRisk.analyzeStakeholders`

This will generate a file called `stakeholderRiskAnalysis.json` in `src/modelOutputs`. Inspect the output.
