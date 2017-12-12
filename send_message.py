import boto3
import json


def lambda_handler(event, context):

  sqs = boto3.resource('sqs', region_name='us-east-1')
  queue = sqs.get_queue_by_name(QueueName='sqsFifoTest')

  response = queue.send_message(
      # MessageBody='{}',
      MessageBody=json.dumps(event),
      DelaySeconds=0,
      MessageAttributes={
          'service_class': {
              'StringValue': 'Service::Worker',
              'DataType': 'String'
          }
      }
  )
print(response)