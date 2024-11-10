"""
This file contains CLI helper functions unrelated
to the algorithm. It may be safely ignored.
"""
from litellm import completion

import sys
import time

class CommandLine:
    def __init__(self, backend):
        self.backend = backend

    def respond(self, stdin):
        context = [{ "content": stdin, "role": "user" }]
        response = completion(model=self.backend,
                              messages=context,
                              stream=True)
        collect = ""

        print("\033[?25l", end="")
        for part in response:
            chunk = part.choices[0].delta.content or ""
            collect += chunk
            for c in chunk:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.0025)
        print("\033[?25h")
        return collect

    def prompt(self):
        stdin = input(">>> ")
        if not len(stdin) > 0:
            return None, None
        elif stdin[0] == "/":
            return None, None
        
        response = self.respond(stdin)
        
        return stdin, response
