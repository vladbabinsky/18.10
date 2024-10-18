class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, item):
        self.items.append(item)

    def view_cart(self):
        return self.items

    def clear_cart(self):
        self.items = []
