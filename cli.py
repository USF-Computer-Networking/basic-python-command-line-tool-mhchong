"""
    Author: Marcus Chong

    Basic Python command line tool
"""

import argparse

def parse():
    parser = argparse.ArgumentParser(description='Simple command line tool')

    parser.add_argument('file', help='filename for results')
    parser.add_argument('-x', type=int, help='an integer')
    parser.add_argument('-y', type=int, help='an integer')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--add', action='store_true', help='addition')
    group.add_argument('-s', '--sub', action='store_true', help='subtraction')
    group.add_argument('-m', '--mul', action='store_true', help='multiplication')
    group.add_argument('-d', '--div', action='store_true', help='division')

    return parser.parse_args()

def file_out(filename, result):
    """
        Function to write result to a file
    """
    f = open(filename + ".txt", 'w+')
    f.write(str(result) + '\n')
    f.close()

def run(args):
    """
        Function that computes x and y based on
        user's choice of math operation
    """
    if args.add:
        result = args.x + args.y
    elif args.sub:
        result = args.x - args.y
    elif args.mul:
        result = args.x * args.y
    elif args.div:
        result = args.x / args.y

    file_out(args.file, result)
    return result

def main():
    args = parse()
    print(run(args))

if __name__ == '__main__':
    main()