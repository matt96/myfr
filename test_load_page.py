# -*- coding: utf-8 -*-

# test_load_page.py
# tec-exitoacademico
# author: Adrian Garro

import unittest
from os import getcwd

from selenium import webdriver

class WEB_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Jake/AppData\Local/Programs/Python/Python37-32/lib/site-packages/selenium/webdriver/chrome" + '/chromedriver')

    def test_load_page(self):
        driver = self.driver
        driver.get("https://tec-exitoacademico.firebaseapp.com/")

        self.assertIn("Matrícula Talleres de Éxito Académico", driver.title)

        intro_p = driver.find_element_by_id("introP")
        self.assertEqual(intro_p.text, "Matrícula de Talleres del Proyecto Éxito Académico")

        complex_footer_p = driver.find_element_by_id("complexFooterP")
        self.assertEqual(complex_footer_p.text, "Copyright © Adrián Garro - Darío Monestel 2019")

    def tear_down(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
