import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "use", "release"]
    while (True):
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while (len(events) > 0):
        index = random.randint(0, len(events)-1)
        event = events[index]
        del events[index]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    g = gen_event()
    for i in range(1000):
        player, action = next(g)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = []
    for i in range(10):
        ten_events += [next(g)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
