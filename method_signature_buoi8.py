class tree_node: #tajo moojt thư viện có tên treenode
    def __init__(self, value):
        self.value = value
        self.children = [] #khởi tạo một ds trống để lưu trữ các nút con

    def add_child(self, child): #hàm thêm một nút con mới vào nút con trống hiện tại
        #nhận giá trị của biến child
        self.children.append(child) 

    def __str__(self, level=0): #hàm tạo chuỗi ret(gốc) 
        indent = "  " * level
        tree_str = indent + str(self.value) + "\n"
        for child in self.children: #Vòng lặp này lặp qua danh sách con của nút cây hiện tại
            tree_str += child.__str__(level + 1)
        return tree_str

# Example usage
if __name__ == "__main__":
    root = tree_node(1) #tạo một biến root lưu lớp treenode
    root.add_child(tree_node(2)) #thêm một nút con sau nút gốc
    root.add_child(tree_node(3)) #tương tự
    child2 = tree_node(4) #tạo gốc mới có tên child2
    child2.add_child(tree_node(5)) #thêm một nút con sau gốc mới vừa tạo
    root.add_child(child2) # gốc mới vừa tạo lại dc biến thành nút con của gốc root
    
    print(root) #in ra  cây có gốc root
