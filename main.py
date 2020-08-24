

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def email(self) -> str:
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name: str):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount: float):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname} - {self.email}"

    def __add__(self, other) -> int:
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_lang: str):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return f"Developer('{self.first}', '{self.last}', {self.pay})"


class Manager(Employee):
    def __init__(self, first: str, last: str, pay: int, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp: Employee):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)

    def __repr__(self):
        return f"Manager('{self.first}', '{self.last}', {self.pay})"


dev_1 = Developer('Ali', 'Schilling', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1)
print(repr(mgr_1))
print(str(mgr_1))

print(dev_1)
print(repr(dev_1))
print(str(dev_1))

print(len(dev_1))
print('test'.__len__())

print(mgr_1 + dev_1)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

print(issubclass(Manager, Developer))


dev_1.fullname = 'Ali Rollins'

print(dev_1.first)
print(dev_1.email)
print(dev_1.fullname)

del dev_1.fullname


# print(dev_1.email)
# print(dev_1.prog_lang)
#
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
