x=10
def show():
    x=5
    print(x)
show()
print(x)

def outer ():
    x=10
    def inner():
        print(x)
    inner()
outer()

x="global"
def outer():
    x="outer"
    def inner():
        x= "inner"
    inner()
    print("outer:",x)
outer()
print("global:",x)