from typing import Optional

class Node:
    def __init__(self, val: int = 0, next  = None):
        self.val = val
        self.next = next

class lista_enlazada_simple:
    def __init__(self, head : Optional[Node] = None):
        self.head = head
