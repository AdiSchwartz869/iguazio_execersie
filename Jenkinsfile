pipeline {
	agent any
	stages {
	    stage('git repo & clean') {
		steps{
			sh "git clone https://github.com/AdiSchwartz869/iguazio_execersie.git"
		}
            }
	    stage('Run') {
		steps {
			sh "python -u my_script.py"
		}
	   }
	}
}	
	
