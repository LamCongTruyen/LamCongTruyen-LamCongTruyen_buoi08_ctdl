class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value) #tạo biến nút mới 
        if self.root is None: #nếu giá trị của gốc là trống
            self.root = new_node #thì giá trị nút mới sẽ là gốc
            return True
        
        temp = self.root #tạo bvieesn đếm 
        while True: #nếu đúng
            if value == temp.value: #ktra giá trị đã tồn tại chwua, nếu rồi trả về false
                return False
            elif value < temp.value:#Kiểm tra xem giá trị cần chèn vào nhỏ hơn giá trị của nút hiện tại hay không.
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
