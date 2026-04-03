class CoffeeShop:

    def __init__(self):
        self.customers = []

    def add_customer(self, name):
        self.customers.append(name)

    def remove_customer_at(self, index):
        try:
            del self.customers[index]
        except IndexError:
            pass

    def get_customer_at(self, index):
        try:
            return self.customers[index]
        except IndexError:
            return "Index Error"

    def get_num_customers(self):
        return len(self.customers)
