from helpers import mask_data
from constants import QUEUE_URL, DB_CONNECTION_STRING
import boto3
import psycopg2

# inserting the data into the table using pipeline
def insert_data(data):
    conn = psycopg2.connect(DB_CONNECTION_STRING)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (data['user_id'], data['device_type'], mask_data(data['ip']), mask_data(data['device_id']), data['locale'], data['app_version'], data['create_date']))
    conn.commit()
    conn.close()
    print(f"Inserted data for user {data['user_id']}")

def etl_process():
    sqs = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://localhost:4576')
    while True:
        messages = sqs.receive_message(QueueUrl=QUEUE_URL, MaxNumberOfMessages=10)
        for message in messages:
            print(f"Processing message {message['MessageId']}")
            insert_data(message)
            print(f"Processed message {message['MessageId']}")

if __name__ == "__main__":
    etl_process()
