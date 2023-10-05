#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv)
    arg = "argument" if length == 2 else "arguments"
    if (length == 1):
        print(f"0 {arg}.")
    else:
        print(f"{length - 1} {arg}:")
        for a in range(1, length):
            print(f"{a}: {argv[a]}")


if __name__ == "__main__":
    main()
