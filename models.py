#Họ và Tên: Nguyễn Đức Hưng
#MSSV:202418913
from enum import Enum
from abc import ABC,abstractmethod
from datetime import date

# Enum trạng thái thiết bị
class DeviceStatus(Enum):
    ACTIVE="Active"
    UNDER_MAINTENANCE="Undermaintenance"
    RETIRED="Retired"

# Interface khả năng kết nối mạng (chỉ khai báo, lớp con tự cài đặt)
class INetworkable(ABC):
    @property
    @abstractmethod
    def ip_address(self):
        pass
    @property
    @abstractmethod
    def is_connected(self):
        pass
    @abstractmethod
    def connect(self,ip_address):
        pass
    @abstractmethod
    def disconnect(self):
        pass

# Thành phần kết nối mạng, được kết tập vào Printer
class NetworkConnection(INetworkable):
    def __init__(self):
        self._ip_address=None
    # IP hiện tại (None nếu chưa kết nối)
    @property
    def ip_address(self):
        return self._ip_address
    # Đang kết nối khi có IP
    @property
    def is_connected(self):
        return self._ip_address is not None
    # Kết nối: IP không rỗng, không kết nối lại khi đang kết nối
    def connect(self,ip_address):
        if self.is_connected:
            raise ValueError("Thiết bị đang kết nối")
        if not ip_address or not ip_address.strip():
            raise ValueError("Địa chỉ IP không được rỗng")
        else:
            self._ip_address=ip_address
    # Ngắt kết nối: xóa IP
    def disconnect(self):
        self._ip_address=None

# Lớp trừu tượng thiết bị (cha của Computer, Printer, Projector)
class Device(ABC):
    def __init__(self,device_id,name,year_in_use,purchase_price,status=DeviceStatus.ACTIVE):
        # Mã thiết bị: không rỗng, chỉ gán ở đây (không có setter)
        if device_id is None or not device_id.strip():
            raise ValueError("Mã thiết bị không được rỗng")
        self._device_id=device_id
        self.name=name
        self.year_in_use=year_in_use
        self.purchase_price=purchase_price
        self.status=status
    # Mã thiết bị (chỉ đọc)
    @property
    def device_id(self):
        return self._device_id
    # Giá mua (phải > 0)
    @property
    def purchase_price(self):
        return self._purchase_price
    @purchase_price.setter
    def purchase_price(self,value):
        if value <=0:
            raise ValueError("Giá mua phải lớn hơn 0")
        self._purchase_price=value
    # Tên thiết bị (không rỗng)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if value is None or not value.strip():
            raise ValueError("Tên thiết bị không được rỗng")
        self._name=value
    # Năm đưa vào sử dụng (không lớn hơn năm hiện tại)
    @property
    def year_in_use(self):
        return self._year_in_use
    @year_in_use.setter
    def year_in_use(self,value):
        if not isinstance(value,int):
            raise ValueError("Năm phải là số nguyên")
        if value <1975 or value > date.today().year:
            raise ValueError("Năm không hợp lệ")
        self._year_in_use=value
    # Trạng thái (phải là DeviceStatus)
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,value):
        if not isinstance(value,DeviceStatus):
            raise ValueError("Trạng thái không hợp lệ")
        self._status=value
    # Số năm đã sử dụng
    @property
    def age(self):
        self._age=date.today().year-self.year_in_use
        return self._age
    # Chi phí bảo trì 1 năm (mỗi lớp con tự tính)
    @abstractmethod
    def calculate_annual_maintenance_cost(self):
        pass
    # Chuỗi mô tả thiết bị
    def __str__(self):
        return (f"{self.device_id}-{self.name}-{self.year_in_use}-{self.purchase_price:,.0f}-{self.status.value}")

# Máy tính: kế thừa Device, thực thi INetworkable
class Computer(Device,INetworkable):
    def __init__(self,device_id,name,year_in_use,purchase_price,ramgb,processorType,hasDedicatedGPU,status=DeviceStatus.ACTIVE):
        super().__init__(device_id,name,year_in_use,purchase_price,status)
        self.ramgb=ramgb
        self.processorType=processorType
        self.hasDedicatedGPU=hasDedicatedGPU
        self._ip_address=None
    # Dung lượng RAM (số nguyên > 0)
    @property
    def ramgb(self):
        return self._ramgb
    @ramgb.setter
    def ramgb(self,value):
        if not isinstance(value,int) or value <=0:
            raise ValueError("Ram phải là 1 số nguyên lớn hơn 0")
        self._ramgb=value
    # Loại bộ xử lý (không rỗng)
    @property
    def processorType(self):
        return self._processorType
    @processorType.setter
    def processorType(self,value):
        if value is None or not value.strip():
            raise ValueError("Bộ xử lí không được để trống")
        self._processorType=value
    # Có GPU rời hay không (bool)
    @property
    def hasDedicatedGPU(self):
        return self._hasDedicatedGPU
    @hasDedicatedGPU.setter
    def hasDedicatedGPU(self,value):
        if not isinstance(value,bool):
            raise ValueError("Kiểu dữ liệu nhập sai")
        self._hasDedicatedGPU=value
    # Các hàm mạng (cài đặt INetworkable)
    @property
    def ip_address(self):
        return self._ip_address
    @property
    def is_connected(self):
        return self._ip_address is not None
    def connect(self,ip_address):
        if self.is_connected:
            raise ValueError("Thiết bị đang kết nối")
        if not ip_address or not ip_address.strip():
            raise ValueError("Địa chỉ IP không được rỗng")
        else:
            self._ip_address=ip_address
    def disconnect(self):
        self._ip_address=None
    # Chi phí bảo trì: 5% giá, +2% nếu có GPU rời, +1% nếu dùng > 5 năm
    def calculate_annual_maintenance_cost(self):
        cost =self.purchase_price*0.05
        if self.hasDedicatedGPU:
            cost+=self.purchase_price*0.02
        if self.age >5:
            cost+=self.purchase_price*0.01
        return cost
    def __str__(self):
        return f"{super().__str__()}--{self.ramgb}--{self.hasDedicatedGPU}--{self.processorType}"

# Máy in: kế thừa Device, kết tập NetworkConnection (None nếu không có mạng)
class Printer(Device):
    def __init__(self,device_id,name,year_in_use,purchase_price,printer_type,pages_printed,is_color,network=None,status=DeviceStatus.ACTIVE):
        super().__init__(device_id,name,year_in_use,purchase_price,status)
        self.printer_type=printer_type
        self.pages_printed=pages_printed
        self.is_color=is_color
        self.network=network
    # Loại máy in (laser/phun)
    @property
    def printer_type(self):
        return self._printer_type
    @printer_type.setter
    def printer_type(self,value):
        if value is None or not value.strip():
            raise ValueError("Không bỏ trống loại máy in")
        self._printer_type=value
    # Số trang đã in (>= 0)
    @property
    def pages_printed(self):
        return self._pages_printed
    @pages_printed.setter
    def pages_printed(self,value):
        if not isinstance(value,int) or value <0:
            raise ValueError("Số trang đã in phải là một số nguyên lớn hơn hoặc bằng 0")
        self._pages_printed=value
    # Máy in màu hay không (bổ sung để tính phụ phí 300.000)
    @property
    def is_color(self):
        return self._is_color
    @is_color.setter
    def is_color(self,value):
        if not isinstance(value,bool):
            raise ValueError("Nhập sai kiểu dữ liệu đầu vào")
        self._is_color=value
    # Thành phần mạng (NetworkConnection hoặc None)
    @property
    def network(self):
        return self._network
    @network.setter
    def network(self,value):
        if value is not None and not isinstance(value,NetworkConnection):
            raise ValueError("Sai kiểu dữ liệu đầu vào")
        self._network=value
    # Máy in có hỗ trợ mạng không
    @property
    def support_network(self):
        return self._network is not None
    # Chi phí bảo trì: 4% giá, +500.000 nếu > 100.000 trang, +300.000 nếu là máy in màu
    def calculate_annual_maintenance_cost(self):
        cost=self.purchase_price*0.04
        if self.pages_printed>100000:
            cost+=500000
        if self.is_color:
            cost+=300000
        return cost
    def __str__(self):
        return f"{super().__str__()}--{self.printer_type}--{self.pages_printed}--{self.is_color}--{self.support_network}"

# Máy chiếu: kế thừa Device, không có mạng
class Projector(Device):
    def __init__(self,device_id,name,year_in_use,purchase_price,brightness_lumen,lamp_hours,status=DeviceStatus.ACTIVE):
        super().__init__(device_id,name,year_in_use,purchase_price,status)
        self.brightness_lumen=brightness_lumen
        self.lamp_hours=lamp_hours
    # Độ sáng (lumen, > 0)
    @property
    def brightness_lumen(self):
        return self._brightness_lumen
    @brightness_lumen.setter
    def brightness_lumen(self,value):
        if not isinstance(value,int) or value <=0:
            raise ValueError("Độ sáng phải lớn hơn 0 lumen")
        self._brightness_lumen=value
    # Số giờ đã dùng bóng đèn (>= 0)
    @property
    def lamp_hours(self):
        return self._lamp_hours
    @lamp_hours.setter
    def lamp_hours(self,value):
        if  not isinstance(value,int) or value <0:
            raise ValueError("Bóng phải sáng lớn hơn hoặc bằng 0 giờ")
        self._lamp_hours=value
    # Chi phí bảo trì: 3% giá, +1.500.000 nếu bóng đèn > 3.000 giờ
    def calculate_annual_maintenance_cost(self):
        cost=self.purchase_price*0.03
        if self.lamp_hours>3000:
            cost+=1500000
        return cost
    def __str__(self):
        return f"{super().__str__()}--{self.brightness_lumen}--{self.lamp_hours}"

# Phòng thực hành: kết tập nhiều thiết bị
class LabRoom:
    def __init__(self,room_id,name,capacity):
        if room_id is None or not room_id.strip():
            raise ValueError("Mã phòng không để trống")
        self._room_id=room_id
        if name is None or not name.strip():
            raise ValueError("Tên phòng không để trống")
        self._name=name
        if not isinstance(capacity,int) or capacity <=0:
            raise ValueError("Sức chưa phải là số nguyên lớn hơn 0 ")
        self._capacity=capacity
        self._devices=[]
    # Danh sách thiết bị của phòng (trả về bản sao)
    @property
    def devices(self):
        return list(self._devices)

    # Tìm thiết bị theo mã (không có thì trả None)
    def find_device(self,device_id):
        for i in self._devices:
            if i.device_id==device_id:
                return i
        return None
    # Thêm thiết bị: không None, không trùng mã
    def add_device(self,device):
        if device is not None and isinstance(device,Device):
            for i in self._devices:
                if i.device_id==device.device_id:
                    raise ValueError("Đã có thiết bị cần thêm trong phòng")
            self._devices.append(device)
        else:
            raise ValueError("thiết bị không để trống")
    # Xóa thiết bị theo mã (True nếu xóa được)
    def remove_device(self,device_id):
        if self.find_device(device_id) is not None:
            self._devices.remove(self.find_device(device_id))
            return True
        return False
    # Tổng chi phí bảo trì của phòng (đa hình)
    def calculate_annual_maintenance_cost(self):
        S=0
        for i in self._devices:
            S+=i.calculate_annual_maintenance_cost()
        return S
    # Thiết bị cần bảo trì: đang bảo trì hoặc dùng > 5 năm
    def get_devices_requiring_maintenance(self):
        result=[]
        for i in self._devices:
            if i.status==DeviceStatus.UNDER_MAINTENANCE or i.age>5:
                result.append(i)
        return result
    # Các đối tượng INetworkable trong phòng (máy tính và thành phần mạng của máy in)
    def get_networkable_devices(self):
        result=[]
        for i in self._devices:
            if isinstance(i,Computer):
                result.append(i)
            if isinstance(i,Printer) and i.network is not None:
                result.append(i.network)
        return result
    # Chuỗi mô tả phòng và các thiết bị
    def __str__(self):
        lines=[f"Phòng {self._room_id} - {self._name} ({len(self._devices)}/{self._capacity} thiết bị)"]
        for d in self._devices:
            lines.append(f"  - {d}")
        return "\n".join(lines)
