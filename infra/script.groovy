node('master') {
    stage("Clonando Repositório") {
        checkout scm

    }
    stage("Instalação das Bibliotecas Python"){
        sh 'pip install -r requirements.txt'
    }
    stage("Classes de Teste") {
        sh 'pytest -vv --cov -W ignore::DeprecationWarning'
    }

    
}