pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile runner.py test_runner.py'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml test_runner.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
          agent any
          environment {
            VOLUME = '$(pwd):/src'
            IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
              dir(path: env.BUILD_ID) {
                sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F runner.py'"
              }
            }
            post {
              success {
                  archiveArtifacts "${env.BUILD_ID}/sources/dist/runner_executable"
                  sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
            }
          }
        }
    }
}
