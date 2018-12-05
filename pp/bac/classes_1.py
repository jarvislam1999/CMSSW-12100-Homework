class Mystery:
    def __init__(self, v0, v1):
        self._v0 = v0
        self._v1 = v1

    def get_a(self):
        return self._v0+1

    def get_b(self):
        return self._v1*2

    def get_c(self):
        return self.get_a() + self.get_b()

    def do_d(self, val):
        self._v0, self._v1 = val

    def __str__(self):
        return str((self.get_a(), self.get_b(), self.get_c()))


m0 = Mystery(1, 2)
m0.do_d((m0.get_a(), m0.get_c()))
print(m0)

m1 = Mystery(3, 4)
m1.do_d((m0.get_a(), m1.get_b()))
print(m1)


