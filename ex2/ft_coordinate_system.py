import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        prompt = "Enter new coordinates as floats in format 'x,y,z': "
        coords = input(prompt).split(",")
        if len(coords) != 3:
            print("Invalid syntax")
            continue

        result = []
        for coord in coords:
            try:
                result += [float(coord)]
            except ValueError as e:
                print(f"Error on parameter '{coord}': {e}")
                break
        else:
            return (result[0], result[1], result[2])


def distance(
    a: tuple[float, float, float], b: tuple[float, float, float]
) -> float:
    x_dist = a[0]-b[0]
    y_dist = a[1]-b[1]
    z_dist = a[2]-b[2]
    dist = math.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
    dist = round(dist, 4)
    return dist


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    dist = distance(first, (0.0, 0.0, 0.0))
    print(f"Distance to center: {dist}")
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    dist = distance(first, second)
    print(f"Distance between the 2 sets of coordinates: {dist}")


if __name__ == "__main__":
    main()
