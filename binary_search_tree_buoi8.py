class Node:
  def __init__(self, value):
      self.value = value #set giá trị cho nút đầu tiên
      self.left = None#khởi tạo giá trị nhánh trái,phải là None
      self.right = None

class BinarySearchTree: #tạo thư viện và gán giá trị gốc của cây là None
  def __init__(self):
      self.root = None

  def insert(self, value):
      if not self.root:#nếu câu đang rỗng
          self.root = Node(value)
        #chèn gtri vào nút gốc
      else:
          self._insert_recursively(self.root, value)#không thì chèn vào các nút trên thân.

  def _insert_recursively(self, node, value):
      if value < node.value:#nếu giâ trị nhỏ hơn giá trị nút hiện tại
          if node.left is None:#nếu k có nút bên trái
              node.left = Node(value)#tạo một nút mới và gán vào nút vừa tạo
          else:
              self._insert_recursively(node.left, value)#nếu có thì chèn ko cần tạo
      else:
          if node.right is None:#nếu lớn hơn
              node.right = Node(value)#tạo một nút bên phải và gân vào
          else:#nếu có rồi thì gân trực tiếp vào
              self._insert_recursively(node.right, value)

  def inorder_traversal(self):
      traversal_result = []#khởi tạo biến để lưu cây vừa tạo
      self._inorder_traversal_recursive(self.root, traversal_result)
      return traversal_result#trả về giá trị của cây vừa tạo

  def _inorder_traversal_recursive(self, node, traversal_result):
      if node:#nếu nuat ko rỗng
          self._inorder_traversal_recursive(node.left, traversal_result)#duyệt nhánh cây bên trái
          traversal_result.append(node.value)#thêm giá trị của nút vào cây
          self._inorder_traversal_recursive(node.right, traversal_result)#duyệt nhánh cây bên phải

# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(17)

print("Inorder traversal:", bst.inorder_traversal())  # Output: [3, 5, 7, 10, 12, 15, 17]
