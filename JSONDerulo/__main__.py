import json as jason
from argparse import ArgumentParser

def command_line():
    parser = ArgumentParser(
        prog='derulo',
        description='A JSON serialization that is dirty to talk about'
    )
    parser.add_argument('--say', action='count')

    return parser.parse_args()

def main():
    derulo = dict()
    args = command_line()
    derulo['JSONDerulo'] = 'Watcha Say' if args.say else 'JSONDerulo'

    print(derulo)

if __name__ == '__name__':
    main()
