import questionary
from colorama import Fore, init

# colorama initialise
init(autoreset=True)


# style for questionary select
select_style = questionary.Style(
    [
        ("qmark", "fg:#11a8cd bold"),
        ("question", "bold"),
        ("answer", "fg:#11a8cd bold"),
        ("pointer", "fg:#11a8cd bold"),
        ("highlighted", "fg:#11a8cd bold"),
        ("instruction", "fg:#555555"),
    ]
)
qmark_arrow = "❯"
qmark_style = questionary.Style([("qmark", "fg:#11a8cd bold")])


def q_input(message: str, is_passwd=False, qmark=qmark_arrow, style=qmark_style):
    if is_passwd:
        inp = questionary.password(message=message, qmark=qmark, style=style).ask()
    else:
        inp = questionary.text(message=message, qmark=qmark, style=style).ask()

    if inp != None:
        return str(inp.strip())

    print(f"\n{Fore.RED}[ERROR] Invalid Input.\n")
    return None


class ATM:
    def __init__(self, account_holder, pin, balance=0):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.pin:
            print(
                f"\n{Fore.GREEN}[SUCCESS] Current balance for {self.account_holder}: ₹{self.balance}"
            )
        else:
            print(f"\n{Fore.RED}[ERROR] Incorrect Pin.")

    def deposit(self, amount, entered_pin):
        if entered_pin == self.pin:
            if amount > 0:
                self.balance += amount
                print(
                    f"\n{Fore.GREEN}[SUCCESS] Deposited ₹{amount}. New balance: ₹{self.balance}"
                )
            else:
                print(f"\n{Fore.RED}[ERROR] Deposit amount cannot be negative.")
        else:
            print(f"\n{Fore.RED}[ERROR] Incorrect Pin")

    def withdraw(self, amount, entered_pin):
        if entered_pin == self.pin:
            if amount > self.balance:
                print(f"\n{Fore.RED}[ERROR] Insufficient balance.")
            elif amount <= 0:
                print(f"\n{Fore.RED}[ERROR] Withdrawal amount cannot be negative.")
            else:
                self.balance -= amount
                print(
                    f"\n{Fore.GREEN}[SUCCESS] Withdraw ₹{amount}. Remaining balance: ₹{self.balance}"
                )
        else:
            print(f"\n{Fore.RED}[ERROR] Incorrect Pin")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            if len(str(new_pin)) == 4:
                self.pin = new_pin
                print(f"\n{Fore.GREEN}[SUCCESS] Pin successfully changed.")
            else:
                print(f"\n{Fore.RED}[ERROR] New pin must be 4 digits.")
        else:
            print(f"\n{Fore.RED}[ERROR] Old Pin is incorrect.")


def get_details():
    print(f"\n\n{Fore.CYAN}--- Welcome to the ATM Setup ---\n\n")

    name = q_input(message="Enter your full name: ")
    pin = q_input(message="Set your 4-digit PIN: ", is_passwd=True)

    if pin == None or len(pin) < 4:
        print(f"\n{Fore.RED}[ERROR] Pin must be 4 digits.")
        return None

    balance = q_input(message="Enter initial balance: ")

    if name != None and balance != None:
        balance = float(balance)
        return name, pin, balance

    print(f"\n{Fore.RED}[ERROR] Invalid Input.")
    return None


def run_atm(atm_instance):
    while True:
        print(f"\n\n{Fore.CYAN}--- ATM System ---\n\n")
        choice = questionary.select(
            "What would you like to do?",
            choices=["Check Balance", "Deposit", "Withdraw", "Change PIN", "Exit"],
            qmark="- ",
            pointer=qmark_arrow,
            style=select_style,
        ).ask()

        if choice == "Exit":
            print(f"\n\n{Fore.YELLOW}Goodbye!")
            break

        pin_input = q_input(message="Enter your PIN:", is_passwd=True)

        if pin_input == None or len(pin_input) < 4:
            print(f"\n{Fore.RED}[ERROR] Invalid PIN.")
            continue

        if choice == "Check Balance":
            atm_instance.check_balance(pin_input)

        elif choice == "Deposit":
            amt = q_input(message="Enter amount to deposit: ")
            if amt != None:
                amt = float(amt)
                atm_instance.deposit(amt, pin_input)
            else:
                print(f"\n{Fore.RED}[ERROR] Invalid Amount.")
                continue

        elif choice == "Withdraw":
            amt = q_input(message="Enter amount to withdraw: ")
            if amt != None:
                amt = float(amt)
                atm_instance.withdraw(amt, pin_input)
            else:
                print(f"\n{Fore.RED}[ERROR] Invalid Amount.")
                continue

        elif choice == "Change PIN":
            new_pin = q_input(message="Enter new 4-digit PIN: ", is_passwd=True)
            if new_pin != None:
                atm_instance.change_pin(pin_input, new_pin)
            else:
                print(f"\n{Fore.RED}[ERROR] Invalid PIN.")
                continue


if __name__ == "__main__":
    data = get_details()
    if data:
        name, pin, balance = data
        my_atm = ATM(name, pin, balance)
        run_atm(my_atm)
    else:
        print(f"\n{Fore.RED}[ERROR] Something Went wrong, try again.")
        print(f"{Fore.YELLOW}Goodbye!")
