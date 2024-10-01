# Brian Morel's Todo App Built with Flask

## To Build docker image.
* Build the image in the same directory as the Dockerfile (bjm-todo/)
* * ```docker build --tag bjm-todo .```

## Run the Docker image.
* Run the below command to run the docker image on the computer where it was built.  This also exposed the port from docker to the host.
* * ```docker run -d -p 5000:5000 bjm-todo```

## Upload Image to Docker Hub
* The Jenkinsfile included in the repository is a sample pipline for using Jenkins to do the following:
* * Checkout the code from the source control repository
* * * The repository is the https link to a git repo, if on GitHub, it needs to be public.  It can be changed by editing the repo variable in the environment section at the top of the Jenkinsfile.
* * Build a Docker Image with the code
* * * The image name should be in the format "username/appname:tag" and can be changed by editing the imagename variable in the environment section at the top of the Jenkinsfile.
* * Upload the Docker Image to Docker Hub
* * * You will need to add your Docker login credentials to Jenkins and name them "docker-login"
* * * * https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials
