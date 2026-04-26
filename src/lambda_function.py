import boto3
import datetime
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # Age threshold: 365 days
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=365)
    
    try:
        snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
        deleted = 0

        for snap in snapshots:
            if snap['StartTime'] < cutoff:
                sid = snap['SnapshotId']
                try:
                    logger.info(f"Deleting snapshot: {sid}")
                    ec2.delete_snapshot(SnapshotId=sid)
                    deleted += 1
                except ClientError as e:
                    logger.error(f"Error deleting {sid}: {e.response['Error']['Message']}")

        return {"status": "complete", "deleted_count": deleted}
    except Exception as e:
        logger.error(f"Execution failed: {str(e)}")
        raise e