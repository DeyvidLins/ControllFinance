node('master') {
    stage("Clonando Repositório") {
        checkout scm

    }
    stage("Classes de Teste") {
        sh 'pytest -vv --cov -W ignore::DeprecationWarning'
    }

    
}