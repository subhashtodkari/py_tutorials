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
    3. map/dict
    4. list
    5. set

python -m com.subhash.basics.collections


8. Python Basics - properties or configuration files
    1. write configuration file - using configparser

python -m com.subhash.basics.properties


9. aws - DynamoDB tutorial
    1. create or access table
    2. add item
    3. search item
    4. delete item
    5. delete table

python -m com.subhash.aws.dynamodb


10. com.subhash.util package - holds common library objects
    1. number_to_words - converts number to words in chunks of billions


11. Artificial Intelligence - all code under com.subhash.ai
    com.subhash.ai.util - contains library objects for other AI programs
        1. text_to_speech - text to speech converter using gTTS (Google Text To Speech) API
            It caches audio data into files and reuse them if available
            reference - https://www.geeksforgeeks.org/convert-text-speech-python/
            pip install gTTS
        2. speech_to_text__mic_input - speech recognizer - listens to mic input and converts speech to text
            using speech_recognizer library
            reference - https://realpython.com/python-speech-recognition/
            pip install SpeechRecognition
            pip install pyaudio (known issues for python 3.6+ on windows
                - pip install pipwin
                - pipwin install pyaudio
                )

        3. speech_to_text__file_input - speech recognizer - listens to audio file input and converts speech to text
            using speech_recognizer library
            reference - https://realpython.com/python-speech-recognition/


