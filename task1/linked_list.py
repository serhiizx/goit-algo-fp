class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self, values = None):
    self.head = None
    if values:
      for value in values:
        self.insert_at_end(value)

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    print(self.__str__())

  def __str__(self):
    current = self.head
    result = []
    while current:
      result.append(str(current.data))
      current = current.next
    return ', '.join(result)
  
  def __repr__(self):
    return f"LinkedList([{self.__str__()}])"