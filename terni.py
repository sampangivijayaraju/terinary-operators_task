x=10
def show():
    x=5
    print(x)
show()
print(x)

o/p:
5
10

def outer ():
    x=10
    def inner():
        print(x)
    inner()
outer()

o/p:
10

x="global"
def outer():
    x="outer"
    def inner():
        x= "inner"
    inner()
    print("outer:",x)
outer()

print("global:",x)

o/p:
outer:outer
global:global
