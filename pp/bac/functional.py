
def functional_programming_warmup():
    return map(lambda x: x + 1, 
               filter(lambda x: x % 3 == 0, range(0, 9)))

print("Warmup exercise #1")
l = functional_programming_warmup()
print(list(l))
print()


def mystery2(fn, N):
    def g(x):
        for i in range(N):
            x = fn(x)
        return x
    return lambda y: g(y*2)


print("Warmup exercise #2")
f = mystery2(lambda x: x+1, 10)
print(f(10))
print()


def gen_fn(c):
    def fn(x):
        return x % c == 0
    return fn

print("Warmup exercise #3")
print(list(filter(gen_fn(10), map(lambda x: x * 2, [10, 25, -10, 18, -9]))))
print(list(map(lambda x: x * 2, filter(gen_fn(5), [10, 25, -10, 100, -9]))))
print()

