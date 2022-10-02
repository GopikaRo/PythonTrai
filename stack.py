stack=[]
def push():
    element=input("enter the elemnt:")
    stack.append(element)
    print(stack)
def pop():
    element=stack.pop()
    print("elemnt removd")
    print(stack)
while True:
    print("select operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
         print("enter the correct operation")
         
    
