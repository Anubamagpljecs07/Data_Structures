class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
class functions:
    def InsAtBeg(self,d):
        temp=node(d)
        temp.next=g.head
        g.head=temp
    def InsAtEnd(self,d):
        temp=node(d)
        trav=g.head
        if(g.head==None):
            InsAtBeg(self,d)
        else:
            while(trav.next!=None):
                trav=trav.next
            trav.next=temp
    def InsAtPos(self,d,pos):
        temp=node(d)
        if pos==1:
            InsAtBeg(self,d)
        else:
            c=2
            trav=g.head
            while(c!=pos):
                trav=trav.next
                c+=1
            temp.next=trav.next
            trav.next=temp
    def DelAtBeg(self):
        temp=g.head
        g.head=temp.next
        del temp
    def DelAtEnd(self):
        trav=g.head
        while(trav.next.next!=None):
            trav=trav.next
        temp=trav.next
        trav.next=None
        del temp
    def DelAtPos(self,pos):
        trav=g.head
        if pos==1:
            DelAtBeg(self)
        else:
            c=2
            while(c!=pos):
                trav=trav.next
                c+=1
            temp=trav.next
            trav.next=temp.next
            del temp
    def search(self,pos):
        if pos==1:
            print(g.head.data)
        else:
            c=2
            trav=g.head
            while(c!=pos):
                trav=trav.next
            print(trav.data)
        
    def Print(self):
        trav=g.head
        while(trav!=None):
            print(trav.data,end=" ")
            trav=trav.next
print("Enter your choice")
ch=int(input())
g=single()
f=functions()
while (ch!=9):
    print("Linked List Implementation \n 1.Insertion at beginning \n 2.Insertion at end\n 3.Insertion at pos\n 4.Deletion at beginning\n 5.Deletion at end\n 6.Deletion at pod \n 7.Display\n 8.search\n 9.Exit")
    if ch==1:
        d=int(input("Enter the node value"))
        f.InsAtBeg(d)
    elif ch==2:
        d=int(input("Enter the node value"))
        f.InsAtEnd(d)
    elif ch==3:
        d=int(input("Enter the node value"))
        p=int(input("Enter the node position"))
        f.InsAtPos(d,p)
    elif ch==4:
        f.DelAtBeg()
    elif ch==5:
        f.DelAtEnd()
    elif ch==6:
        p=int(input("Enter the node position"))
        f.DelAtPos(p)
    elif ch==7:
        f.Print()
    elif ch==8:
        pos=int(input("Enter the position "))
        f.search(pos)
    ch=int(input())
        
