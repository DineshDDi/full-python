#example for constructor
class CTS():
    def __init__(self, Name, Age, Employee_Id, Phone_Number, Department):
        self.Name = Name
        self.Age = Age
        self.Employee_Id = Employee_Id
        self.Phone_Number = Phone_Number
        self.Department = Department

Divi = CTS('Divi', 22, 'CTS4456', 9176528966, 'Banking')
Dini = CTS('Dini', 21, 'CTS4457', 8072288759, 'I.T')
Ram = CTS('Ram', 21, 'CTS4444', 6323444565, 'Insurance')

print(Divi.__dict__)
print(Dini.__dict__)
print(Ram.__dict__)





