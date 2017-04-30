import random
import string
from models.group import Group


def random_string(maxlen):
    length = random.randrange(maxlen)
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return ''.join([random.choice(symbols) for _ in range(length)])


names = ['', 'hgvjhsdfcs', "123"]
headers = ['', 'hgvjhsdfcs', "123"]
footers = ['', 'hgvjhsdfcs', "123"]

test_groups = [
    Group(name=name, header=header, footer=footer)
    for name in names
    for header in headers
    for footer in footers
] + [
    Group(name=random_string(14), header=random_string(20), footer=random_string(50))
    for _ in range(5)
]
