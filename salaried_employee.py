"""
Program: salaried_employee_class
Author: Ryan Blankenship
Last date modified: 11/09/2019

The purpose of this program is to create a
 derived class for a Salaried Employee while
 demonstrating inheritance.
"""
from datetime import datetime
from overriding_class_methods_assignment.employee_class import Employee


class SalariedEmployee(Employee):
    """Salaried Employee class"""

    # Constructor
    def __init__(self, fname, lname, addy, pnumber, start_date, salary):
        super().__init__(fname, lname, addy, pnumber)
        self._start_date = start_date
        self._salary = salary

    def give_raise(self, incr_salary):
        self._salary += incr_salary

    def display(self):
        return f"{Employee.display_employee(self)}Start Date: {self._start_date}\n" \
               f"Salary: ${self._salary:,.2f}"

    def __str__(self):
        return f"{Employee.display_employee(self)}Start Date: {self._start_date}\n" \
               f"Salary: ${self._salary:,.2f}"

    def __repr__(self):
        return f"{self._first_name} {self._last_name}\n{self._address}\n{self._phone_number}\n" \
               f"{self._start_date} ${self._salary}"


if __name__ == '__main__':
    first_day = datetime.now()
    sal_emp = SalariedEmployee('Ryan', 'Blankenship', 'Des Moines', 'No phone', first_day.strftime("%x"), 40000)
    print(sal_emp.display())
    sal_emp.give_raise(5000)
    print(sal_emp.display())
    del sal_emp
