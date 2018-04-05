pipeline {
	agent none
	options {
		skipDefaultCheckout() 
	}
	
	stages {
		stage('Build') {
			agent { label 'docs-build' }
			
			steps {
				deleteDir()
				
				checkout scm
				
				withEnv(["PATH+PERL=${env.PERL_DIR}", "PATH+TEX=${env.TEX_DIR}", "PATH+PYTHON=${env.PY_DIR}"]) {
					bat("latexmk")
				}
			}
			
			post {
				success {
					archiveArtifacts 'output/*.pdf'
				}
			}
		}
	}
}