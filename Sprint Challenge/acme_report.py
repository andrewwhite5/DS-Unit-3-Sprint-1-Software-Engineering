#!/usr/bin/env python
import random
import numpy as np
from acme import Product

# Generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    while len(products) < num_products:
        products.append(
            f'{random.sample(ADJECTIVES,1)[0]} {random.sample(NOUNS,1)[0]}')
    return products

# Generate clean-looking report
def inventory_report(products):
    name_list = []
    price_list = []
    weight_list = []
    flam_list = []
    for product in products:
        name = product
        price = random.randint(5,100)
        weight = random.randint(5,100)
        flammability = random.uniform(0,2.5)
        name_list.append(name)
        price_list.append(price)
        weight_list.append(weight)
        flam_list.append(flammability)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(np.unique(name_list))}')
    print(f'Average price: {np.mean(price_list)}')
    print(f'Average weight: {np.mean(weight_list)}')
    print(f'Average flammability: {np.mean(flam_list)}')

if __name__ == '__main__':
    inventory_report(generate_products())
