class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"

class Cart:
    def __init__(self, store):
        self.store = store
        self.items = {}

    def add_to_cart(self, product_name, quantity):
        product = self.store.find_product(product_name)
        if product and product.stock >= quantity:
            if product_name in self.items:
                self.items[product_name] += quantity
            else:
                self.items[product_name] = quantity
            product.stock -= quantity  # Уменьшаем остаток товара на складе
        elif product:
            print(f"Ошибка: недостаточно товара '{product_name}' на складе.")
        else:
            print(f"Ошибка: товар '{product_name}' не найден.")

    def remove_from_cart(self, product_name):
        if product_name in self.items:
            del self.items[product_name]
        else:
            print(f"Товар '{product_name}' не найден в корзине.")

    def show_cart(self):
        total_cost = 0
        if not self.items:
            print("Корзина пуста.")
            return
        
        print("Товары в корзине:")
        for product_name, quantity in self.items.items():
            product = self.store.find_product(product_name)
            total_cost += product.price * quantity if product else 0
            print(f"{product_name}: {quantity} шт, Общая стоимость: {product.price * quantity}")
        
        print(f"Общая стоимость корзины: {total_cost}")

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, stock):
        new_product = Product(name, price, stock)
        self.products.append(new_product)

    def show_products(self):
        if not self.products:
            print("В магазине нет товаров.")
            return
        print("Доступные товары:")
        for product in self.products:
            print(product.show_info())

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def process_order(self, cart):
        for product_name in cart.items:
            product = self.find_product(product_name)
            if product:
                product.stock -= cart.items[product_name]  # Уменьшаем остаток на складе
        print("Заказ обработан.")