import csv
import json


if __name__ == "__main__":
    inFile = open("resources/users.csv", "r")
    outFile = open("output/users.json", "w")

    headers = ["First Name", "Last Name", "Age"]
    reader = csv.DictReader(inFile, headers)

    for record in reader:
        json.dump(record, outFile)
        outFile.write("\n")