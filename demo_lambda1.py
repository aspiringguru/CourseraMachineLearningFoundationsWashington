def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print "f(0)=", f(0)
print "f(1)", f(1)

print "--------------"
def multSquared(n):
    return lambda x: x * n
g = multSquared(2)
print "g(1)", g(1)
print "g(2)", g(2)
print "g(5)", g(5)
