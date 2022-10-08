class ListNode:
   def __init__(self, data, next = None):
      self.data = data
      self.next = next
def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head
def get_node(head, pos):
   if pos != -1:
      p = 0
      ptr = head
      while p < pos:
         ptr = ptr.next
         p += 1
      return ptr
class Solution(object):
   def hasCycle(self, head):
      hashS = set()
      while head:
         if head in hashS:
            return True
         hashS.add(head)
         head = head.next
      return False
# Example 1 : input [3,2,0,-4] pos= 1
head = make_list([3,2,0,-4])
last_node = get_node(head,3)
pos = 1
last_node.next = get_node(head, pos)
ob1 = Solution()
print(ob1.hasCycle(head))

# Example 2 : input [1,2] pos= 1
head = make_list([1,2])
last_node = get_node(head,1)
pos = 0
last_node.next = get_node(head, pos)
ob1 = Solution()
print(ob1.hasCycle(head))

# Example 3 : input [1] pos= -1

head = make_list([1])
last_node = get_node(head,0)
pos = -1
last_node.next = get_node(head, pos)
ob1 = Solution()
print(ob1.hasCycle(head))