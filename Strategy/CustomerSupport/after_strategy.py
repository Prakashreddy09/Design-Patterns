import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket:
    
    id : str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy
    
class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy

class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return []

class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self,customer,issue):
        self.tickets.append(SupportTicket(customer,issue))

    def process_tickets(self,processing_strategy: TicketOrderingStrategy = FIFOOrderingStrategy()):

        tickets_list = processing_strategy.create_ordering(self.tickets)


        if len(tickets_list) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        for ticket in tickets_list:
            self.process_ticket(ticket)
    
    def process_ticket(self, ticket: SupportTicket):
        print("====================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("====================================")

app = CustomerSupport()

app.create_ticket("Prakash Reddy", "My Laptop suddenly freezes.")
app.create_ticket("Pushpa harshitha", "My Laptop always gets stuck.")

app.process_tickets(BlackHoleOrderingStrategy())