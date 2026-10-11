#Họ và Tên: Nguyễn Đức Hưng
#MSSV:202418913
from models import(Computer,Printer,Projector,LabRoom,NetworkConnection,DeviceStatus)
def test():
    # Tạo thiết bị: 2 máy tính (pc2 có GPU rời)
    pc1 = Computer("PC01", "Dell", 2022, 15000000, 16, "Intel i5", False)
    pc2 = Computer("PC02", "HP", 2018, 30000000, 32, "Intel i7", True)        # có GPU rời
    # 2 máy in (pr1 in > 100.000 trang, có mạng; pr2 không mạng, đang bảo trì)
    pr1 = Printer("PR01", "HP Laser", 2019, 8000000, "Laser", 120000, False,
                NetworkConnection())                                       # in > 100.000 trang, có mạng
    pr2 = Printer("PR02", "Canon", 2023, 4000000, "Phun", 5000, True,
                status=DeviceStatus.UNDER_MAINTENANCE)
    # 1 máy chiếu (bóng đèn > 3.000 giờ)
    pj1 = Projector("PJ01", "Epson", 2017, 12000000, 3800, 3500)             # bóng đèn > 3.000 giờ

    # Tạo 2 phòng thực hành
    room1 = LabRoom("P101", "Phòng A", 30)
    room2 = LabRoom("P102", "Phòng B", 20)

    # 1. Thêm thiết bị vào phòng
    room1.add_device(pc1)
    room1.add_device(pc2)
    room1.add_device(pr1)
    room2.add_device(pr2)
    room2.add_device(pj1)

    # 2. Thêm thiết bị trùng mã (bị từ chối)
    try:
        room1.add_device(pc1)
    except ValueError as e:
        print("Lỗi:", e)

    # 3. In danh sách thiết bị từng phòng
    print(room1)
    print(room2)

    # 4. Tổng chi phí bảo trì mỗi phòng
    print("Chi phí P101:", room1.calculate_annual_maintenance_cost())
    print("Chi phí P102:", room2.calculate_annual_maintenance_cost())

    # 5. Liệt kê thiết bị cần bảo trì
    print("Cần bảo trì:")
    for d in room1.get_devices_requiring_maintenance() + room2.get_devices_requiring_maintenance():
        print(" ", d)

    # 6. Kết nối mạng
    pc1.connect("192.168.1.1")
    pc2.connect("192.168.1.2")
    pr1.network.connect("192.168.1.3")

    # 7. Duyệt thiết bị mạng qua INetworkable (không phụ thuộc lớp cụ thể)
    print("Thiết bị mạng:")
    for n in room1.get_networkable_devices() + room2.get_networkable_devices():
        print(" ", n.ip_address, n.is_connected)
if __name__=="__main__":
    test()
