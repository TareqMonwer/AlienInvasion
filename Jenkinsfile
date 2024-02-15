pipeline {
    agent {
        docker {
            image 'python:3.8-alpine'
        }
    }

    stages {
        stage('Test') {
            steps {
                script {
                    // Ensure Python3 is installed and check its version
                    sh 'python --version'

                    // Install pygame library using pip
                    sh 'pip install pygame'

                    // Print hello world using Python
                    sh 'python -c "print(\'Hello, World!\')"'
                }
            }
        }
    }
}
