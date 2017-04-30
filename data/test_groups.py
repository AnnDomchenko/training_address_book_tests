from models.group import Group

names = ['', 'hgvjhsdfcs', "123"]
headers = ['', 'hgvjhsdfcs', "123"]
footers = ['', 'hgvjhsdfcs', "123"]

test_groups = [
    Group(name=name, header=header, footer=footer)
    for name in names
    for header in headers
    for footer in footers
]
