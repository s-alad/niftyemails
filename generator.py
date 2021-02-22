import random
import names
from random_username.generate import generate_username

hi = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "aol.com",
    "msn.com",
    "outlook.com",
    "mail.com",
]

me = [
    "facebook.com",
    "mac.com",
    "hotmail.co.uk",
    "hotmail.fr",
    "orange.fr",
    "yahoo.co.uk",
    "yahoo.com.br",
]

lo = [
    "googlemail.com",
    "yahoo.co.in",
    "live.com",
    "yandex.ru",
    "verizon.net",
    "yahoo.es",
    "protonmail.com",
]

class Email:
    username = ""
    domain = ""

    def __init__(self):
        self.username = self.random_username()
        self.domain = self.random_domain()

    def display(self):
        return ""+self.username+"@"+self.domain

    def random_username(self):
        sex = random.choices(['male', 'female'], weights=[.45, .55])[0]
        return names.get_last_name() if random.randint(0, 1) == 0 else names.get_first_name(sex)

    def random_domain(self):
        preliminary_selection = random.choices([hi, me, lo], weights=[.8, .15, .05])[0]
        selection = random.choices(preliminary_selection, weights=[.4, .2, .15, .075, .075, .05, .05, ])[0]
        return selection

def main():
    email = Email()
    print(email.display())
if __name__ == "__main__":
    main()


