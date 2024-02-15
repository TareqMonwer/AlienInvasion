pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Testing Settings Values'
        sh '''sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
python3 --version'''
      }
    }

  }
}