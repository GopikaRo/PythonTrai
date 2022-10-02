queue=[]
def enqueue():
    element=input("enter the element:")
    queue.append(element)
    print("element is added")
    print(queue)
def dequeue():
    element=queue.pop(0)
    print("removed elemnt:",element)
    print(queue)
while True:
    print("select operation 1.add 2.remove 3.quit")
    choice=int(input())
    if choice==1:
       enqueue()
    elif choice==2:
       dequeue()
    elif choice==3:
       break
    else:
        print("enter the correct operation")
        
