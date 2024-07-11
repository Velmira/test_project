pipeline {
    agent any
     parameters {
        string(name: 'EXECUTOR', defaultValue: '127.0.0.1', description: 'Executor host')
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Browser for UI tests')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Velmira/test_project.git'
            }
        }

        stage('Run API Tests') {
            steps {
                sh 'pytest API/tests --alluredir allure-results'
            }
        }

        stage('Run UI Tests') {
            steps {
                sh 'pytest UI/tests --executor ${EXECUTOR} --browser ${BROWSER}
                --alluredir allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [
                            [path: 'api-results'],
                            [path: 'ui-results']
                        ]
                    ])
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}