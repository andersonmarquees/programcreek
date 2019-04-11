"""Add Two Numbers"""

# class Solution:
#
#     def addTwoNumbers(self, l1, l2):
#         aux = 0
#         l3 = []
#         for i in range(len(l1)):
#             if (l1[i] + l2[i]) >= 10:
#                 l3.append((l1[i] + l2[i]) % 10)
#                 aux += (l1[i] + l2[i]) // 10
#             else:
#                 l3.append(l1[i] + l2[i] + aux)
#                 aux = 0
#         return l3
#
#
# x = [2, 4, 3]
# y = [5, 6, 4]
# a = Solution()
# print(a.addTwoNumbers(x, y))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista possui elementos
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)  # primeira inserção
        self._size = self._size + 1

    def __len__(self):
        """retorna o tamanho da lista"""
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError("List index out of range")

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range")

    def index(self, elem):
        """Retorna o indice do elemento da lista"""
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("{} is not in list.".format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1


if __name__ == '__main__':

    lista = LinkedList()
    lista.append(7)
    lista.append(80)
    lista.append(56)
    lista.append(32)
    lista.append(17)
    lista.insert(0, 22)
    print(lista[1])
    print(lista[0])
    lista.insert(3, 888)
    print(lista[3])
    print(len(lista))
    lista.insert(len(lista), 50)
    print(len(lista))
    print(lista[len(lista) - 1])
