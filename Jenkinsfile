pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests > test_report.txt || true'
            }
        }
        stage('Code Quality') {
            steps {
                sh 'pylint app > pylint_report.txt || true'
            }
        }
        stage('Security Scan') {
            steps {
                sh 'bandit -r app > bandit_report.txt || true'
            }
        }
        stage('Run API') {
            steps {
                sh 'nohup python3 run.py &'
            }
        }
        stage('Health Check') {
            steps {
                sh 'curl --fail http://localhost:5000/calc || echo "Health check failed"'
            }
        }
    }
}
