#testing git commit
import math

def main():
    print("hello world")
    #name=input("what's your name?")
    name="sathish"
    #print("Welcome", name)
    

if __name__ == "__main__":
    main()   

def funct():
    print("inside function")
    #return "print return value"

funct() 

def loop(arg1, *args):
    result = 0
    for i in args:
        result = result + arg1 + i
    return result

#print(loop(5,1,2,3))

def cond():
    x, y = 1100, 200
    print("x is greater than y") if x > y else print("x is smaller than or equal to y")

#cond()

def loop():
    i = 100
    for i in range(1,10):
        if i % 3 == 0:
            break
        #if i == 105:
        #    break
        print(i)

#loop()

def enum():
    months = ["Jan","Feb", "Mar", "Apr", "May", "Jun" ]
    for i,d in enumerate(months):
        print(i,d)
#enum()


for i in range(6, 16):
    print(i)

var="abcdefghi"
print(var[0:9:5])