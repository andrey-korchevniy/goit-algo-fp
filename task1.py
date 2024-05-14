class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse(self):
        current = self.head
        previous = None

        while current:
            next_el = current.next

            # обробляємо випадок першого елемента у списку
            if not previous:
                previous = current
                previous.next = None
                current = next_el
                continue

            # обробляємо випадок останнього елемента у списку
            if not next_el:
                current.next = previous
                self.head = current
                break

            # обробляємо внутрішні елементи списку
            current.next = previous
            previous = current
            current = next_el
        return


    def insertion_sort(self):
        # Створюємо "фіктивний" вузол як новий початок списку
        dummy = Node(0)
        dummy.next = self.head
        curr = self.head

        # Зовнішній цикл проходить по кожному елементу у списку
        while curr and curr.next:
            if curr.data <= curr.next.data:
                curr = curr.next
            else:
                # Елемент, що вимагає переміщення
                to_insert = curr.next
                curr.next = to_insert.next

                # Вставка елементу в потрібне місце
                prev = dummy
                while prev.next and prev.next.data <= to_insert.data:
                    prev = prev.next

                to_insert.next = prev.next
                prev.next = to_insert

        self.head = dummy.next


    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        dummy = Node()
        current = dummy
        list1 = self.head
        list2 = other_list.head

        while list1 and list2:
            if list1.data <= list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        merged_list.head = dummy.next
        return merged_list


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(40)
llist.insert_at_beginning(30)
llist.insert_at_beginning(20)
llist.insert_at_beginning(10)
llist.insert_at_beginning(5)
llist.insert_at_beginning(1)

print("Зв'язний список:")
llist.print_list() # 1 5 10 20 30 40

print('Здійснюємо реверс')
llist.reverse()

print("Зв'язний список після реверсу:")
llist.print_list() # 40 30 20 10 5 1

llist.insertion_sort()

print("Зв'язний список після сортування вставками (в порядку зростання):")
llist.print_list() # 1 5 10 20 30 40

other_list = LinkedList()

other_list.insert_at_beginning(45)
other_list.insert_at_beginning(35)
other_list.insert_at_beginning(25)
other_list.insert_at_beginning(15)
other_list.insert_at_beginning(5)
other_list.insert_at_beginning(1)

print('Новий список, який складається з двох списків:')
llist.merge_sorted_lists(other_list)
llist.print_list() # 1 1 5 5 10 15 20 25 30 35 40 45