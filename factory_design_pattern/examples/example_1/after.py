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


# Factory Class
class PaymentFactory:
    @staticmethod
    def create_payment_method(choice):
        if choice == '1':
            card_number = "1234-5678-9012-3456"
            card_holder = "John Doe"
            return CreditCardPayment(card_number, card_holder)
        elif choice == '2':
            email = "dummy@example.com"
            return PayPalPayment(email)
        else:
            print("Invalid choice")
            exit()

if __name__ == "__main__":
    print("Select Payment Method:")
    print("1. Credit Card")
    print("2. PayPal")

    choice = input("Enter choice (1 or 2): ")
    payment_method = PaymentFactory.create_payment_method(choice)

    amount = 100.0
    payment_method.pay(amount)
