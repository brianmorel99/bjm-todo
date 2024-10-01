pipeline {
    agent any
    
    environment { 
        repo = 'https://github.com/brianmorel99/bjm-todo.git'
        imagename = 'brianmorel99/bjm-todo:latest'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: "${repo}"]])
            }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("${imagename}")
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('', 'docker-login') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
