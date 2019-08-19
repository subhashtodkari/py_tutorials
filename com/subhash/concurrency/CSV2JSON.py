import csv
import json
import queue
from concurrent.futures.thread import ThreadPoolExecutor
import random

outFile = open("output/users.json", "w")

# synchronous queue
q = queue.Queue()


# write records to file synchronously to avoid overwriting in multi-threading situation
def write_json_sync():
    try:
        while 1:
            msg = q.get()
            if isinstance(msg, str):
                # check if it is last message
                if msg == "done":
                    print("stopping reading from queue -----")
                    # end of thread by exiting while loop
                    break
            json.dump(msg, outFile)
            outFile.write("\n")
            outFile.flush()
    except Exception as e:
        print(e)


# process dictionary object, edit it, write to file or send it to queue like AWS SQS
def process_dict(obj):
    try:
        # string message is also expected to signal reader thread to stop processing
        # check if obj is of type dictionary then only edit
        if isinstance(obj, dict):
            new_age = random.randint(30, 40)
            obj["Age"] = new_age
        q.put(obj)
    except Exception as e:
        print(e)
        print("failed to process message")


if __name__ == "__main__":
    inFile = open("resources/users.csv", "r")

    headers = ["First Name", "Last Name", "Age"]
    reader = csv.DictReader(inFile, headers)

    # Threadpool executor with 2 worker threads
    with ThreadPoolExecutor(max_workers=5) as pool:
        # start output file writer thread, it will occupy one thread from pool
        pool.submit(write_json_sync)

        futures = []
        # process input records and send to sync queue using remaining threads from pool
        for record in reader:
            futures.append(pool.submit(process_dict, record))

        for future in futures:
            future.result()

        # send final message to stop writer thread
        futures.append(pool.submit(process_dict, "done"))

        print("shutting down threadpool...")
        # shutdown thread pool
        pool.shutdown()

        print("Processing finished, please check output file: ", outFile.name)
