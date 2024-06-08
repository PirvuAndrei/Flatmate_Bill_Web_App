class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.

    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat
    and plays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in.house = days_in_house

    def pays(self, bill):
        return bill.amount / 2

class PdfReport:
    """

     Creates a Pdf file that contains data about
     the flatmates such as their names, their due amounts
     and the period of the bill.

    """

    def __init(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatemate2, bill):
        pass


the_bill = Bill(amount = 120, period = "June 2024")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.pays(bill=the_bill))
