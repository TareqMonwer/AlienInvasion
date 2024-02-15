pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                script {
                    // Install Python3
                    sh 'apt-get update && apt-get install -y python3'

                    // Ensure Python3 is installed and check its version
                    sh 'python3 --version'

                    // Install pygame library using pip
                    sh 'pip install pygame'

                    // Print hello world using Python
                    sh 'python3 -c "print(\'Hello, World!\')"'
                }
            }
        }
    }
}
