import random

# Item Price Bucket
def get_price(name: str) -> float:
    
    if name.lower() == "shirt":
        return 5.99
    elif name.lower() == "pant":
        return 9.99
    elif name.lower() == "sweater":
        return 7.99
    elif name.lower() == "raincoat":
        return 11.99
    
# Discount Strategies
class DiscountStrategy:
    def apply_discount(self, total_price: float) -> float:
        raise NotImplementedError("This method should be overridden by subclasses")

# Percentage Discount
class PercentageDiscount:
    def apply_discount(self, total_price: float) -> float:
        discount_price = total_price - (total_price *(10/100.0))
        return discount_price

# Buy X Get Y Free
class BuyXGetYFree:
    def apply_discount(self, total_price: float) -> float:
        pass

# Fixed Amount Off:
class FixedDiscount:
    def apply_discount(self, total_pirce: float) -> float:
        discount_price = total_pirce - 2.99
        return discount_price

# Item class
class Item:

    id: int
    name: str
    price: float

    def __init__(self, name):
        self.id = random.randint(956,99898)
        self.name = name
        self.price = get_price(name)


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.cart: list[Item] =  []

    def add(self, name: str) -> None:
        self.cart.append(Item(name))

    def calculate_total_price(self) -> float:
        total_price = sum(item.price for item in self.cart)
        return total_price
    
    def apply_discount(self, discount_method: DiscountStrategy):
        total_price = self.calculate_total_price()
        return discount_method.apply_discount(total_price)
    
    def display_cart(self) -> None:
        print("\nCart Items:")
        for item in self.cart:
            print("==========================")
            print(f"ID: {item.id}")
            print(f"Item: {item.name}")
            print(f"Price: {item.price}")
            print("==========================")
            print("--------------------------\n")

# Creating Our shoppingcart object        

cart = ShoppingCart()

cart.add("shirt")
cart.add("pant")
cart.add("raincoat")
cart.display_cart()
print(f"Total Price after Discount: {cart.apply_discount(PercentageDiscount()):.2f}")
# print(f"{cart.apply_discount(FixedDiscount()):.2f}")
print("-------------------------------------------------------------------------------")
