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

con  = Converter(3)
print(con.ToDigital())
print(con.SetAnalogValue(0b1111111110))

