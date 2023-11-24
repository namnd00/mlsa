import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    # Iterate over each record in the event
    for record in event['Records']:
        srcBucket = record['s3']['bucket']['name']
        srckey = record['s3']['object']['key']
        desBucket = "MLSA-DataLake-<your initials>"

        # Extract the folder name from the source key
        desFolder = srckey[0:srckey.find('.')]
        desKey = "bank_customer_db/" + desFolder + "/" + srckey

        # Set the source and destination parameters for the S3 copy operation
        source = { 'Bucket': srcBucket, 'Key': srckey}
        dest = { 'Bucket': desBucket, 'Key': desKey}

        # Copy the file from the source bucket to the destination bucket
        s3.meta.client.copy(source, desBucket, desKey)
        
    return {
        'statusCode': 200,
        'body': json.dumps('files ingested')
    }