pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Testing Settings Values'
        sh '''apt-get update
apt-get install python3
apt-get install python3-pip
python3 --version'''
      }
    }

  }
}