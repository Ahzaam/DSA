# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:



from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

 

    def add(self, node: object) -> None:
        """ 
        this function takes a node and appends it to the array and performes Heap operations 
        
        """
        # appends the node at last of the heap
        self._heap.append(node)

        current = self._heap.length() -1

        # performes heap operation to find the best place to the node
        _percolate_up(self._heap, current)


    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        """
        return self._heap.is_empty()

    def get_min(self) -> object:
        """
         It returns the root element of Min Heap. Time Complexity of this operation is O(1)   
        """
        return self._heap[0]

    def remove_min(self) -> object:
        """
        Removes the minimum element from MinHeap.
         Time Complexity of this Operation is O(Log n) 
         as this operation needs to maintain the heap property (by calling heapify()) after removing root.

        """
        if self._heap.is_empty():
            raise MinHeapException
        # print(self._heap.length())
        min = self._heap[0]
        last_child_ind = self._heap.length() -1
        swap(self._heap._data, 0, last_child_ind)
        self._heap.remove_at_index(last_child_ind)
        _percolate_down(self._heap, 0)
       
        
        return min

    def build_heap(self, da: DynamicArray) -> None:
        """
        This function takes dynamic array and replaces heap with dynamic array values O(n)
        and loops through the new heap and percolates only if the the node has a child O(n/2)

        total time complacity O(n)
        """
        n= da.length() 

        # Clears the previous array
        self.clear()

        # adds the dynamic array values to to the heap
        for i in range(0, n):
           self._heap.append(da[i])
        
        # loops trough new heap 
        for i in range(0, n):
            # checks weather node has a child else breaks the loop, because if one node doesn't hava a child
            # nodes after that will doesn't have a child 
            if leftChild(i) < n:
                # percolating the parent value
                _percolate_down(self._heap, i)
            else:
                break
            
       

    def size(self) -> int:
        """
        returns the dynamic array size its equal to heap size
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the heap 
        """
        self._heap._size = 0

# These are custom defined functions

def parent(pos):
    """ 
    Function takes the current node and returns the parent node of the element 
    """
    return int((pos -1) / 2)

def swap(self, fpos, spos):
    """ 
    Function takes two arguments first position (fpos) and second position (spos) and swaps those values
    """

    self[fpos], self[spos] = self[spos], self[fpos]

def leftChild(pos):
    """ 
    Function takes the position of the parent element and returns the left childs index 
    """
    return (2 * pos) + 1
    
def rightChild(pos):
    """ 
    Function takes the position of the parent element and returns the right childs index  
    """
    return (2 * pos) + 2
def heapify(arr, n, i):
    """
    function takes the array, index  and hepifies the array
    """



    largest = i  # Initialize largest as root
    l = leftChild(i)     # left = 2*i + 1
    r = rightChild(i)     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
 

def heapsort(da: DynamicArray) -> None:

    n= da.length()
    
    # Hepifies the array
    for i in range(n//2 - 1, -1, -1):
        heapify(da, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        da[i], da[0] = da[0], da[i]  # swap
        heapify(da, i, 0)
    


    # Revercing the heap by swapping element 
    # from left side to right
    from_last = da.length() -1
    from_start = 0
    
    while True:
        # if the swapping index was equal the breaks the loop
        if from_last == from_start:
            break
        # if the swapping index was equal to +1 the right then breaks the loop
        # if array length was a odd number
        if from_last + 1 == from_start:
            break
        # swapping elements
        swap(da, from_last, from_start)
        from_start += 1
        from_last -= 1

        
        


def _percolate_up(da: DynamicArray, current: int) -> None:
    # performes heap operation to find the best place to the node
    # print(current , parent(current), da.length())

    while da[current] < da[parent(current)]:
            swap(da, current, parent(current))
            current = parent(current)

    
             


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #


def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    This function takes a dynamic array and checks weather the array full fills heap rule
    else it will rearrange the order

    """
    while True:
        
        # initializing the staring childs
        left_child = leftChild(parent)
        right_child = rightChild(parent)
       
    
        # if the left child index was inside the 
        if left_child < da._size:
            # and if right child index was inside the array
            if right_child < da._size:
                # getts the child with the minumum value
                min_child = min(da[right_child], da[left_child])
                # if it's left child 
                if da[left_child] == min_child:
                    min_child_ind = left_child
                # else it will be the right child
                else:
                    min_child_ind = right_child

            # if the parent doesnt have a right child the the minimun value child is left child
            else:
                min_child_ind = left_child
            
            # if the child is greater than child else breaks the loop
            if da[min_child_ind] < da[parent]:
                # Then swaps the elements
                swap(da, min_child_ind, parent)
                # percolating
                _percolate_down(da, parent)
                # initializing the new parent
                parent = min_child_ind
            else:
                break
        else:
            break
    
            

    


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
