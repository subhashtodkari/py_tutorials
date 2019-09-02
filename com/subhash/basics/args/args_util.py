import sys

# library file


def print_help_if_no_args(parser):
    if len(sys.argv) == 1:
        print("No arguments provided. Please check args usage below:")
        parser.print_help()
        print()
        print("Application will proceed with default values...")
        print()
