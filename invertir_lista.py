from lista_enlazada import lista_enlazada_simple
from lista_enlazada import Node

from typing import Optional
import re

def main():
    entrada = input("Introduce los números de la lista: ")
    nums = [int(x) for x in re.findall(r"\d+", entrada)]
    lista = lista_enlazada_simple()

    previo = None

    for i in range(len(nums)):
        if nums[i] <-5000 or nums[i] > 5000:
            print(f"El número {nums[i]} es inválido, debe ser de entre -5000 a 5000")
            return
            
        if i == 0:
           head : Node = Node(nums[0], None)
           lista.head = head
           previo = lista.head
        else:
            next : Node = Node(nums[i], None)
            if previo is not None:
                previo.next = next
            previo = next


    # Imprimimos los elementos (antes de la inversión)
    print("\n**** ANTES DE LA INVERSIÓN ****\n")

    actual : Optional[Node] = lista.head
    i : int = 0

    while actual is not None:
        print(f"Valor {i} siguiente: {actual.val}")
        i += 1
        actual = actual.next

    # Inversión de los elementos...
    previo =  None
    actual = lista.head

    while actual is not None:
        actual_copia = actual.next
        actual.next = previo
        previo = actual
        actual = actual_copia

    lista.head = previo
        
    # Imprimimos los elementos (después de la inversión)
    print("\n**** DESPUÉS DE LA INVERSIÓN ****\n")


    actual = lista.head
    i = 0

    while actual is not None:
        print(f"Valor {i} siguiente: {actual.val}")
        i += 1
        actual = actual.next
    
if __name__ == "__main__":
    main()