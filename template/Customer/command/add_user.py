# filepath: c:\Users\btnka\Desktop\Project\drf-template-boilerplate\drf-template-boilerplate\template\Customer\command\add_user.py
import os
import sys
import random
import string
import django
from faker import Faker

# Thiết lập đường dẫn để Django có thể tìm thấy các module
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'template.settings')
django.setup()

from Customer.models import Customer

def generate_random_phone():
    """Tạo số điện thoại ngẫu nhiên theo định dạng Việt Nam."""
    prefixes = ['086', '096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039', '090', '093', '070', '079', '077', '076', '078']
    suffix = ''.join(random.choices(string.digits, k=7))
    return random.choice(prefixes) + suffix

def create_users(count=100):
    """Tạo và lưu số lượng user được chỉ định vào cơ sở dữ liệu."""
    fake = Faker('vi_VN')  # Sử dụng localization tiếng Việt
    
    print(f"Bắt đầu tạo {count} người dùng...")
    
    # Danh sách để lưu trữ các đối tượng Customer
    customers = []
    
    for i in range(count):
        name = fake.name()
        email = fake.email()
        phone = generate_random_phone()
        address = fake.address()
        
        customer = Customer(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        customers.append(customer)
        
        # In tiến trình
        if (i + 1) % 10 == 0 or i + 1 == count:
            print(f"Đã tạo {i + 1} người dùng")
    
    # Sử dụng bulk_create để tối ưu hóa việc lưu vào cơ sở dữ liệu
    Customer.objects.bulk_create(customers)
    print(f"Hoàn thành! Đã tạo {count} người dùng.")

if __name__ == "__main__":
    # Lấy số lượng user từ tham số dòng lệnh hoặc mặc định là 100
    count = 100
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Số lượng không hợp lệ, sử dụng giá trị mặc định (100)")
    
    create_users(count)