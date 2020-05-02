pipeline {
    agent any
    stages {
        stage('build') {
            steps {
		            echo "Running build phase..."
                sh 'python test_hello.py'
            }
        }
    }
}
