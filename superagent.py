from cli import CommandLine

# https://rlhflow.github.io/posts/2024-03-23-bradley-terry-reward-model/
# https://arxiv.org/pdf/2406.12845

# Decides which LLM to use.
# https://docs.litellm.ai/docs/providers/
LLM_BACKEND = "gemini/gemini-1.5-flash"

# https://github.com/HumanSignal/RLHF/
cli = CommandLine(LLM_BACKEND)

while True:
    prompt, response = cli.prompt()
