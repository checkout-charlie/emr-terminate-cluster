#emr-terminate-cluster

a simple script to check and terminate AWS EMR clusters which runs longer as estimated.
works on **Python3.4** or higher with usage of the boto3 package

##usage

###config###
add the absolute path to the directory to BASEPATH in check_clusters.sh
add the AWS credentials and region to main.py
check inside the directory if the executing user has permission to read/write/execute

###launcher###
usage of the sh launcher script. launchs the virtualenv, installs the requirements and executes the script
(virtualenv, pip should be installed)
`
sh check_cluster.sh
`

##simple###
`
python3 main.py
`
