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
                sh 'python main.py --test-data=./resource/testData2.txt > temp'
                script {
                    String diff = sh(returnStdout: true, script: "diff temp resource/answer.txt")
                    if (diff != "") {
                        echo diff
                        error("The answer is incorrect!")
                    }
                }
            }
        }
    }
}