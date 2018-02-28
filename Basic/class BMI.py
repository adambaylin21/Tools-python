class BMI:
    count = 0
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        BMI.count +=1
    def tinh(self):
        print ('So BMI la',(self.weight/(self.height*self.height)))
    def htx(self):
        print('show',BMI.count)

    @staticmethod
    def hts():
        print('show2',BMI.count)
Hai = BMI('Hai',21,56,1.7)
print (Hai.tinh())
BMI.hts()