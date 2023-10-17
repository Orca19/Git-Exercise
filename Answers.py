class Converter:
    def __init__(self, voltage, maxV, bits):
        self.voltage = voltage
        self.Max_Voltage = maxV
        self.bits = bits
    def Difference(self):
        dif = self.Max_Voltage/((2**self.bits)-1)
        return dif
    
    def ToDigital(self):
        dif = self.Difference()
        digital = bin(int((self.voltage/dif)))
        return digital[2:]
    
    def SetAnalogValue(self, digital):
        dif = self.Difference()
        voltage = (int(digital)+1) * dif
        self.voltage  = voltage
        print(f'Voltage updated to {self.voltage} volt')

con  = Converter(5,5,10)
print(con.ToDigital())
print(con.SetAnalogValue(0b1111111110))

