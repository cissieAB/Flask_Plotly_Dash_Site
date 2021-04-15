"""
The "main function" of the whole Python project.
"""

from apps import create_app

server = create_app()

if __name__ == "__main__":
    server.run()   # in deployment, cannot use debug=True
