
ANUBAMA GOPAL <anucud1998@gmail.com>
23:33 (0 minutes ago)
to THARANIRAMESH28

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
class functions:
    def Enqueue(self,d):
        temp=node(d)
        trav=g.head
        if g.head==None:
            g.head=temp
        else:
            while(trav.next!=None):
                trav=trav.next
            trav.next=temp
    def Dequeue(self):
        temp=g.head
        g.head=temp.next
        del temp
    def Print(self):
        trav=g.head
        while(trav!=None):
            print(trav.data,end=" ")
            trav=trav.next
print("Enter your choice")
ch=int(input())
g=single()
f=functions()
while(ch!=4):
    print("1.Enqueue\n 2.Dequeu\n 3.Display\n 4.Exit")
    if ch==1:
        d=int(input("Enter the node to be queued"))
        f.Enqueue(d)
    elif ch==2:
        f.Dequeue()
    elif ch==3:
        f.Print()
    ch=int(input())
