# py_tutorials
My sample python programs

1. csv to json conversion - sequential processing
python -m com.subhash.io.CSV2JSON

2. csv to json conversion - concurrent processing
python -m com.subhash.concurrency.CSV2JSON

3. aws - various s3 operations - you must have
    1. boto3 installed
    2. ~/.aws/credentails - file containing default aws_access_key_id and aws_secret_access_key
    3. ~/.aws/config - file containing default region
python -m com.subhash.aws.s3

4. Basics: parsing program arguments
python -m com.subhash.basics.args_parsing --name Subhash --msg  hello

5. aws - various sqs operations like send, receive and delete message - you must have
    1. boto3 installed
    2. ~/.aws/credentails - file containing default aws_access_key_id and aws_secret_access_key
    3. ~/.aws/config - file containing default region
    4. and a queue created in AWS account
python -m com.subhash.aws.sqs
python -m com.subhash.aws.sqs -h
python -m com.subhash.aws.sqs --cmd send
python -m com.subhash.aws.sqs --cmd --rec
