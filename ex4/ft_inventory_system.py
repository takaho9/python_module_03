import sys


def argv_to_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            k, v = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if k in inventory.keys():
            print(f"Redundant item '{k}' - discarding")
            continue
        try:
            inventory.update({k: int(v)})
        except ValueError as e:
            print(f"Quantity error for '{k}': {e}")
    return inventory


def max_count(inventory: dict[str, int]) -> str:
    max_key = list(inventory)[0]
    for k in inventory.keys():
        if inventory[max_key] < inventory[k]:
            max_key = k
    return max_key


def min_count(inventory: dict[str, int]) -> str:
    min_key = list(inventory)[0]
    for k in inventory.keys():
        if inventory[min_key] > inventory[k]:
            min_key = k
    return min_key


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = argv_to_inventory()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    len_items = sum(inventory.values())
    len_item_types = len(inventory.keys())
    print(f"Total quantity of the {len_item_types} items: {len_items}")
    for k in inventory.keys():
        print(f"Item {k} represents {round(inventory[k]/len_items*100, 1)}%")
    if inventory:
        most_name = max_count(inventory)
        least_name = min_count(inventory)
        most_qty = inventory[most_name]
        least_qty = inventory[least_name]
        print(f"Item most abundant: {most_name} with quantity {most_qty}")
        print(f"Item least abundant: {least_name} with quantity {least_qty}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
