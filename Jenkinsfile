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
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run FastAPI') {
            steps {
                sh 'nohup python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &'
            }
        }
    }
}