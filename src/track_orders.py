class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"person": customer, "order": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        all_orders = {}
        for orders in self.orders:
            if orders["person"] == customer:
                if orders["order"] not in all_orders:
                    all_orders[orders["order"]] = 1
                else:
                    all_orders[orders["order"]] += 1
        return max(all_orders, key=all_orders.get)

    def get_never_ordered_per_customer(self, customer):
        orders = set()
        client_orders = set()
        for order in self.orders:
            orders.add(order["order"])
            if order["person"] == customer:
                client_orders.add(order["order"])
        return orders.difference(client_orders)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        client_days = set()
        for order in self.orders:
            days.add(order["day"])
            if order["person"] == customer:
                client_days.add(order["day"])
        return days.difference(client_days)

    def get_busiest_day(self):
        all_orders = {}
        for orders in self.orders:
            if orders["day"] not in all_orders:
                all_orders[orders["day"]] = 1
            else:
                all_orders[orders["day"]] += 1
        return max(all_orders, key=all_orders.get)

    def get_least_busy_day(self):
        all_orders = {}
        for orders in self.orders:
            if orders["day"] not in all_orders:
                all_orders[orders["day"]] = 1
            else:
                all_orders[orders["day"]] += 1
        return min(all_orders, key=all_orders.get)
