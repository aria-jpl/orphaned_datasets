import sys
import json
import requests
from datetime import datetime


DATASET_TYPE = sys.argv[1]  # ["slc", "interferogram"]
BUCKET = sys.argv[2]  # aria-ops-dataset-bucket
MODE = sys.argv[3]  # ["PRETEND", "PERMANENT"]

queue = 'system-jobs-queue'
job_type = "job-purge-orphaned-datasets"
job_release = sys.argv[4]  # release-20190722-3
tag_name = '["od_orphan_finder_{}_{}"]'.format(DATASET_TYPE, datetime.now().date())

# https://128.149.127.151/mozart/api/v0.1/job/submit
job_submit_url = sys.argv[5]

job_params = {
    "bucket": BUCKET,
    "dataset_type": DATASET_TYPE,
    "mode": MODE
}
params = {
    'queue': queue,
    'priority': '6',
    'job_name': job_type,
    'tags': tag_name,
    'type': "{}:{}".format(job_type, job_release),
    'params': json.dumps(job_params),
    'enable_dedup': False
}

req = requests.post(job_submit_url, params=params, verify=False)
if req.status_code != 200:
    req.raise_for_status()
print(req.text)
result = req.json()
print(result)
