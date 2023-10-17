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
        voltage = (int(digital)) * dif
        self.voltage  = voltage
        print(f'Voltage updated to {self.voltage} volt')

cur_Voltage = float(input("Enter the current voltage "))
Max_Voltage = float(input("Enter the max voltage "))
bits = float(input("Enter the number of bits "))
con  = Converter(cur_Voltage,Max_Voltage,bits)
print("The current digital number is ",con.ToDigital())
digital = int(input("Enter current digital number in binary base "), base=2)
con.SetAnalogValue(digital)

