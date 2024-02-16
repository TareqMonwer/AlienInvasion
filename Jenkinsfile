pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                script {
                    // Ensure Python3 is installed and check its version
                    sh 'python3 --version'

                    // Install pygame library using pip
                    sh 'pip3 install pygame'

                    // Print hello world using Python
                    sh 'python3 -c "print(\'Hello, World!\')"'
                }
            }
        }
    }
}
