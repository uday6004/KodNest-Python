from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self):
        pass


class UPIPayment(PaymentProcessor):

    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"UPI Payment: {self.amount}")


class CardPayment(PaymentProcessor):

    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Card Payment: {self.amount}")


class NetBankingPayment(PaymentProcessor):

    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Net Banking Payment: {self.amount}")


# Reading inputs
upi_amount = int(input())
card_amount = int(input())
net_amount = int(input())

# Creating objects
upi = UPIPayment(upi_amount)
card = CardPayment(card_amount)
net = NetBankingPayment(net_amount)

# Storing all objects in a list
payments = [upi, card, net]

# Processing using one loop
for payment in payments:
    payment.process_payment()