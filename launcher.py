"""launcher.py. Launches the application.

This module is the application entry point. It is responsible for setting up the
web application and launching the cli afterwards.
"""

import time

import background

import cli
from api.server import run_server


@background.task
def launch_web_server():
    run_server()

    time.sleep(1)


def main():
    print("Launching web server...")
    launch_web_server()

    print("Visit http://localhost:5042/docs to view the interactive API Documentation.")
    print("Ctrl+C to exit.")
    print("--")
    print()

    time.sleep(0.5)

    print("Launching CLI...")
    cli.main()


if __name__ == "__main__":
    main()