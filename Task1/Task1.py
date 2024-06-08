class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            sorted_list.sorted_insert(Node(current.data))
            current = next_node
        self.head = sorted_list.head

    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged_list = LinkedList()
        dummy = Node(0)
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        merged_list.head = dummy.next
        return merged_list

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    # Створення списків
    list1 = LinkedList()
    list1.sorted_insert(Node(3))
    list1.sorted_insert(Node(8))
    list1.sorted_insert(Node(12))

    list2 = LinkedList()
    list2.sorted_insert(Node(2))
    list2.sorted_insert(Node(9))
    list2.sorted_insert(Node(11))

    print("Перший відсортований список (list1):")
    list1.print_list()

    print("Другий відсортований список (list2):")
    list2.print_list()

    # Об'єднання та сортування списків
    merged_list = LinkedList.merge_sorted_lists(list1.head, list2.head)

    print("Об'єднаний відсортований список:")
    merged_list.print_list()

    # Реверс одного зі списків
    list1.reverse()
    print("Реверсований перший список (list1):")
    list1.print_list()
