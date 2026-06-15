pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code downloaded from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run FastAPI') {
            steps {
                bat 'start cmd /c uvicorn main:app --host 0.0.0.0 --port 8000'
            }
        }

    }
}