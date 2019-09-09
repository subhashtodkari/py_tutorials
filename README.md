# py_tutorials
My sample python programs

1. csv to json conversion - sequential processing

python -m com.subhash.io.CSV2JSON

2. csv to json conversion - concurrent processing

python -m com.subhash.concurrency.CSV2JSON

3. aws - various s3 operations - you must have
    1. boto3 installed
    2. ~/.aws/credentials - file containing default aws_access_key_id and aws_secret_access_key
    3. ~/.aws/config - file containing default region

python -m com.subhash.aws.s3

4. Python Basics - parsing program arguments

python -m com.subhash.basics.args_parsing --name Subhash --msg  hello

5. aws - various sqs operations like send, receive and delete message - you must have
    1. boto3 installed
    2. ~/.aws/credentials - file containing default aws_access_key_id and aws_secret_access_key
    3. ~/.aws/config - file containing default region
    4. and a queue created in AWS account

python -m com.subhash.aws.sqs

python -m com.subhash.aws.sqs -h

python -m com.subhash.aws.sqs --cmd send

python -m com.subhash.aws.sqs --cmd --rec

6. Python Basics - Object Oriented Programming - create class and objects
    1. no method or constructor overloading
    2. no 'new' keyword to create object
    3. 'self' ==> 'this' of Java
    4. define static / class attribute
    5. inherit from another class and override methods

python -m com.subhash.basics.oops

7. Python Basics - loops
    1. for loop
    2. while loop
    3. use of range()
    4. uee of 'break' and 'continue'

python -m com.subhash.basics.loops

7. Python Basics - collections/containers
    1. arrays
    2. Counters

python -m com.subhash.basics.collections

