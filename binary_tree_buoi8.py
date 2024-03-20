class tree_node:
    def __init__(self,data):
        self.data = data
        self.left_child = None #khởi tạo giá trị cho nút trái của tree
        self.right_child = None #tương tự với nút bên phải

new_bt = tree_node ("drink") #tạo nút gốc
left_child = tree_node("hot") #tạo nút nhánh bên trái
right_child = tree_node("cold")#tạo nút nhánh bên phải
new_bt.left_child = left_child #gán nút bên trái vào gốc
new_bt.right_child = right_child #tương tự

def pre_order_travelsal(root_node):
    if not root_node: #ktra xem nút gốc tồn tại k
        return
    print(root_node.data)
    pre_order_travelsal(root_node.left_child)#Duyệt cây theo thứ tự trước trên cây con bên trái của nút gốc.
    pre_order_travelsal(root_node.right_child)#Duyệt cây theo thứ tự trước trên cây con bên phải của nút gốc.

pre_order_travelsal(new_bt)