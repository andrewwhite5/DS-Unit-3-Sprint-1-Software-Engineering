#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    '''Making sure Acme products are the tops!'''
    def test_default_product_price(self):
        '''Test default product price being 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_generate_products(self):
        '''Test to make sure 30 products are generated.'''
        list = generate_products()
        self.assertEqual(len(list), 30)

    def test_default_product_flammability(self):
        '''Test default product flammability being 0.5.'''
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


if __name__ == '__main__':
    unittest.main()
