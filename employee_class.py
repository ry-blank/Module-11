"""
Program: employee_class
Author: Ryan Blankenship
Last date modified: 11/09/2019

The purpose of this program is to create a
 base class for an Employee while demonstrating
 inheritance.
"""


class Employee:
    """Employee Class """

    # Constructor
    def __init__(self, fname, lname, addy, pnumber):
        self._first_name = fname
        self._last_name = lname
        self._address = addy
        self._phone_number = pnumber

    def set_first_name(self, fname):
        self._first_name = fname

    def set_last_name(self, lname):
        self._last_name = lname

    def set_address(self, addy):
        self._address = addy

    def set_phone_number(self, pnumber):
        self._phone_number = pnumber

    def display_employee(self):
        return f'Employee Name: {self._last_name}, {self._first_name}\nAddress: {self._address}\n' \
               f'Phone Number: {self._phone_number}\n'

    def __str__(self):
        return f'Employee Name: {self._last_name}, {self._first_name}\nAddress: {self._address}\n' \
               f'Phone Number: {self._phone_number}\n'

    def __repr__(self):
        return f"{self._first_name} {self._last_name}\n{self._address}\n{self._phone_number}\n"
