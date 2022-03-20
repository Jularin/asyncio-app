import asyncio
import argparse
from typing import List

from connections import simple_client, execute


def configure_parser(commands: List[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help=f"Available commands: {' '.join(commands)}")
    parser.add_argument("-d", "--data", help="string for task execution")
    parser.add_argument("-t", "--task", help="task type. use only when create task")
    parser.add_argument("-id", help="Task identifier to get task status or result")
    return parser


def add_args_error():
    print("Please add arguments")
    exit(-1)


if __name__ == '__main__':
    commands = ["create", "get_status", "get_result", "execute"]
    parser = configure_parser(commands)
    args = parser.parse_args()

    if args.command not in commands:
        print(f"Available commands: {' '.join(commands)}")
        exit(-1)

    if args.command == "create":
        if args.data is None or args.task is None:
            add_args_error()
        asyncio.run(simple_client(f"create {args.task} {args.data}"))

    elif args.command == "get_status":
        if args.id is None:
            add_args_error()
        asyncio.run(simple_client(f"get_status {args.id}"))

    elif args.command == "get_result":
        if args.id is None:
            add_args_error()
        asyncio.run(simple_client(f"get_result {args.id}"))

    elif args.command == "execute":
        if args.data is None or args.task is None:
            add_args_error()
        try:
            asyncio.run(execute(args.task, args.data))
        except KeyboardInterrupt:
            print("Okay dude, I'm exiting")
            exit(-1)

