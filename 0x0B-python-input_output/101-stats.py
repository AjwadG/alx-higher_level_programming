#!/usr/bin/python3
"""
reads stdin line by line and computes metrics:

"""
import sys


def print_stat(size, stats):
    """prints stats in formated way"""
    s = "File size: {}\n".format(size)
    for a in stats:
        if stats[a] != 0:
            s += "{}: {}\n".format(a, stats[a])
    sys.stdout.write(s)
    sys.stdout.flush()


def main():
    size = 0
    stats = {"200": 0, "301": 0, "400": 0,
             "401": 0, "403": 0, "404": 0,
             "405": 0, "500": 0}
    count = 0
    try:
        for line in sys.stdin:
            try:
                split = line[:-1].split()[-2:]
                size += int(split[-1])
                if split[0] in stats:
                    stats[split[0]] += 1
            except Exception:
                continue
            count += 1

            if count % 10 == 0:
                print_stat(size, stats)
        print_stat(size, stats)
    except KeyboardInterrupt:
        print_stat(size, stats)
        raise


if __name__ == "__main__":
    main()
