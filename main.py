import signal
import sys
import psutil

from runner import Runner

# mymodule.py


def signal_handler(sig, frame):
    current_process = psutil.Process()
    children = current_process.children(recursive=True)
    for child in children:
        child.terminate()
    sys.exit(0)


# Register the handler
signal.signal(signal.SIGINT, signal_handler)


def main():
    r = Runner()
    r.Execute()


if __name__ == "__main__":
    main()
