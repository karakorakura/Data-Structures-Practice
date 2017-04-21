

class MinHeap(object):
    def __init__(self):
        self.heap = []
        self.length = 0

    # Constructor equivalent of build_min_heap
    def __init__(self, arr):
        self.length = len(arr)
        self.heap = arr
        i = self.length//2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    # Get the children of index i as array
    @staticmethod
    def children(i):
        return [2 * i + 1, 2 * i + 2]

    # Get parent of index i
    @staticmethod
    def parent(i):
        return i / 2 if i % 2 else i / 2 - 1

    def min_heapify(self, i):
        left, right = MinHeap.children(i)
        if left < self.length and self.heap[left] < self.heap[i]:
            smallest = left
        else:
            smallest = i
        if right < self.length and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.min_heapify(smallest)

    def is_empty(self):
        return True if len(self.heap) == 0 else False

    def insert(self, new_elem):
        self.heap.append(new_elem)
        self.length += 1
        index = self.length - 1
        while index > 0:
            parent = MinHeap.parent(index)
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def find_min(self):
        return None if self.length == 0 else self.heap[0]

    def delete_min(self):
        if self.length == 0:
            return None
        min_elem = self.heap[0]
        self.heap[0], self.heap[self.length - 1] = self.heap[self.length - 1], self.heap[0]
        self.heap.pop()
        self.length -= 1
        if self.length != 0:
            self.min_heapify(0)
        return min_elem

def heap_sort(heap):
    arr = []
    while not heap.is_empty():
        arr.append(heap.delete_min())
    return arr

def print_heap(heap):
    print "Current heap is: ",
    print heap.heap

heap = MinHeap([1, 5, 8, 9, -5, -4])
print_heap(heap)

heap.insert(int(raw_input("Enter an element to insert: ")))
print_heap(heap)

print "The minimum element in heap is: ",
print heap.find_min()

heap.delete_min()
print "Minimum element is deleted."
print_heap(heap)

print "Sorted heap is: ",
print heap_sort(heap)
