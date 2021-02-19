pipeline {
	agent any
	stages {
	    stage('sleep 30 sec') {
		steps{
			sh "sleep 30"
		}
            }
	    stage('git repo & clean') {
		steps{
			sh "rm -rf iguazio_execersie"
			sh "git clone https://github.com/AdiSchwartz869/iguazio_execersie.git"
		}
            }
	    stage('Run hello') {
		steps {
			sh "python -u my_script.py"
		}
	   }
	    stage('Run weather') {
		steps {
			sh "python -u .weather.py"
		}
	   }
	}
}	
	
