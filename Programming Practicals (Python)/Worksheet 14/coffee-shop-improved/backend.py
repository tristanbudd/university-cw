class CoffeeShop:

    def __init__(self, limit=3):
        self.customers = []
        self.limit = limit

    def add_customer(self, name):
        if name in self.customers:
            raise ValueError("Customer already exists!")
        elif name == "" or name == " ":
            raise ValueError("Invalid customer name!")
        elif self.get_num_customers() >= self.limit:
            raise ValueError("Customer limit reached!")
        else:
            self.customers.append(name)

    def remove_customer_at(self, index):
        del self.customers[index]

    def get_customer_at(self, index):
        return self.customers[index]

    def get_num_customers(self):
        return len(self.customers)

    def get_limit(self):
        return self.limit
