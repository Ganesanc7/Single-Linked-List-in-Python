class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insertfirst(self,data):
        node=Node(data,self.head)
        self.head=node
    def insertlast(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(data,None)
    def insert_at(self,index,data):
        if index==0:
            self.insertfirst(data)
            return
        count=0
        itr=self.head
        while(itr):
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def insertmultiple_values(self,list_values):
        for i in list_values:
            self.insertlast(i)
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr=self.head
        s=""
        while(itr):
            s+=str(itr.data)+"-->"
            itr=itr.next
        print(s)
    #Deletion part
    def removefirst(self):
        self.head=self.head.next
    def remove_at(self,index):
        if index==0:
            self.removefirst()
            return
        count=0
        itr=self.head
        while(itr):
            if count==index-1:
                 itr.next=itr.next.next
                 break
            itr=itr.next
            count+=1
ll=LinkedList()
ll.insertmultiple_values(list(map(int,input().split())))
ll.insert_at(3,10)
ll.insertfirst(0)
ll.print()
ll.removefirst()
ll.remove_at(3)
ll.print()