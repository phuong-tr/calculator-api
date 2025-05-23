pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user -r requirements.txt || true'
            }
        }
        stage('Run Tests') {
            steps {
                sh '~/.local/bin/pytest tests > test_report.txt || true'
            }
        }
        stage('Code Quality') {
            steps {
                sh '~/.local/bin/pylint app > pylint_report.txt || true'
            }
        }
        stage('Security Scan') {
            steps {
                sh '~/.local/bin/bandit -r app > bandit_report.txt || true'
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
