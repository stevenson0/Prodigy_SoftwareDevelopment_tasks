class temp():
    def __init__(self):
        print("1.Celsius\n2.Fahrenheit\n3.Kelvin")
        user=input("Select the Temperature scale('1','2','3'): ")
        if user=="1":
            self.cel()
        elif user=="2":
            self.far()
        elif user=="3":
            self.kel()
        
    def cel(self):
        value=float(input("Enter the Celsius value: "))
        a=round(value*(9/5)+32,2)
        b=round(value+273.15,2)
        print("Faherenheit value:",a)
        print("Kelvin value:",b)
        self.call()

    def far(self):
        value=float(input("Enter the Fahrenheit value: "))
        a=round((value-32)*5/9,2)
        b=round((value-32)*5/9+273.15,2)
        print("Celsius value:",a)
        print("Kelvin value:",b)
        self.call()

    def kel(self):
        value=float(input("Enter the Kelvin value: "))
        a=round(value-273.15,2)
        b=round((value-273.15)*9/5+32,2)
        print("Celsius value:",a)
        print("Faherenheit value:",b)
        self.call()

    def call(self):
        s=input("Do you want to continue(Y/N): ")
        if s=="Y":
            self.__init__()
        elif s=="N":
            print("Thank You")
        
t1=temp()
