pipeline {
    agent any
       stages {
        stage('code') {
            steps {
               git 'https://github.com/sahu04/Assigment_Aaptatt.git'
            }
        }
        stages {
        stage('build') {
            steps {
               sh 'mvn package'
            }
       }
    }
  }
}


   



   

