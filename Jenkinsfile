pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                script {
                    // Install pyenv
                    sh 'curl https://pyenv.run | bash'

                    // Add pyenv to the PATH
                    sh 'export PATH="$HOME/.pyenv/bin:$PATH"'
                    sh 'eval "$(pyenv init --path)"'
                    sh 'eval "$(pyenv virtualenv-init -)"'

                    // Install Python 3.8.12
                    sh 'pyenv install 3.8.12'
                    sh 'pyenv global 3.8.12'

                    // Verify Python installation
                    sh 'python --version'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python3 --version'
                }
            }
        }
    }
}
