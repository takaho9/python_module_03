# === Expected output ===
#
# $> python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
# === Inventory System Analysis ===
# Redundant item 'sword' - discarding
# Error - invalid parameter 'hello'
# Quantity error for 'key': invalid literal for int() with base 10: 'value'
# Got inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1}
# Item list: ['sword', 'potion', 'shield', 'armor', 'helmet']
# Total quantity of the 5 items: 12
# Item sword represents 8.3%
# Item potion represents 41.7%
# Item shield represents 16.7%
# Item armor represents 25.0%
# Item helmet represents 8.3%
# Item most abundant: potion with quantity 5
# Item least abundant: sword with quantity 1
# Updated inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1, 'magic_item': 1}

import sys

def argv_to_inventory() -> dict[str, int]:
    inventory = {}
    for arg in sys.argv[1:]:
        try:
            k, v = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter {arg}")
        if k in inventory.keys():
            print(f"Redundant item {arg} - discarding")
            continue

        try:
            inventory.update({k: int(v)})
        except ValueError as e:
            print(f"Quantity error for {k}: {e}")

    return inventory





def main() -> None:
    inventory = argv_to_inventory()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys()   )}")
    len_items = sum(inventory.values())
    len_item_types = len(inventory.keys())
    print(f"# Total quantity of the {len_item_types} items: {len_items}")


if __name__ == "__main__":
    main()
