from cli import CommandLine
from sentence_transformers import SentenceTransformer
from agents import AGENTS

import torch
import time

# Decides which LLM to use.
# https://docs.litellm.ai/docs/providers/
LLM_BACKEND = "gemini/gemini-1.5-flash"

# https://github.com/HumanSignal/RLHF/
cli = CommandLine(LLM_BACKEND)
superagent = SentenceTransformer("all-MiniLM-L6-v2")

init_t = time.time()
agent_embeds = [
    superagent.encode(agent) for agent in AGENTS
]
print(time.time() - init_t)

while True:
    prompt = cli.prompt()
    embed = superagent.encode(prompt)
    
    best_agent = None
    best_score = -float("inf")

    for i in range(len(AGENTS)):
        similarity = superagent.similarity(embed, agent_embeds[i]).float()
        if similarity > best_score:
            best_agent = AGENTS[i]
            best_score = similarity
        print(AGENTS[i], ":", similarity)
    
    print("Best agent:", best_agent)
    response = cli.respond(prompt)
