# complex numbers class
# getting used to one-constructor concept
# learning inheritance syntax


class Complex:

    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def printComplex(self):
        print(self.real, "+", self.img, "i")

    def add(self, right):
        result = Complex()
        result.real = self.real + right.real
        result.img = self.img + right.img
        return result

    def getConjugate(self):
        return (Complex(self.real, -self.img))


class PositiveComplex(Complex):
    def __init__(self, real, img):
        if real > 0 and img > 0:
            Complex.__init__(self, real, img)
        elif real < 0 or img < 0:
            print(
                "Negative values are forbidden, positive values are assigned to real and img")
            Complex.__init__(self, abs(real), abs(img))
        else:
            print("Zero is forbidden, 1 is assigned to real and img")
            Complex.__init__(self, 1, 1)


c1 = Complex(1, 2)
c2 = Complex(3, 5)
c3 = c1.add(c2)
c3.printComplex()
c3 = c3.getConjugate()
c3.printComplex()
print(c3.img)
pc1 = PositiveComplex(-5, 3)
pc1.printComplex()
pc1 = PositiveComplex(0, 0)
pc1.printComplex()
