from boto3.session import Session
from datetime import datetime, timedelta
import pytz

''' cluster lifetime limit in hours '''
LIMIT = 2
''' your local timezone '''
TIMEZONE = 'Europe/Berlin'

AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_REGION = ''

print('Start cluster check')

emrsession = Session(AWS_ACCESS_KEY, AWS_SECRET_KEY)
emr = emrsession.client('emr', AWS_REGION)

local_tz = pytz.timezone(TIMEZONE)
today = local_tz.localize(datetime.today(), is_dst=None)
lifetimelimit = today - timedelta(hours=LIMIT)

clusters = emr.list_clusters(
    CreatedBefore=lifetimelimit,
    ClusterStates=['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING', 'TERMINATING']
)

if clusters['Clusters'] is not None:
    for cluster in clusters['Clusters']:
        print('Terminating Cluster: %s active since: %s' % (cluster['Id'], cluster['Status']['Timeline']['CreationDateTime']))
        emr.terminate_job_flows(
            JobFlowIds=[cluster['Id']]
        )

print('cluster check done')
