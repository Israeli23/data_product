class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def get_sum(self):
        return self.a + self.b

    def get_multiple(self):
        return self.a * self.b 

    def get_difference(self):
        return self.a - self.b 

    def get_quotient(self):
        if self.b == 0:
            raise ValueError("Cannot divide by 0")
        return self.a / self.b 
    

if __name__ == '__main__':
    calc = calculator(10, 5)
    print(calc.get_quotient())


    




