from apps import create_app

server = create_app()

if __name__ == "__main__":
    server.run(debug=True)   # in deployment, cannot use debug=True
