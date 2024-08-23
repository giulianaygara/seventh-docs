from datetime import date

class Person():
    def __init__ (self, name, country, day, month, year):
        self.name = name
        self.country = country
        self.day = day
        self.month = month
        self.year = year
        
        
        
    def calculate_age(self):
        today = date.today ()
        age =  self.year - today.year
        if today < date (today.year, self.day):
            age -= 1
        return age
    
person = Person("Nicolas","Brasil", 2, 2, 1972)
    
    
print("Person")
print("Name:", person.name)
print("Country:", person.country)
print("Date of Birth:", person.day, person.month, person.year)
print("Age:", person.calculate_age())
               
