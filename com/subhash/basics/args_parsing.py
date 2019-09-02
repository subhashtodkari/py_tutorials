import argparse

parser = argparse.ArgumentParser(description='sends or receives SQS messages')
parser.add_argument("--name", required=False, help='name of the person', default='Subhash')
parser.add_argument("--msg", required=False, help='message for the person', default='Hi there')
args = parser.parse_args()
# print(args)


if __name__ == "__main__":
    print(args.name, ' : ', args.msg)
    print("This is sample program for program argument parsing, please try with and without passing argument to test "
          "required arguments and default values for not-required arguments")
