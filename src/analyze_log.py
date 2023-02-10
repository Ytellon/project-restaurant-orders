import csv


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
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        list_of_orders = []
        with open(path_to_file) as file_open:
            reader = csv.reader(file_open)
            for name, order, day in reader:
                list_of_orders.append(
                    {"person": name, "order": order, "day": day})

        most_popular_order_maria = most_popular_order("maria", list_of_orders)
        favorite_order_arnaldo = favorite_order(
            "arnaldo", "hamburguer", list_of_orders)
        which_dish_not_ordered_joao = which_dish_not_ordered(
            "joao", list_of_orders)
        which_days_never_attended_joao = which_days_never_attended(
            "joao", list_of_orders)

        with open("data/mkt_campaign.txt", "w") as f:
            f.write(
                f"{most_popular_order_maria}\n"
                f"{favorite_order_arnaldo}\n"
                f"{which_dish_not_ordered_joao}\n"
                f"{which_days_never_attended_joao}\n"
            )

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
