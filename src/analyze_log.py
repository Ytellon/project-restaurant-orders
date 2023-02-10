def favorite_order(name, order, list_of_orders):
    count = 0
    for orders in list_of_orders:
        if orders["person"] == name and orders["order"] == order:
            count += 1
    return count


def most_popular_order(name, list_of_orders):
    all_orders = {}
    for orders in list_of_orders:
        if orders["person"] == name:
            if orders["order"] not in all_orders:
                all_orders[orders["order"]] = 1
            else:
                all_orders[orders["order"]] += 1
    return max(all_orders, key=all_orders.get)


def which_dish_not_ordered(name, list_of_orders):
    orders = set()
    client_orders = set()
    for order in list_of_orders:
        orders.add(order["order"])
        if order["person"] == name:
            client_orders.add(order["order"])
    return orders.difference(client_orders)


def which_days_never_attended(name, list_of_orders):
    days = set()
    client_days = set()
    for order in list_of_orders:
        days.add(order["day"])
        if order["person"] == name:
            client_days.add(order["day"])
    return days.difference(client_days)


def analyze_log(path_to_file):
    raise NotImplementedError
