#!/usr/bin/python3
"""read from json then add the args and save it to file"""
import sys
load_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file


def main():
    fileName = "add_item.json"
    try:
        lis = load_json(fileName)
    except FileNotFoundError:
        lis = []

    for a in sys.argv[1:]:
        lis.append(a)

    save_json(lis, fileName)


if __name__ == "__main__":
    main()
