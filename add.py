def add(num1, num2):
    return num1+num2
def add3(num1, num2,num3):
    return num1+num2+num3

print "add\n1) 2 numbers\n2) 3 numbers\n"
choice = raw_input("Enter choice = ")
if choice == '1':
    a = int(raw_input("Enter 1st = "))
    b = int(raw_input("Enter 2nd = "))
    print "sum = ",add(a,b)
else:
    a = int(raw_input("Enter 1st = "))
    b = int(raw_input("Enter 2nd = "))
    c = int(raw_input("Enter 3rd = "))
    print "sum = ",add(a,b,c)
