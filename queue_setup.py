#setting up amazon AWS SQS Queue

import boto3

def setup_queue():
    sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://localhost:4576')
    response = sqs.create_queue(QueueName='test')

if __name__ == "__main__":
    setup_queue()
