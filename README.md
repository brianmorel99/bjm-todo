# Brian Morel's Todo App Built with Flask

## To Build docker image.
* Build the image in the same directory as the Dockerfile (bjm-todo/)
* * ```docker build --tag bjm-todo .```

## Run the Docker image.
* Run the below command to run the docker image on the computer where it was built.  This also exposed the port from docker to the host.
* * ```docker run -d -p 5000:5000 bjm-todo```

## Upload Image to Docker Hub