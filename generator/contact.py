import string
import random
import os.path
import jsonpickle
import argparse
from model.contact import Contact

parser = argparse.ArgumentParser(description="Generate test data for contacts")
parser.add_argument("-n", "--number", type=int, default=2, help="number of contacts")
parser.add_argument("-f", "--file", type=str, default="data/contacts.json", help="name of the file for data contacts")

args = parser.parse_args()
n = args.number
f = args.file

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    return "+79" + "".join([random.choice(string.digits) for i in range(maxlen)])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


testdata = [Contact(firstName=random_string("firstName", 10), lastName=random_string("lastName", 10),
                    nickname=random_string("nickname", 10), company=random_string("company", 10),
                    address=random_string("nickname", 20),
                    phone_home=random_numbers(9), phone_mobile=random_numbers(9), phone_work=random_numbers(9), fax=random_numbers(9),
                    email=random_email(10)+"@gmail.com", email2=random_email(10)+"@gmail.com", email3=random_email(10)+"@gmail.com",
                    webpage=random_string("web", 5) + ".com", title=random_string("nickname", 5),
                    bday=str(random.randint(1, 31)), bmonth=str(random.choice(months)), byear=str(random.randint(1900, 2025)),
                    an_day=str(random.randint(1, 31)), an_month=str(random.choice(months)), an_year=str(random.randint(1900, 2025)))
            for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))