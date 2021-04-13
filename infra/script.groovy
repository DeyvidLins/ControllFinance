node('master') {
    stage("Clonando Repositório") {
        checkout scm

    }
    stage("Instalação das Bibliotecas Python"){
        sh 'pip3 install -r requirements.txt'
    }
    stage("Classes de Teste") {
        sh 'python3 pytest -vv --cov -W ignore::DeprecationWarning'
    }

    
}