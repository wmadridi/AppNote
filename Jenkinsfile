pipeline {
    agent any
    stages{
        stage('Checkout') {
            steps {
                // Récupère les playbooks Ansible depuis le dépôt Git
            checkout([$class: 'GitSCM',
                branches: [[name: '*/main']],
                doGenerateSubmoduleConfigurations: false,
                extensions: [],
                submoduleCfg: [],
                userRemoteConfigs: [[url: 'https://github.com/wmadridi/AppNote.git']]
                ])
                }
        }
    stage('Execute Ansible Playbook'){
        agent { node { label 'Ansible'} }
            environment{
                // Définit les variables d'environnement pour l'utilisateur distant et les informations d'authentification SSH
                remoteUser = 'ubuntu'
                sshKey = credentials('a3bfb168-fc51-464e-8d24-3384d077e22c')
                }
                steps{
                // Exécute les commandes Ansible pour déployer les playbooks sur l'agent distant
                    withEnv(["ANSIBLE_CONFIG=workspace/AppNote/ansible.cfg"]) {
                        sh "ansible-playbook -i host.yml --user='${remoteUser}' --private-key='${sshKey}' playbook.yml"
                        }
                    }
        }
    }
}