import boto3
import argparse
from com.subhash.basics.args import args_util

# argument parsing
parser = argparse.ArgumentParser(description='sends, receives and/or deletes SQS messages')
parser.add_argument("--cmd", required=False, help='command: "send" or "rec", default is "rec"', default='rec')
args = parser.parse_args()

# A configured AWS user (using ~/.aws/credentials and config file) must have AmazonSQSFullAccess permissions
sqs = boto3.client("sqs")

# queue name that exists in AWS
queue_url = "https://sqs.us-east-1.amazonaws.com/274754587255/sqs_temp_queue"


def send_msg(msg):
    print('\nSending message to queue: ', msg)
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            "Title": {
                'DataType': 'String',
                'StringValue': 'FirstMessage'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'Subhash Todkari'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            msg
        )
    )

    print('Message sent: ', response['MessageId'])


def receive_and_delete_msg():
    print('Retrieving message from queue')
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    if 'Messages' not in response:
        print('No message available')
        return

    message = response['Messages'][0]

    print('\nMessage: ')
    print(message)

    print('\n')
    print('\n')

    delete_msg(message)


def delete_msg(message):
    print('Deleting message now')

    receipt_handle = message['ReceiptHandle']

    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

    print('\nMessage deleted')


if __name__ == "__main__":
    args_util.print_help_if_no_args(parser)

    if args.cmd == 'send':
        send_msg('Some nice message to send to queue')
    else:
        receive_and_delete_msg()
