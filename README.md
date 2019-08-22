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
