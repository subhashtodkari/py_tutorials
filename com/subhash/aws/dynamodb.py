import boto3

# A configured AWS user (using ~/.aws/credentials and config file) must have AmazonDynamoDBFullAccess permissions

dynamodb = boto3.resource("dynamodb")


def create_users_table():
    print('\nCreating table in dynamodb')
    try:
        table = dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'last_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        print('waiting till table is created...')
        table.meta.client.get_waiter('table_exists').wait(TableName='users')

        print('Table created, item count: ', table.item_count)
    except Exception as e:
        print('Table already exists..', e)
        table = dynamodb.Table('users')

    return table


def add_user_to_table(table, username, firstname, lastname, age, acc_type):
    table.put_item(
        Item={
            'username': username,
            'first_name': firstname,
            'last_name': lastname,
            'age': age,
            'account_type': acc_type
        }
    )


def get_user(table, username, l_name):
    response = table.get_item(
        Key={
            'username': username,
            'last_name': l_name
        }
    )
    item = response['Item']
    return item


def update_item(table, username, l_name, age):
    item = get_user(table, username, l_name)
    table.update_item(
        Key={
            'username': username,
            'last_name': l_name
        },
        UpdateExpression='Set age = :val1',
        ExpressionAttributeValues={
            ':val1': age
        }
    )


def delete_user(table, username, l_name):
    table.delete_item(
        Key={
            'username': username,
            'last_name': l_name
        }
    )


if __name__ == "__main__":
    t = create_users_table()
    add_user_to_table(t, 'superuser', 'f_name', 'l_name', 30, 'standard_user')
    user = get_user(t, 'superuser', 'l_name')
    print('Searched user: ', user)
    print('Updated age to 50')
    update_item(t, 'superuser', 'l_name', 50)
    user = get_user(t, 'superuser', 'l_name')
    print('Searched user: ', user)
    print('deleting user')
    delete_user(t, 'superuser', 'l_name')
    print('Table items: ', t.item_count)
    print("Deleting table")
    t.delete()
