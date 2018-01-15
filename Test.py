class Bankacc:
    rate = 0.0
    @staticmethod
    def setrate(newrate):
        Bankacc.rate = newrate

acb = Bankacc()
Bankacc.setrate(0.1)

print (acb.rate)

