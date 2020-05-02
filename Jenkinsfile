pipeline {
    agent any
    stages {
        stage('build') {
            steps {
		            echo "Running build phase..."
                sh '/usr/bin/python test_hello.py'
            }
        }
    }
}
