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
                sh 'pip install -i https://pypi.doubanio.com/simple/ -r ./requirements.txt'
            }
        }
        stage('Style Check') {
            steps {
                echo 'Checking'
                sh 'python -m pylint taxi'
            }
        }
        stage('Test') {
            steps {
                echo 'testing'
                sh 'python -m pytest --cov-branch --cov=taxi tests/ --cov-report xml:coverage.xml'
            }
        }
        stage('Run') {
            steps {
                echo 'running'
                sh 'python main.py --test-data=./resource/testData.txt'
            }
        }
    }
}