from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        print(f"Paying {amount} using Credit Card: {self.card_number} - {self.card_holder}")

# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paying {amount} using PayPal: {self.email}")



if __name__ == "__main__":
    print("Select Payment Method:")
    print("1. Credit Card")
    print("2. PayPal")

    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        card_number = "1234-5678-9012-3456"
        card_holder = "John Doe"
        payment_method = CreditCardPayment(card_number, card_holder)
    elif choice == '2':
        email = "dummy@example.com"
        payment_method = PayPalPayment(email)
    else:
        print("Invalid choice")
        exit()

    amount = 100.0
    payment_method.pay(amount)

    