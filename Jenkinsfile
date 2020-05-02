pipeline {
    agent any
    stages {
        stage('build') {
            steps {
		            echo "Running build phase..."
                sh 'python3 test_hello.py'
            }
        }
    }
}
