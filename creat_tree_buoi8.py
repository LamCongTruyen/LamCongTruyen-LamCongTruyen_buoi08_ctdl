#root:     gốc của tree
#leaf:     nút lá không còn nhánh nào thêm nữa
#sibling:  hai nút lá có cùng gốc
#ancestor: mối quan hệ gốc chính>>gốc cha>>gốc con>...

#depth of node:   chiều dài của nhánh tính từ gốc
#height of node:  chiều dài của nhánh tính từ 1 nút bất kì

class tree_node: #tạo thư viện cây mã
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"  #ret = root(gốc) 
        for child in self.children:#Tạo chuỗi ret bằng cách thêm vào chuỗi khoảng trắng với độ dài bằng với level, sau đó thêm dữ liệu của nút và một dấu xuống dòng.
            ret += child.__str__(level + 1)
        return ret
    def add_child(self, tree_node): #tạo hàm thêm nút vào cây mã
        self.children.append(tree_node)

tree = tree_node('Drink' , []) #khai báo nút drink
cold = tree_node('cold', []) #tương tự
hot = tree_node('hot', []) 
winter = tree_node('winter', []) #khai báo nút winter
tree.add_child(cold) #thêm hai nút cold và hot làm nút con của drink
tree.add_child(hot)
cold.add_child(winter) #thêm nút winter vào làm nút con của nút cold
print(tree)