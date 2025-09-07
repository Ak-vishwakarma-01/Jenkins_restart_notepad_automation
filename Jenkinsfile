pipeline {
    agent any

    stages {
        stage('Create File') {
            steps {
                script {
                    if (!fileExists('done_create.flag')) {
                        bat 'python scripts\\1create_file.py'
                        writeFile file: 'done_create.flag', text: 'done'
                        echo "Created done_create.flag"
                    } else {
                        echo 'Skipping Create File - already done'
                    }
                }
            }
        }

        stage('Restart System') {
            steps {
                script {
                    if (!fileExists('done_restart.flag')) {
                        // create the flag BEFORE restarting so it persists
                        writeFile file: 'done_restart.flag', text: 'done'
                        echo "Created done_restart.flag (will now restart)"
                        bat 'python scripts\\2restart.py'
                    } else {
                        echo 'Skipping Restart - already done'
                    }
                }
            }
        }

        stage('After Restart') {
    steps {
        script {
            if (!fileExists('done_after.flag')) {
                bat 'python scripts\\3after_restart.py'
                writeFile file: 'done_after.flag', text: 'done'
            } else {
                echo 'Skipping After Restart - already done'
            }
        }
    }
}

stage('Install Notepad++') {
    steps {
        script {
            if (!fileExists('done_install.flag')) {
                bat 'python scripts\\4install_notepadd.py'
                writeFile file: 'done_install.flag', text: 'done'
            } else {
                echo 'Skipping Install - already done'
            }
        }
    }
}

    }
}
