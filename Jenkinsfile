pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                script {
                    // Install pyenv
                    sh 'curl https://pyenv.run | bash'

                    // Add pyenv to the PATH and source initialization script
                    sh 'export PYENV_ROOT="$HOME/.pyenv"'
                    sh 'export PATH="$PYENV_ROOT/bin:$PATH"'
                    sh 'eval "$(pyenv init --path)"'
                    sh 'eval "$(pyenv virtualenv-init -)"'

                    // Source the initialization script in the current shell
                    sh 'source ~/.bashrc || source ~/.bash_profile || true'

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
