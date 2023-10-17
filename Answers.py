class Converter:
    def __init__(self, voltage):
        self.voltage = voltage
    def ToDigital(self):
        dif = 5/1024
        digital = bin(int((self.voltage/dif)-1))
        return digital[2:]
    
    def SetAnalogValue(self, digital):
        dif = 5/1024
        voltage = (int(digital)+1) * dif
        self.voltage  = voltage
        print(f'Voltage updated to {self.voltage} volt')

cur_Voltage = float(input("Enter the current voltage "))
con  = Converter(cur_Voltage)
print("The current digital number is ",con.ToDigital())
digital = int(input("Enter current digital number in binary base "), base=2)
con.SetAnalogValue(digital)


