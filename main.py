
import argparse

def greet():
    print("Hello, world!")

def run_task(task_name):
    if task_name == "greet":
        greet()
    else:
        print(f"Unknown task: {task_name}")

def main():
    parser = argparse.ArgumentParser(description="Awesome CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--task", required=True)

    args = parser.parse_args()

    if args.command == "run":
        run_task(args.task)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
