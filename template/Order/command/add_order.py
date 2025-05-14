# filepath: c:\Users\btnka\Desktop\Project\drf-template-boilerplate\drf-template-boilerplate\template\Order\command\add_order.py
import os
import sys
import random
import django
import datetime
from faker import Faker

# Thiết lập môi trường Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'template.settings')
django.setup()

from Order.models import Order
from OrderItem.models import OrderItem
from Product.models import Product
from Customer.models import Customer

def create_random_orders(count=100):
    """
    Tạo số lượng đơn hàng ngẫu nhiên được chỉ định với các mục đơn hàng
    """
    fake = Faker('vi_VN')
    
    # Kiểm tra xem có khách hàng không
    customers = list(Customer.objects.all())
    if not customers:
        print("Không tìm thấy khách hàng. Vui lòng tạo khách hàng trước.")
        return 0
    
    # Kiểm tra xem có sản phẩm không
    products = list(Product.objects.all())
    if not products:
        print("Không tìm thấy sản phẩm. Vui lòng tạo sản phẩm trước.")
        return 0
    
    print(f"Bắt đầu tạo {count} đơn hàng ngẫu nhiên...")
    orders_created = 0
    
    for i in range(count):
        # Chọn ngẫu nhiên một khách hàng
        customer = random.choice(customers)
        
        # Tạo đơn hàng mới
        order = Order(customer=customer)
        order.save()
        
        # Quyết định số lượng sản phẩm trong đơn hàng (1-5)
        item_count = random.randint(1, 5)
        
        # Chọn các sản phẩm ngẫu nhiên không trùng lặp
        order_products = random.sample(products, min(item_count, len(products)))
        
        # Tạo các mục đơn hàng
        for product in order_products:
            quantity = random.randint(1, 10)  # Số lượng từ 1-10
            
            # Tạo mục đơn hàng
            order_item = OrderItem(
                order=order,
                product=product,
                quantity=quantity
            )
            order_item.save()
        
        orders_created += 1
        
        # In tiến trình
        if (i + 1) % 10 == 0 or i + 1 == count:
            print(f"Đã tạo {i + 1} đơn hàng")
    
    print(f"Hoàn thành! Đã tạo {orders_created} đơn hàng ngẫu nhiên.")
    return orders_created

if __name__ == "__main__":
    # Lấy số lượng đơn hàng từ tham số dòng lệnh hoặc mặc định là 100
    count = 100
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Số lượng không hợp lệ, sử dụng giá trị mặc định (100)")
    
    create_random_orders(count)