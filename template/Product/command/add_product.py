# filepath: c:\Users\btnka\Desktop\Project\drf-template-boilerplate\drf-template-boilerplate\template\Product\command\add_product.py
import os
import sys
import random
import django
from decimal import Decimal
from faker import Faker

# Thiết lập môi trường Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'template.settings')
django.setup()

from Product.models import Product

def add_random_products(count=100):
    """
    Tạo và lưu số lượng sản phẩm ngẫu nhiên được chỉ định
    """
    fake = Faker()
    products_created = 0
    
    # Các danh mục sản phẩm để tạo tên chân thực hơn
    product_categories = [
        "Điện thoại", "Laptop", "Máy tính bảng", "Tai nghe", "Chuột", "Bàn phím",
        "Màn hình", "Loa", "Camera", "Đồng hồ thông minh", "TV", "Tủ lạnh",
        "Máy giặt", "Điều hòa", "Quạt", "Nồi cơm điện", "Bếp điện", "Bàn",
        "Ghế", "Giường", "Tủ quần áo", "Đèn", "Sách", "Áo", "Quần", "Giày",
        "Túi xách", "Ví", "Mũ", "Kính mát"
    ]
    
    for _ in range(count):
        category = random.choice(product_categories)
        adjective = fake.word()
        brand = fake.company().split()[0]  # Lấy phần đầu tiên của tên công ty
        
        # Tạo tên sản phẩm kết hợp
        name = f"{brand} {adjective.capitalize()} {category}"
        
        # Tạo giá ngẫu nhiên từ 50,000 đến 20,000,000 VNĐ
        price = Decimal(random.randint(50, 20000) * 1000)
        
        # Tạo sản phẩm mới
        product = Product(name=name, price=price)
        product.save()
        products_created += 1
        
    return products_created

if __name__ == "__main__":
    print("Bắt đầu tạo sản phẩm ngẫu nhiên...")
    count = add_random_products()
    print(f"Đã tạo thành công {count} sản phẩm ngẫu nhiên.")