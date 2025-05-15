from collections import defaultdict


def displayTable(orders: list[list[str]]) -> list[list[str]]:
    food_items = set()
    table_orders = defaultdict(lambda: defaultdict(int))

    for _, table, food in orders:
        food_items.add(food)
        table_orders[table][food] += 1

    sorted_food_items = sorted(food_items)

    result = []
    result.append(["Table"] + sorted_food_items)

    for table in sorted(table_orders.keys(), key=int):
        row = [table] + [str(table_orders[table].get(food, 0)) for food in sorted_food_items]
        result.append(row)

    return result


orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
          ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
print(displayTable(orders))
