import random

ACHIEVEMENTS = [
    "Bonus Hunter", "Code Explorer", "Rigorous Basterd",
    "Awake", "Hackerman", "Pioneer", "Perfectionist",
    "Shopaholic", "Speed Star", "Slot machine",
    "Corewar Champion", "Master of the basics",
    "Meet the pentester", "Low Level Master",
    "Grand Master of all things", "Crowd pleaser",
    "Make it rain", "Missionary",
]

ACHIEVEMENTS_LEN = len(ACHIEVEMENTS)
MIN_COUNT = 3
MAX_COUNT = 10


def gen_player_achievements() -> set[str]:
    count = random.randrange(MIN_COUNT, MAX_COUNT + 1)
    return set(random.sample(ACHIEVEMENTS, count))


def common_achievements(player_list: list[set[str]]) -> set[str]:
    return set(ACHIEVEMENTS).intersection(*player_list)


def distinct_achievements(player_list: list[set[str]]) -> set[str]:
    return set().union(*player_list)


def missing_achievements(player: set[str]) -> set[str]:
    return set(ACHIEVEMENTS).difference(player)


def exclusive_achievements(
    player: set[str],
    others: list[set[str]]
) -> set[str]:
    return player.difference(distinct_achievements(others))


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    players = [alice, bob, charlie, dylan]
    print(f"\nAll distinct achievements: {distinct_achievements(players)}")
    print(f"\nCommon achievements: {common_achievements(players)}")

    others = [bob, charlie, dylan]
    print(f"\nOnly Alice has: {exclusive_achievements(alice, others)}")
    others = [alice, charlie, dylan]
    print(f"Only Bob has: {exclusive_achievements(bob, others)}")
    others = [alice, bob, dylan]
    print(f"Only Charlie has: {exclusive_achievements(charlie, others)}")
    others = [alice, bob, charlie]
    print(f"Only Dylan has: {exclusive_achievements(dylan, others)}")

    print(f"\nAlice is missing: {missing_achievements(alice)}")
    print(f"Bob is missing: {missing_achievements(bob)}")
    print(f"Charlie is missing: {missing_achievements(charlie)}")
    print(f"Dylan is missing: {missing_achievements(dylan)}")


if __name__ == "__main__":
    main()
