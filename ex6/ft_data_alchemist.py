import random


def main() -> None:
    print("=== Game Data Alchemist ===", end="\n\n")
    init_players = ['Alice', 'bob', 'Charlie', 'dylan',
                    'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    capitalized_all = [p.capitalize() for p in init_players]
    capitalized_only = [p for p in init_players if p == p.capitalize()]
    print(f"Initial list of players: {init_players}")
    print(f"New list with all names capitalized: {capitalized_all}")
    print(f"New list of capitalized names only: {capitalized_only}")

    score_dict = {k: random.randint(0, 999) for k in capitalized_all}
    print(f"Score dict: {score_dict}")
    avg = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {avg}")
    high_score_dict = {k: v for k, v in score_dict.items() if v > avg}
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    main()
