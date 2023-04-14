cat jenkins-docker-example/Jenkinsfile 
node {
  stage 'Checkout'
  git url: 'https://github.com/agani3-UNH-DSCI/sample-jenkins-pipeline.git'

  stage 'build'
  docker.build('app')

  stage 'deploy'
  sh './deploy.sh'
}
