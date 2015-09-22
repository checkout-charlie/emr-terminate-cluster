#emr-terminate-cluster

a simple script to check and terminate AWS EMR clusters which runs longer as estimated.
works on **Python3.4** or higher with usage of the boto3 package

##usage

###launcher###
usage of the sh launcher script. lanchs the virtualenv, installs the requirements and executes the script
(virtualenv, pip should be installed)
`
sh check_cluster.sh
`

##simple###
`
python3 main.py
`
