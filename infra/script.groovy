node('master') {
    stage("Limpeza de Cache e Clonando Repositório") {
        cleanWs()
        checkout scm

    }
    
    stage("Classes de Teste") {
        sh 'python3 pytest -W ignore::DeprecationWarning'
    }

    
}