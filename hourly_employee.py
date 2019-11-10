"""
Program: salaried_employee_class
Author: Ryan Blankenship
Last date modified: 11/09/2019

The purpose of this program is to create a
 derived class for a Hourly Employee while
 demonstrating inheritance.
"""
from datetime import datetime
from overriding_class_methods_assignment.employee_class import Employee


class HourlyEmployee(Employee):
    """Salaried Employee class"""

    # Constructor
    def __init__(self, fname, lname, addy, pnumber, start_date, hourly_pay):
        super().__init__(fname, lname, addy, pnumber)
        self._start_date = start_date
        self._hourly_pay = hourly_pay

    def give_raise(self, incr_salary):
        self._hourly_pay += incr_salary

    def display(self):
        return f"{Employee.display_employee(self)}Start Date: {self._start_date}\n" \
               f"Salary: ${self._hourly_pay:,.2f}"

    def __str__(self):
        return f"{Employee.display_employee(self)}Start Date: {self._start_date}\n" \
               f"Salary: ${self._hourly_pay:,.2f}"

    def __repr__(self):
        return f"{self._first_name} {self._last_name}\n{self._address}\n{self._phone_number}\n" \
               f"{self._start_date} ${self._hourly_pay}"


if __name__ == '__main__':
    first_day = datetime.now()
    hrly_emp = HourlyEmployee('Ryan', 'Blankenship', 'Des Moines', 'No phone', first_day.strftime("%x"), 10.00)
    print(hrly_emp.display())
    hrly_emp.give_raise(2.00)
    print(hrly_emp.display())
    del hrly_emp
