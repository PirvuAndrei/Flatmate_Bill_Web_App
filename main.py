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
        self.days_in_house = days_in_house

    def pays(self, bill, flatemate2):
        weight = self.days_in_house / (self.days_in_house + flatemate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

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

print("John pays: ", john.pays(bill=the_bill, flatemate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatemate2=john))
