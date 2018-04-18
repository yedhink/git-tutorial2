def add(num1, num2):
    return num1+num2
def add3(num1, num2,num3):
    return num1+num2+num3
def add4(num1, num2,num3,num4):
    return num1+num2+num3+num4

while True:
    print "add\n1) 2 numbers\n2) 3 numbers\n3) 4 numbers\n"
    choice = raw_input("Enter choice = ")
    if choice == '1':
        a = int(raw_input("Enter 1st = "))
        b = int(raw_input("Enter 2nd = "))
        print "sum = ",add(a,b),"\n"
    elif choice == '2':
        a = int(raw_input("Enter 1st = "))
        b = int(raw_input("Enter 2nd = "))
        c = int(raw_input("Enter 3rd = "))
        print "sum = ",add3(a,b,c),"\n"
    else:
        a = int(raw_input("Enter 1st = "))
        b = int(raw_input("Enter 2nd = "))
        c = int(raw_input("Enter 3rd = "))
        d = int(raw_input("Enter 4th = "))
        print "sum = ",add4(a,b,c,d),"\n"
