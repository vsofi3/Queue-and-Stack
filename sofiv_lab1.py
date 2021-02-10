'''
Sofi Vinas
CIS 313 Lab 1
Last Modified: 1/24/21
MealTicket project with Singly-Linked List Implementation of
Queue and Stack data structures
'''

#singly-linked list implementation of queue and stack data structures
from mealticket import *

class Node():
    def __init__(self, ticket):
        self.ticketID = ticket
        self.next = None

#for invalid capacity input
defaultCapacity = 20

class Queue():

    #constructor of the Queue class
    def __init__(self, capacity) -> None:
        if(capacity <= 0):
            self.maxSize = defaultCapacity
        else:
            self.maxSize = capacity
        self.head = self.tail = None
        self.currentSize = 0


    def checkType(self, ticket) ->bool:
        #checks to see if ticket is of type MealTicket
        statement = (type(ticket) is MealTicket)
        return statement

    def isEmpty(self) -> bool:
        #returns True if queue is empty
        #returns False if queue is NOT empty
        return self.currentSize == 0


    def enqueue(self, ticket) -> bool:
        #takes object of type: MealTicket
        #return False on invalid input
        #add a new ticket at the tail of the queue

        if self.isFull(): #check to see if the queue is full first
            return False

        if self.tail == None:
            if(self.checkType(ticket)):
                #CHECK FOR VALID INPUT
                ticket = Node(ticket)
                self.head = self.tail = ticket #tail is new ticket Node
                self.currentSize += 1
                return True
            else:
                #ticket was NOT added to the queue
                return False

        if(self.checkType(ticket)):
            #CHECK FOR VALID INPUT
            ticket = Node(ticket)
            self.tail.next = ticket
            self.tail = ticket
            self.currentSize += 1
            return True
        else:
            return False


    def dequeue(self):
        #remove ticket at front of the queue and return it or False
        #if the queue is empty
        #GET RID OF ALLLLL REFERENCES TO THIS NODE
        """
        [1] -> [2] -> [3] -> [4] -> None
        temp   head          tail
        1 is an orphan, gets garbaged collected
        FULLY DEREFERENCE head node before considering deleted
        """
        if self.isEmpty():
            return False
        else:
            temporary = self.head
            self.head = temporary.next
            self.currentSize -= 1

        return temporary.ticketID



    def front(self):
        #lets user peak at the front of the queue without deleting it
        #returns either a meal ticket or false is the queue is empty
        status = self.currentSize > 0
        if status:
            return self.head.ticketID
        else:
            return False


    def isFull(self) -> bool:
        #return True if the currentSize is GREATER than max capacity
        #return False if currentSize is NOT at max capacity
        return self.currentSize == self.maxSize


class Stack():

    #constructor of the Stack class
    def __init__(self, capacity) -> None:
        if (capacity <= 0):
            self.maxSize = 20
        else:
            self.maxSize = capacity
        self.head = None
        self.currentSize = 0

    def checkType(self, ticket) ->bool:
        #checks to see if ticket is of type MealTicket
        statement = (type(ticket) is MealTicket)
        return statement

    def push(self, ticket) -> bool:
        #push an object of type MealTicket
        #add MealTicket to head of the stack

        if self.isFull():
            return False

        if(self.checkType(ticket)):
            if self.head == None:
                ticket = Node(ticket)
                self.head = ticket
                self.currentSize += 1
                return True
            else:
                new = Node(ticket)
                new.next = self.head
                self.head = new
                self.currentSize += 1
                return True
        else:
            return False


    def pop(self):
        #remove the ticket at the top of the stack or False is the stack is empty
        #pop a ticket from the HEAD of the stack

         #stack is EMPTY, return false
        if self.isEmpty():
            return False
        else: #stack is NOT empty- proceed with pop
            poppedNode = self.head.ticketID
            self.head = self.head.next
            self.currentSize -= 1 #update current size variable
            return poppedNode



    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.head.ticketID



    def isEmpty(self) -> bool:
        return self.currentSize == 0


    def isFull(self) -> bool:
        #return True if the currentSize is GREATER than maxSize
        #return False if the currentSize is SMALLER than maxSize
        return self.currentSize == self.maxSize



