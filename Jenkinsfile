pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code downloaded from GitHub'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run FastAPI') {
            steps {
                sh '''
                . venv/bin/activate
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &
                '''
            }
        }
    }
}