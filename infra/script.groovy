node('master') {
    stage("Limpeza de Cache e Clonando Repositório") {
        cleanWs()
        checkout scm

    }

    stage("Verificação da qualidade do código via Sonarqube"){
        withSonarQubeEnv("sonarqube") {
        sh 'sonar-scanner  -Dsonar.projectKey=sonarqube  -Dsonar.sources=.  -Dsonar.host.url=http://localhost:9000  -Dsonar.login=6427ddd395e6d22fd32a90b1ee936c112775e3f4'
        }
    }
    
    stage("Classes de Teste") {
        sh 'pytest -W ignore::DeprecationWarning'
    }

    
}