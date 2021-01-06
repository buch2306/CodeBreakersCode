pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    stage('test') {
            steps {
                sh '''
                echo "This is the test stage"
                '''
            }
        }
        
    }
}
