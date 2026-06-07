import sys


def main() -> None:
    path, *args = sys.argv
    argc = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {path}")
    if argc == 1:
        print("No arguments provided!")
    else:
        argc_without_path = argc - 1
        print(f"Arguments received: {argc_without_path}")
        i = 0
        while i < argc_without_path:
            print(f"Argument {i+1}: {args[i]}")
            i += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
