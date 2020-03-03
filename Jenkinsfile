pipeline {
    agent {
        docker {
            image 'python:3.6'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip install -r ./requirements.txt'
            }
        }
        stage('Style Check') {
            steps {
                echo 'Checking'
                sh 'pylint taxi'
            }
        }
    }
}