from classes import Product, Store, Cart

store = Store() 
store.add_product("Apple", 10, 100) # Название, цена, количество 
store.add_product("Banana", 5, 50)

# Показываем товары в магазине 
store.show_products() 

# Создаем корзину 
cart = Cart(store) 

# Добавляем товары в корзину 
cart.add_to_cart("Apple", 3) 
cart.add_to_cart("Banana", 5) 

# Показываем корзину 
cart.show_cart() 

# Обрабатываем заказ 
store.process_order(cart) 

# Показываем остатки в магазине 
store.show_products()