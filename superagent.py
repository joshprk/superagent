from litellm import completion

import sys
import time

# Decides which LLM to use.
# https://docs.litellm.ai/docs/providers/
LLM_BACKEND = "gemini/gemini-1.5-flash"

def print_info():
    print("SuperAgent\n" +
          "Automated Agent Recommendation\n")

def respond(prompt):
    payload = [{ "content": prompt, "role": "user" }]
    response = completion(model=LLM_BACKEND,
                          messages=payload,
                          stream=True)
    
    print('\033[?25l', end="")
    for part in response:
        chunk = part.choices[0].delta.content or ""
        for c in chunk:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.0025)
    print('\033[?25h')

def command(cmd):
    match cmd:
        case "exit":
            sys.exit()
        case _:
            print("Command not found\n")

def main():
    print_info()
    while True:
        prompt = input(">>> ")
        if not len(prompt) > 0:
            continue
        if prompt[0] == "/":
            command(prompt[1:])
            continue

        respond(prompt)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
