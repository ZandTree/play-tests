import json
from pathlib import Path
from typing import Iterator


class GenericCustomer:
    id: int
    first_name: str
    last_name: str
    email: str
    make: str
    model: str
    year: int
    vin: str
    price: int

    def __init__(self, _id: int, first_name, last_name, email, make, model, year, vin, price):
        # print(f"Creating customer {_id}: {first_name} {last_name}")
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price


def get_raw_data():
    file_temp = Path(__file__).parent  # C:\Users\tanja\PycharmProjects\monkey\start
    file = Path(__file__).parent / 'MOCK_DATA.json'
    with file.open('r') as fh:
        raw_data = json.load(fh)  # list
    return raw_data


def load_list():
    raw_data = get_raw_data()
    all_customers = [GenericCustomer(**obj) for obj in raw_data]
    print(type(all_customers))
    return all_customers


def main():
    sales = load_list()
    count = 20
    for idx, s in enumerate(sales, start=1):
        print(f'{idx}. {s.first_name} {s.last_name} bought {s.make} {s.model} for ${s.price:,}.')
        if idx < count:
            break



if __name__ == '__main__':
    main()

# def load_list_retro(file_):
#     try:
#         # open json file
#         with open(file_) as fh:
#             read_data = fh.read()  # type == string
#             data = json.loads(read_data)  # type = list
#             return data
#     except Exception as e:
#         print('exception:', e)
