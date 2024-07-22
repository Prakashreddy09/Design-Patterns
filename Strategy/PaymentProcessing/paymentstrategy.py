from typing import Tuple, List
from typing_extensions import Annotated
import random

class PaymentStrategy:
    def process_payment(self, amount: Annotated[float, "The amount to be processed"]) -> Tuple[Annotated[float,  str]]:
        raise NotImplementedError("This method should be overridden by subclasses")

class CreditCardPayment(PaymentStrategy):

    def __init__(self):
        self.total_amount = 0

    def process_payment(self, amount: Annotated[float, " The amount to be processed"] ) -> Tuple[Annotated[float, "The Processing Fee"], Annotated[str, "Status"]]:
        self.total_amount = amount + amount * (2 / 100.0)
        return (self.total_amount, "Added 2% Processing Fee")


class PayPalPayment(PaymentStrategy):

    def __init__(self):
        self.total_amount = 0

    def process_payment(self, amount: Annotated[float, " The amount to be processed"] ) -> Tuple[Annotated[float, "The Processing Fee"], Annotated[str, "Status"]]:
        self.total_amount = amount + amount * (3 / 100.0) + 0.3
        return (self.total_amount, "Added 3% processing fee plus a fixed fee of $0.30 per transaction")

class BankTransferPayment(PaymentStrategy):

    def __init__(self):
        self.total_amount = 0

    def process_payment(self,  amount: Annotated[float, " The amount to be processed"]) -> Tuple[Annotated[float, "The Processing Fee"], Annotated[str, "Status"]]:
        self.total_amount = amount
        return (self.total_amount, "No processing fee, but takes 3-5 business days to process.")

def item_price(name: str) -> float:
    if name.lower() == "cricket bat":
        return 3.33
    elif name.lower() == "shirt":
        return 1.99
    elif name.lower() == "laptop":
        return 699.99

class Item:

    id: int
    name: str
    price: float

    def __init__(self, name):
        self.id = random.randint(234,3243254)
        self.name = name
        self.price = item_price(name)


class Order:
    def __init__(self):
        self.items_list: List[Item] = []

    def add_item(self, name: str):

        self.items_list.append(Item(name))
    
    def calculate_price(self, payment_method: PaymentStrategy):
        total_price = sum(item.price for item in self.items_list)
        final_amount, status = payment_method.process_payment(total_price)
        self.final_amount(final_amount, status)

    def final_amount(self, total_price: float, status: str):
        print("==================")
        print(f"Total Amount: ${total_price:.2f}")
        print(f"Payment Status: {status}")
        print("==================")


app = Order()

app.add_item("laptop")
app.add_item("cricket bat")
app.add_item("shirt")

app.calculate_price(CreditCardPayment())
app.calculate_price(PayPalPayment())
app.calculate_price(BankTransferPayment())