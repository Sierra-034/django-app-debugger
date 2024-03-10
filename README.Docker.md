### Run this application using Docker
- In order to debbug the application you need to build the image first if it doesn't exists
`docker build -t <IMAGE_TAG> .`
- Then create and run a new container with: `docker run --rm --name django-app-container -p 8000:8000 -p 3000:3000 --mount type=bind,source=./,target=/app <IMAGE_TAG>`
- If you are using vscode you should create a `.vscode/launch.json` with the following content:
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Django",
            "type": "debugpy",
            "request": "attach",
            "pathMappings": [
                {
                  "localRoot": "${workspaceFolder}", // Maps C:\Users\user1\project1
                  "remoteRoot": "." // To current working directory ~/project1
                }
              ],
            "connect": {
                "host": "127.0.0.1",
                "port": 3000
            }
        }
    ]
}
```

### Run this application using Docker compose
- Just execute the next command `docker compose up --build`
- Now you just have to launch vscode debugger

### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)