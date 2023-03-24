pipeline {
    agent any
    stages{
        stage('Project-2 Execution') {
           agent { docker {image 'python:latest'} }
           steps{
                sh "python3 project-2.py"               
           }
        }
    }
}
