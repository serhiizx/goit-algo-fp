"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
"""

from linked_list import LinkedList, Node
import random

"""
Створюємо класс наслідуючись від класу звʼязаного списку (взятий з конкпекту).
Додаємо в нього ф-цію reverse як частину завдання.
"""
class ReversableLinkedList(LinkedList):
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self

"""
Створюємо класс наслідуючись від ReversableLinkedList.
Додаємо в нього ф-цію sort як частину завдання.
"""
class SortableLinkedList(ReversableLinkedList):
    def sort(self):
        self.head = self._merge_sort(self.head)
        return self
    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head
        # Роозділити список навпіл
        middle = self._get_middle(head)
        right_side_start = middle.next
        middle.next = None

        # Рекурсивно сортувати обидві половини і змержити
        return self._merge(self._merge_sort(head), self._merge_sort(right_side_start))
    
    def _get_middle(self, head):
        """
        Для пошуку середини списка використовуємо техніку "повільний-швидкий"
        Оскільки fast рухається в два рази швидше за slow
        то коли fast дійде до кінця, slow буде вказувати рівно на середину
        """
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)
        return result
    

"""
Функція злиття двох відсортованих списків в один.
"""
def merge_sorted_list(leftList, rightList):
    result = SortableLinkedList()
    left = leftList.head
    right = rightList.head
    node = Node()
    current = node
    while left and right:
        if left.data <= right.data:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    current.next = left if left else right
    result.head = node.next
    return result

list1 = SortableLinkedList([random.randint(1, 100) for _ in range(8)])
list2 = SortableLinkedList([random.randint(1, 100) for _ in range(8)])
list2.sort()

print(f"Зв'язний список: \n{list1}")
print(f"\nЗв'язний список після реверсу: \n{list1.reverse()}")
print(f"\nЗв'язний список після сортування: \n{list1.sort()}")

print("\nОбʼєднані два відсортовані списки:")
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"\nmerged_lists = {merge_sorted_list(list1, list2)}")
