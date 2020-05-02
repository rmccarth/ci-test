pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
		echo "Running build phase..."
                sh 'python test_hello.py'
            }
        }
    }
}
