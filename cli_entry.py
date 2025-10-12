import sys
import os

# Immediate feedback - this should print almost instantly
print("Scribe CLI starting...", flush=True)

# Only import after initial feedback
from scribe.cli import run

if __name__ == "__main__":
    run()
