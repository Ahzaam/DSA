# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        return self._head.next is None

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        # Creating the node
        new_node = SLNode(value)

        # making the new node as head and previous head as next
        new_node.next = self._head.next
        self._head.next = new_node

    def insert_back(self, value: object) -> None:

        # Creating the node
        new_node = SLNode(value)
        # checking if the queue has value
        if self._head is None:
            self._head = new_node
            return

        # looping through all the list and finding the tail of the list
        last_node = self._head
        while last_node.next:

            last_node = last_node.next
        # inserting the value to last node
        last_node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:

        # Creating the node
        new_node = SLNode(value)
        size = self.length()

        # check if the position is > 0
        if index < 0:
            raise SLLException()
        # if inserting to head
        elif index == 0:
            new_node.next = self._head.next
            self._head.next = new_node

        else:
            loc = 1
            current = self._head.next
            prev = self._head
            temp = self._head.next
            # looping to find the inserting position
            while current is not None:
                # if inserting to back of the list
                if current.next is None and size == index:
                    current.next = new_node
                    new_node.next = None
                    return
                # if inserting index was larger than the list
                elif size < index:
                    raise SLLException
                # if the location and index matches inserting the node
                elif loc == index + 1:
                    temp = prev.next
                    prev.next = new_node
                    new_node.next = temp
                    return

                prev = current
                current = current.next
                # tracking the location in the list
                loc += 1

    def remove_at_index(self, index: int) -> None:
        # if the list has nothing raises an exception
        if self._head is None:
            return
        # if the removing element wad the head
        if index == 0:
            self._head = self._head.next
            return
        # for the negative index
        if index < 0:
            raise SLLException()

        # for outbounds index
        if index >= self.length():
            raise SLLException()
        loc = 0
        current = self._head
        prev = self._head
        temp = self._head
        # getting the position to remove the index
        while current is not None:
            if loc == index + 1:
                # connecting the previous and the next node of the removing element
                temp = current.next
                break
            prev = current
            current = current.next
            loc += 1
        prev.next = temp

    def remove(self, value: object) -> bool:
        # if the list has nothing raises an exception
        if self._head is None:
            raise SLLException

        loc = 0
        current = self._head
        prev = self._head
        temp = self._head
        remove = False
        # getting the position to remove the value
        while current is not None:
            # checking the value if it matches the removing value
            if current.value == value:

                # removing the value
                temp = current.next
                prev.next = temp
                # return
                return True

            prev = current
            current = current.next
            loc += 1
        # if the loop runs until the end, it didn't remove anything,then its returns False
        return False

    def count(self, value: object) -> int:
        # if the list has nothing raises an exception
        if self._head is None:
            raise SLLException

        loc = 0
        current = self._head
        count = 0
        # looping through the list
        while current is not None:
            # if the list value matches the value
            if current.value == value:
                # then it increments count by 1
                count += 1
            # else continues the loop
            current = current.next
            loc += 1
        return count

    def find(self, value: object) -> bool:
        # if the list has nothing raises an exception
        if self._head is None:
            raise SLLException
        current = self._head
        # looping through the list
        while current is not None:
            # if the list value matches the value
            if current.value == value:
                # returns true
                return True
            current = current.next
        # if the loop end without return then it returns False
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        # if the list has nothing raises an exception
        if self._head is None:
            raise SLLException()
        # for the negative index
        if start_index < 0:
            raise SLLException()

        # if the end point of the requested list exceeds the length of the list and
        # it raises an exception for outbound index
        if start_index + size > self.length() :
            raise SLLException()

        loc = 0
        new_size = 0
        current = self._head
        # creating new empty list to hold the sliced list
        sliced_list = LinkedList()
        # looping through the list
        while current is not None:
            # if the start index is larger than the current index
            if start_index < loc:
                # it starts to get fill the new empty list
                new_size += 1
                sliced_list.insert_back(current.value)
            # if the requested size reaches, then it returns the new list
            if new_size == size:
                return sliced_list
            # else continues the loop
            current = current.next
            loc += 1
        # if the loops until the end it returns the list
        # it doesn't return if the requested size is out of bond,
        # because if it happens it breaks the loop at beginning of the function
        return sliced_list


if __name__ == '__main__':

    print('\n# insert_front example 1')
    test_case = ['A', 'B', 'C']
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print('\n# insert_back example 1')
    test_case = ['C', 'B', 'A']
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_at_index example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 2, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# remove example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, length: {lst.length()}"
              f"\n  {lst}")

    print('\n# remove example 2')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, length: {lst.length()}"
              f"\n  {lst}")

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")