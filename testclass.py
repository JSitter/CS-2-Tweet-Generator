class mytest:
    def __init__(self, tint):
        self.raninger = self.superCall(tint)
    
    def superCall(self, linteger):
        return linteger + 10000

    def plow(self):
        return self.raninger

if __name__=="__main__":
    tyrant = mytest(34)
    print(tyrant.plow())