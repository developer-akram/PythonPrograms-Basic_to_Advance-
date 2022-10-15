class ElectronicDevice:
    freeze = 1
    tv = 2
    def details(self):
        return f"{self.freeze} and {self.tv} contains in Electronic Devices"
class PocketGadget(ElectronicDevice):
    hand_watch = 3
    wallet = 4
    freeze = 5
    tv = 8
    # def details(self):
    #     return f"{self.hand_watch} and {self.wallet} contains in Pocket Gadgets"
class Phone(PocketGadget):
    contacts = 100
    call_log = 500
    hand_watch = 30
    wallet = 400
    freeze = 11
    tv = 22
    # def details(self):
    #     return f"Number of Contacts = {self.contacts}\nand\nNumber of " \
    #            f"Call logs are = {self.call_log}\nThese are stored in the Phone"

current = ElectronicDevice()
small_things = PocketGadget()
mobile = Phone()

print(small_things.details())
print(mobile.details())