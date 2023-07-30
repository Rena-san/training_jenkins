pipeline {
    agent any
    stages {
        stage('Checkout project') {
            steps {
                script {
                    git branch: "main",
                        credentialsId: 'DESKTOP-0IPILK4$',
                        url: 'https://github.com/Rena-san/training_jenkins'
                }
            }
        }

        stage('Setup') {
            steps {
                sh "python -m venv venv"
                sh "source venv/Scripts/activate"
                sh "pip install -r requirements.txt"
            }
        }
        }

    }

