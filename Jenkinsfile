pipeline {
    agent any
       environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-diksha')
	}
       stages {
        stage('code') {
            steps {
               git 'https://github.com/sahu04/Assigment_Aaptatt.git'
            }
        }
        stage('build') {
            steps {
               sh 'mvn package'
            }
       }
		stage('build docker image') {
			steps {
				sh 'docker build -t  dikshasahu/javaapp:1 .'
			}
		}
        stage('Login') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

   }
  }

