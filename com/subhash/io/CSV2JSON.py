import csv
import json
import random

if __name__ == "__main__":
    inFile = open("resources/users.csv", "r")
    outFile = open("output/users.json", "w")

    headers = ["First Name", "Last Name", "Age"]
    reader = csv.DictReader(inFile, headers)

    for record in reader:
        # update age randomly
        new_age = random.randint(30, 40)
        record["Age"] = new_age

        # save record to jason file
        json.dump(record, outFile)
        outFile.write("\n")
