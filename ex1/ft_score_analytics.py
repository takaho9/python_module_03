import sys


def parse_scores(args: list[str]) -> list[int]:
    scores = []
    for arg in args:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def print_stats(scores: list[int]) -> None:
    len_scores = len(scores)
    sum_scores = sum(scores)
    max_scores = max(scores)
    min_scores = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len_scores}")
    print(f"Total score: {sum_scores}")
    print(f"Average score: {sum_scores / len_scores}")
    print(f"High score: {max_scores}")
    print(f"Low score: {min_scores}")
    print(f"Score range: {max_scores-min_scores}")


def main() -> None:
    print("=== Player Score Analytics ===")
    path, *args = sys.argv
    scores = parse_scores(args)
    if len(scores) == 0:
        print(
            f"No scores provided. Usage: python3 {path} <score1> <score2> ...")
    else:
        print_stats(scores)


if __name__ == "__main__":
    main()
