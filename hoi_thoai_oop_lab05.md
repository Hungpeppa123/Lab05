# Hội thoại: Bài thực hành OOP — Hệ thống quản lý thiết bị và hợp đồng bảo trì

- **Sinh viên:** Nguyễn Đức Hưng — HUST, Khoa Toán – Tin
- **Học phần:** Lập trình hướng đối tượng (MI-OOP) — GV Vũ Thành Nam
- **Ngày:** 11/10/2026
- **Ngôn ngữ cài đặt:** Python (đề bài viết theo C#)

> Ghi chú: những chỗ người dùng gửi ảnh được mô tả trong ngoặc vuông `[...]`.

---

## 1. Tóm tắt đề bài

**Hỏi:** Tóm tắt những gì tôi phải làm trong file này. *[đính kèm đề lab_w05a.pdf]*

**Đáp:**

Bạn phải viết một chương trình gồm **5 phần code**, **2 câu trả lời lý thuyết** và **1 hàm main để kiểm thử**.

**Phần 1 – Lớp trừu tượng `Device`**
- Thuộc tính: mã, tên, năm sử dụng, giá mua, trạng thái (`Active` / `UnderMaintenance` / `Retired`).
- Kiểm tra dữ liệu: mã không rỗng; giá > 0; năm sử dụng ≤ năm hiện tại.
- Mã chỉ đọc: chỉ gán được lúc khởi tạo.
- Phương thức trừu tượng: tính chi phí bảo trì một năm.
- Ghi đè hàm in chuỗi (`__str__` trong Python).

**Phần 2 – Ba lớp con kế thừa `Device`**

| Lớp | Thuộc tính thêm | Chi phí bảo trì |
|---|---|---|
| Computer | RAM, CPU, có GPU rời | 5% giá + 2% nếu có GPU + 1% nếu dùng trên 5 năm |
| Printer | loại (laser/phun), số trang, hỗ trợ mạng | 4% giá + 500k nếu in trên 100.000 trang + 300k nếu máy in màu |
| Projector | lumen, giờ dùng bóng đèn | 3% giá + 1,5 triệu nếu bóng đèn dùng trên 3.000 giờ |

⚠️ Bẫy: Printer tính phí theo "máy in màu" nhưng đề không cho thuộc tính màu → phải tự thêm `is_color` và giải thích.

**Phần 3 – Interface `INetworkable`**
- Thành phần: `ip_address`, `connect(ip)`, `disconnect()`, `is_connected`.
- Quy tắc: IP không rỗng; không kết nối lại khi đang kết nối; sau khi ngắt `is_connected = False` và xóa IP.
- Computer bắt buộc thực thi. Với máy in, chọn 1 trong 2 cách (lớp con `NetworkPrinter` hoặc thành phần `NetworkConnection` kết tập) và viết 3–5 câu trade-off.

**Phần 4 – Lớp `LabRoom` (kết tập)**
- Thuộc tính: mã phòng, tên, sức chứa, danh sách thiết bị.
- `add_device` (từ chối `None`, từ chối trùng mã), `remove_device`, `find_device`.
- `calculate_annual_maintenance_cost`: dùng **đa hình**, không `isinstance`.
- `get_devices_requiring_maintenance`: thiết bị `UnderMaintenance` **hoặc** dùng trên 5 năm.

**Phần 5 – Câu hỏi lý thuyết:** LabRoom – Device là kết tập hay hợp thành? (giải thích theo vòng đời)

**Phần 6 – Hàm main kiểm thử:** 2 máy tính (1 có GPU), 2 máy in (1 in trên 100k trang), 1 máy chiếu (bóng đèn trên 3.000 giờ), 2 phòng; chạy 7 thao tác (thêm, thử trùng mã, in danh sách, tính tổng chi phí, liệt kê cần bảo trì, kết nối mạng, duyệt qua kiểu `INetworkable`).

**Đổi từ C# sang Python**

| C# | Python |
|---|---|
| `abstract class` | `from abc import ABC, abstractmethod` |
| `enum` | `from enum import Enum` |
| `interface` | lớp `ABC` chỉ chứa `@abstractmethod` |
| `{ get; }` | `@property` không có setter |
| `decimal` | `Decimal` (hoặc `float`) |
| `null` | `None` |

---

## 2. Tạo khung báo cáo LaTeX

**Hỏi:** Tạo cho tôi 1 file LaTeX theo khung này. *[ảnh yêu cầu nộp: link GitHub, phân tích nghiệp vụ, danh sách lớp & sơ đồ, kết quả chạy, vì sao Device là lớp trừu tượng, vì sao INetworkable là interface, đa hình thể hiện ở đâu]* — *Sau đó bổ sung:* "Tôi chỉ cần bạn tạo khung thôi, còn lại để tôi tự làm."

**Đáp:** Đã tạo file `bao_cao_lab_w05a.tex` (biên dịch thử không lỗi):
- Trang bìa điền sẵn tên, MSSV, giảng viên.
- 7 mục theo khung; mục phân tích nghiệp vụ có thêm 3 tiểu mục: thuộc tính tự bổ sung, trade-off phương án máy in mạng, LabRoom–Device là kết tập hay hợp thành.
- Chỗ cần điền đánh dấu `% TODO`.
- **Phải biên dịch bằng XeLaTeX** (Overleaf: Menu → Compiler → XeLaTeX).

---

## 3. Bài giảng 7 kiến thức OOP (ví dụ bãi gửi xe)

**Hỏi:** Dạy tôi các kiến thức này để hoàn thành bài tập bằng Python: kế thừa, lớp trừu tượng, interface, kết tập, đa hình, kiểm tra dữ liệu, giải thích quan hệ.

**Đáp:** Ví dụ xuyên suốt: **bãi gửi xe** — cấu trúc giống hệt bài thiết bị.

### 0. Lớp và đối tượng
```python
class Car:
    def __init__(self, plate, seats):     # hàm khởi tạo
        self.plate = plate                # self = chính đối tượng
        self.seats = seats

    def describe(self):
        return f"Xe {self.plate}, {self.seats} chỗ"

c = Car("30A-123", 5)                     # không có từ khóa new
```

### 1. Kế thừa — quan hệ "là một"
```python
class Car(Vehicle):
    def __init__(self, plate, owner, year, seats):
        super().__init__(plate, owner, year)     # gọi __init__ lớp cha
        self.seats = seats
```
Kiểm tra: câu "B là một A" phải đúng. Trong bài: Computer/Printer/Projector "là một" Device.

### 2. Lớp trừu tượng
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def calculate_fee(self, hours):
        pass

class Bicycle(Vehicle):
    def calculate_fee(self, hours):
        return 2000
```
Tạo `Vehicle(...)` → lỗi *Can't instantiate abstract class…*. Device là lớp trừu tượng vì có dữ liệu chung nhưng chi phí bảo trì phụ thuộc loại thiết bị, và "thiết bị chung chung" không có ý nghĩa thực tế.

### 3. Kiểm tra dữ liệu & đóng gói
```python
from datetime import date

def __init__(self, plate, owner, year):
    if not plate or not plate.strip():
        raise ValueError("Biển số không được rỗng")
    if year > date.today().year:
        raise ValueError("Năm sản xuất không hợp lệ")
    self._plate = plate

@property
def plate(self):
    return self._plate     # chỉ đọc; gán c.plate = "X" -> AttributeError
```
Enum cho trạng thái:
```python
from enum import Enum
class VehicleStatus(Enum):
    PARKED = "Đang gửi"
    LEFT = "Đã lấy xe"
```

### 4. Interface — năng lực độc lập cây kế thừa
```python
class IChargeable(ABC):
    @abstractmethod
    def charge(self, kwh): pass

    @property
    @abstractmethod
    def is_charging(self): pass

class ElectricCar(Car, IChargeable):
    ...
```
INetworkable là interface vì kết nối mạng là năng lực "cắt ngang" cây kế thừa: có thiết bị có, có thiết bị không.

### 5. Kết tập — quan hệ "có"
```python
class ParkingLot:
    def __init__(self, name):
        self.name = name
        self._vehicles = []

    def add_vehicle(self, vehicle):
        if vehicle is None:
            raise ValueError("Xe không được None")
        if self.find_vehicle(vehicle.plate) is not None:
            raise ValueError("Biển số đã có trong bãi")
        self._vehicles.append(vehicle)

    def find_vehicle(self, plate):
        for v in self._vehicles:
            if v.plate == plate:
                return v
        return None
```

### 6. Đa hình
```python
# ❌ SAI
for v in vehicles:
    if isinstance(v, Car): ...
    elif isinstance(v, Bicycle): ...

# ✅ ĐÚNG
def total_fee(self, hours):
    return sum(v.calculate_fee(hours) for v in self._vehicles)
```
Đa hình qua interface: `if isinstance(v, IChargeable): v.charge(30)` — kiểm tra năng lực, không kiểm tra lớp cụ thể.

Trong bài, đa hình thể hiện ở: (1) ghi đè `calculate_maintenance_cost`; (2) ghi đè `__str__`; (3) duyệt thiết bị qua kiểu `INetworkable`.

### 7. Cách quyết định quan hệ

| Câu kiểm tra | Quan hệ | Python |
|---|---|---|
| "B là một A" | Kế thừa | `class B(A)` |
| "B có thể làm X" (chỉ một số B) | Thực thi interface | `class B(A, IX)` |
| "A có/chứa nhiều B" | Kết tập | `self._items = []` |

**Bản đồ áp dụng:** Vehicle → Device; Bicycle/Car → Computer/Printer/Projector; VehicleStatus → DeviceStatus; IChargeable → INetworkable; ParkingLot → LabRoom; `calculate_fee` → `calculate_maintenance_cost`.

**Thứ tự làm:** Device + DeviceStatus → 3 lớp con → INetworkable → LabRoom → main.py.

---

## 4. Mục "Quy tắc nghiệp vụ và ràng buộc dữ liệu"

**Hỏi:** Ở mục này tôi nên nói về những gì?

**Đáp:** Chia 3 nhóm.

**Nhóm 1 – Ràng buộc dữ liệu (thuộc tính hợp lệ):**
- Bắt buộc: mã không rỗng; giá > 0; năm ≤ năm hiện tại; mã chỉ gán khi khởi tạo; trạng thái chỉ 3 giá trị.
- Nên bổ sung: RAM > 0; số trang ≥ 0; giờ bóng đèn ≥ 0; lumen > 0; loại máy in chỉ laser/phun; mã phòng không rỗng, sức chứa > 0.

**Nhóm 2 – Quy tắc nghiệp vụ (hành xử khi thao tác):**
- Phòng: không thêm `None`; không trùng mã trong một phòng; thiết bị tồn tại được khi không thuộc phòng nào; xóa thiết bị không có → trả `False`.
- Bảo trì: công thức theo loại; "cần bảo trì" = UnderMaintenance hoặc > 5 năm; tổng chi phí bằng đa hình.
- Mạng: IP không rỗng; không kết nối lại; ngắt → `is_connected = False`, xóa IP; chỉ thiết bị có năng lực mạng mới kết nối được.

**Nhóm 3 – Giả định tự đặt:** cách tính "trên 5 năm"; thiết bị có được ở 2 phòng không; sức chứa là chỗ ngồi hay số thiết bị; thiết bị Retired có tính chi phí không.

**Trình bày:** bảng 3 cột *Quy tắc – Kiểm tra tại – Xử lý khi vi phạm*. Mỗi dòng = một câu `if ... raise` trong code.

---

## 5. Trade-off là gì

**Hỏi:** Tôi chọn NetworkPrinter kế thừa Printer và thực thi INetworkable. Viết 3–5 câu trade-off là sao?

**Đáp:** Trade-off là **sự đánh đổi**. Đoạn văn phải trả lời: **Chọn gì? Được gì? Mất gì / vì sao chấp nhận?**

Khung câu:
> (1) Nhóm chọn phương án … vì … (2) Ưu điểm là … (3) Ngoài ra … (4) Đổi lại, nhược điểm là … (5) Tuy nhiên trong phạm vi bài toán …, nhược điểm này chấp nhận được.

---

## 6. Kết tập là gì

**Hỏi:** Kết tập là gì?

**Đáp:** Quan hệ **"có/chứa"** trong đó **thành phần tồn tại độc lập** với đối tượng chứa (lớp học – sinh viên, đội bóng – cầu thủ).

| | Kết tập | Hợp thành |
|---|---|---|
| Thành phần tạo ở đâu | Bên ngoài, truyền vào | Bên trong đối tượng chứa |
| Đối tượng chứa bị xóa | Thành phần vẫn còn | Thành phần mất theo |
| Dùng chung | Được | Không |
| UML | ◇ thoi rỗng | ◆ thoi đặc |

Mẹo: thành phần **truyền vào qua tham số** → kết tập; **tạo mới trong `__init__`** → hợp thành.

---

## 7. Kết tập vs kế thừa cho khả năng mạng

**Hỏi:** Kết tập phức tạp hơn NetworkPrinter đúng không? Nhưng sau này thêm thuộc tính khác thì không cần tạo nhiều lớp con?

**Đáp:** Đúng — nhưng nên nói "thêm **năng lực**" (mạng, scan, Wi-Fi), không phải "thuộc tính" (như `color`).
- **Kết tập phức tạp hơn:** phải kiểm tra `None`; gọi vòng `printer.network.connect(...)`; không dùng `isinstance(d, INetworkable)` trực tiếp được.
- **Kết tập linh hoạt hơn:** không bùng nổ lớp con (2 năng lực → 3 lớp con, 3 năng lực → 7); gắn/tháo khi chạy; tái sử dụng `NetworkConnection`.
- Nguyên tắc: **"ưu tiên kết tập/hợp thành hơn kế thừa"** (*favor composition over inheritance*).

---

## 8. Ví dụ code kết tập: Đội bóng – Cầu thủ

**Hỏi:** Ví dụ 1 đoạn code về kết tập để tôi hiểu sâu hơn.

**Đáp:**
```python
class Player:
    def __init__(self, player_id, name):
        if not player_id:
            raise ValueError("Mã cầu thủ không được rỗng")
        self._player_id = player_id
        self.name = name

    @property
    def player_id(self):
        return self._player_id

    def __str__(self):
        return f"{self._player_id} - {self.name}"


class Team:
    def __init__(self, name):
        self.name = name
        self._players = []

    def add_player(self, player):
        if player is None:
            raise ValueError("Không thêm cầu thủ None")
        if self.find_player(player.player_id) is not None:
            raise ValueError(f"Cầu thủ {player.player_id} đã có trong đội")
        self._players.append(player)

    def remove_player(self, player_id):
        p = self.find_player(player_id)
        if p is None:
            return False
        self._players.remove(p)
        return True

    def find_player(self, player_id):
        for p in self._players:
            if p.player_id == player_id:
                return p
        return None

    def show(self):
        print(f"Đội {self.name}:")
        for p in self._players:
            print("   ", p)


an = Player("P01", "An"); binh = Player("P02", "Bình"); chi = Player("P03", "Chi")
team_a = Team("Bách Khoa"); team_a.add_player(an); team_a.add_player(binh)
team_b = Team("Đội tuyển HN"); team_b.add_player(an); team_b.add_player(chi)
an.name = "An (đội trưởng)"        # cả 2 đội đều thấy
team_a.remove_player("P02")         # Bình vẫn tồn tại
del team_a                          # An vẫn tồn tại
```

4 điểm cần hiểu:
1. Thành phần có trước đối tượng chứa.
2. Danh sách chỉ lưu **tham chiếu**, không lưu bản sao → một cầu thủ có thể ở 2 đội; sửa một nơi, mọi nơi thấy.
3. Gỡ khỏi đội ≠ xóa đối tượng.
4. Xóa đội không xóa cầu thủ.

---

## 9. Đối chiếu ví dụ với bài

**Hỏi:** Team tương đương Printer, Player như các loại máy in có khả năng khác nhau đúng không?

**Đáp:** Chưa đúng. Có hai chỗ kết tập khác nhau:

| | Đối tượng chứa | Thành phần |
|---|---|---|
| LabRoom – Device (đề bắt buộc) | LabRoom (≈ Team) | Device (≈ Player) |
| Kết tập mạng | Printer | NetworkConnection (card mạng) |

Với phương án kết tập, chỉ có **một lớp Printer**; "có mạng hay không" là có gắn thành phần `NetworkConnection` hay không. "Các loại máy in có khả năng khác nhau" là tư duy **kế thừa**.

---

## 10. `class Printer(Device)` nghĩa là gì

**Hỏi:** Tại sao class Printer lại có `(Device)`?

**Đáp:** Đó là **cú pháp kế thừa** (C#: `class Printer : Device`). Nhờ đó Printer:
1. Thừa hưởng thuộc tính, kiểm tra dữ liệu, phương thức chung của Device.
2. Bị bắt buộc viết `calculate_maintenance_cost()`.
3. Được đối xử như một Device (thêm vào LabRoom, đa hình).

Bỏ `(Device)` → phải viết lại mọi thứ và mất quan hệ kế thừa.

**Hỏi tiếp:** Thuộc tính của Device được Printer kế thừa, thuộc tính khác thì Printer tự `self` vào đúng không?

**Đáp:** Đúng, nhưng thuộc tính của Device **chỉ được tạo khi gọi `super().__init__(...)`**. Phương thức thì kế thừa tự động.

**Hỏi tiếp:** Vậy trong `__init__` vẫn phải liệt kê lại thuộc tính của Device?

**Đáp:** Liệt kê lại ở **tham số** (để nhận dữ liệu), nhưng **không** gán `self.` và kiểm tra lại — chuyển tiếp lên Device:
```python
def __init__(self, device_id, name, year, price, pages, is_color):
    super().__init__(device_id, name, year, price)   # Device tự gán + kiểm tra
    self.pages = pages
    self.is_color = is_color
```

---

## 11. Đổi sang phương án kết tập cho máy in

**Hỏi:** Tôi chọn phương án kết tập vì sau này thêm khả năng (màu, scan…) không phải tạo nhiều lớp con.

**Đáp:** Hợp lệ, cần chỉnh 2 chỗ:
1. Kết tập là **gắn thêm thành phần**, không phải "thừa lại": `Printer(..., network=NetworkConnection())`.
2. "Màu" là **thuộc tính**, không phải năng lực; ví dụ năng lực đúng là scan, fax, Wi-Fi.

Hệ quả: `NetworkConnection` thực thi INetworkable; bước kiểm thử 7 cần cách duyệt không phụ thuộc lớp cụ thể — gợi ý thêm `get_network()` vào Device (mặc định `None`, Computer trả về chính nó, Printer trả về thành phần mạng).

---

## 12. Nhược điểm của phương án kết tập

**Hỏi:** Giải thích về mất mát của phương án này.

**Đáp:**
1. **Gọi vòng:** `printer.network.connect(...)` thay vì `printer.connect(...)`.
2. **Phải kiểm tra `None`** khắp nơi, quên là lỗi `AttributeError: 'NoneType' object has no attribute 'connect'`.
3. **Kiểu đối tượng không cho biết năng lực:** `isinstance(printer, INetworkable)` luôn `False`.
4. **Nguy cơ dùng chung một thành phần:** gắn cùng một card cho 2 máy in → trạng thái mạng bị chia sẻ.

Câu gợi ý cho báo cáo:
> Đổi lại, thiết kế trở nên phức tạp hơn: phải truy cập khả năng mạng gián tiếp qua thành phần, phải kiểm tra `None` trước khi sử dụng, và không thể nhận biết thiết bị có khả năng mạng chỉ bằng kiểu đối tượng.

---

## 13. Vì sao 2 máy in không được dùng chung trạng thái mạng

**Hỏi:** Tại sao 2 máy in không được dùng chung trạng thái mạng?

**Đáp:** Mỗi máy in là một máy vật lý có card mạng và IP riêng. Nếu dùng chung:
- Máy chưa kết nối lại báo đã kết nối và **trùng IP**.
- Máy thứ hai **không kết nối được** (bị chặn bởi quy tắc "không kết nối lại").
- Ngắt máy này thì máy kia cũng mất mạng.

So với đội bóng: cầu thủ An ở 2 đội là **cùng một người** → dùng chung đúng; 1 card cho 2 máy in là **2 card khác nhau** → sai. Kết tập *cho phép* dùng chung nhưng không phải lúc nào cũng *nên*.

---

## 14. So sánh kết tập và hợp thành

**Hỏi:** So sánh kết tập và hợp thành.

**Đáp:**

| Tiêu chí | Kết tập | Hợp thành |
|---|---|---|
| Ràng buộc | Yếu | Mạnh |
| Tạo thành phần | Bên ngoài, truyền vào | Bên trong |
| Tồn tại trước | Có | Không |
| Xóa đối tượng chứa | Thành phần còn | Thành phần mất |
| Chuyển chỗ | Được | Không |
| UML | ◇ rỗng | ◆ đặc |
| Ví dụ | Phòng – thiết bị | Nhà – phòng, Hóa đơn – dòng hàng |

3 câu hỏi quyết định: thành phần có nghĩa khi đứng một mình? chuyển sang chủ khác được? xóa chủ thì thành phần có nên mất theo?

Áp dụng: LabRoom – Device là **kết tập**. Printer – NetworkConnection: card được tạo bên ngoài, truyền vào, có thể tháo/lắp → **kết tập**, nhưng tại mỗi thời điểm chỉ gắn vào một thiết bị.

**Hỏi tiếp:** Tôi chọn LabRoom – Device là kết tập vì thiết bị không ở trong phòng vẫn tồn tại.

**Đáp:** Đúng. Viết theo 3 mốc vòng đời: **trước** (thiết bị tạo trước khi thuộc phòng), **trong** (chuyển phòng được), **sau** (xóa phòng, thiết bị vẫn còn). Thêm câu nối với code: thiết bị khởi tạo bên ngoài rồi truyền vào qua `add_device()`, LabRoom chỉ lưu tham chiếu. Lưu ý diễn đạt hợp thành đúng: thành phần **do đối tượng chứa tạo ra và bị hủy theo**.

---

## 15. Trạng thái Retired

**Hỏi:** Retired trong trường hợp này là loại bỏ?

**Đáp:** Là **ngừng sử dụng / thanh lý**, không phải xóa.

| | Đổi sang Retired | Xóa / gỡ khỏi phòng |
|---|---|---|
| Đối tượng còn không | Còn | Không còn trong danh sách |
| Code | `device.status = DeviceStatus.RETIRED` | `room.remove_device("PC01")` |
| Mục đích | Giữ hồ sơ tài sản | Thiết bị không còn liên quan |

Cần tự quyết định và ghi vào giả định: có tính chi phí bảo trì cho Retired không; thiết bị Retired dùng > 5 năm có nằm trong danh sách "cần bảo trì" không.

---

## 16. Kiểm tra bảng danh sách lớp

**Hỏi:** Kiểm tra bảng danh sách lớp. *[ảnh bảng: DeviceStatus, Device, Computer, Printer, Projector, INetworkable, LabRoom]*

**Đáp:**
1. **Thiếu lớp `NetworkConnection`.**
2. **Printer chưa khớp phương án:** thay "có hỗ trợ mạng" bằng thành phần `network`; thêm `is_color`.
3. **Computer thiếu "thực thi INetworkable".**
4. Cột vai trò thiếu phương thức (Device: kiểm tra dữ liệu, phương thức trừu tượng, `__str__`; lớp con: ghi đè chi phí; INetworkable: 4 thành phần; LabRoom: các phương thức, ghi rõ kết tập).
5. Chính tả: "tên biết bị" → thiết bị; "độ sang" → sáng; "Undermaintenance" → UnderMaintenance; "dịa chỉ Ip" → địa chỉ IP; "ram" → RAM.
6. Caption bảng bị lặp khi sang trang → dùng `\endfirsthead` và `\endhead`.

**Hỏi tiếp:** *[ảnh lỗi LaTeX ở dòng NetworkConnection]* Bị sao?

**Đáp:** Dòng cuối bảng **thiếu `\\`** trước `\bottomrule`. Ngoài ra dấu `_` trong bảng phải viết `\_` hoặc bọc `\texttt{}`.

---

## 17. Sơ đồ lớp

**Hỏi:** Sơ đồ lớp gồm Device, 3 lớp thiết bị, LabRoom, NetworkConnection đúng không?

**Đáp:** Thiếu **INetworkable** (`«interface»`) và **DeviceStatus** (`«enumeration»`). Tổng 8 thành phần.

| Quan hệ | Từ → Đến | Ký hiệu |
|---|---|---|
| Kế thừa | Computer, Printer, Projector → Device | Nét liền, tam giác rỗng |
| Thực thi | Computer, NetworkConnection → INetworkable | Nét đứt, tam giác rỗng |
| Kết tập | LabRoom ◇── Device | Thoi rỗng phía LabRoom |
| Kết tập | Printer ◇── NetworkConnection | Thoi rỗng phía Printer |
| Liên kết | Device ── DeviceStatus | Nét liền |

Bội số: LabRoom `0..1` – Device `0..*`; Printer – NetworkConnection `0..1`. `-` private, `+` public; phương thức trừu tượng in nghiêng; lớp con chỉ ghi thuộc tính riêng. Công cụ: draw.io.

**Hỏi:** Interface chỉ có method chứ không có property phải không?

**Đáp:** Interface không có **thuộc tính lưu dữ liệu**, nhưng **có thể khai báo property** (`ip_address`, `is_connected` dạng `{readOnly}`). Lớp thực thi mới có thuộc tính lưu dữ liệu thật (`- _ip_address: str`).

---

## 18. Kiểu dữ liệu của các thuộc tính Device

**Hỏi:** Năm đưa vào sử dụng nên để là gì? Trạng thái là string phải không?

**Đáp:**

| Thuộc tính | Kiểu | UML |
|---|---|---|
| Mã thiết bị | `str` | `- _device_id: str` |
| Tên | `str` | `- _name: str` |
| Năm đưa vào sử dụng | `int` | `- _year_in_use: int` |
| Giá mua | `float` / `Decimal` | `- _purchase_price: float` |
| Trạng thái | **`DeviceStatus`** (không phải `str`) | `- _status: DeviceStatus` |

- Năm: so với `date.today().year`, không viết cứng 2026. Thêm property `years_used`.
- Trạng thái dùng Enum vì chỉ có đúng 3 giá trị hợp lệ; gõ sai sẽ báo lỗi ngay. Chuỗi `"Đang hoạt động"` chỉ là giá trị hiển thị (`.value`).

---

## 19. Phương thức của Device

**Hỏi:** Method của Device là tạo đối tượng, tính chi phí bảo trì trừu tượng và biểu diễn thông tin?

**Đáp:** Đúng 3 cái chính, bổ sung thêm:

| Phương thức | UML |
|---|---|
| Khởi tạo | `+ __init__(device_id, name, year_in_use, purchase_price)` |
| Tính chi phí (trừu tượng, in nghiêng) | `+ calculate_maintenance_cost(): float` |
| Biểu diễn | `+ __str__(): str` |
| Property đọc | `device_id {readOnly}`, `name`, `year_in_use`, `purchase_price`, `status` |
| Setter trạng thái | `status` |
| Số năm đã dùng | `+ years_used: int {readOnly}` |
| Lấy thành phần mạng (tùy chọn) | `+ get_network(): INetworkable` |

---

## 20. NetworkConnection

**Hỏi:** NetworkConnection có những thuộc tính và method gì?

**Đáp:**
- Thuộc tính: chỉ `- _ip_address: str` (None khi chưa kết nối). Không lưu thêm `_is_connected` vì sẽ mâu thuẫn.
- `__init__()`: gán `_ip_address = None`.
- `ip_address` (property): trả `_ip_address`.
- `is_connected` (property): `return self._ip_address is not None`.
- `connect(ip)`: kiểm tra IP không rỗng, chưa đang kết nối, rồi gán.
- `disconnect()`: gán `_ip_address = None`.

```
           NetworkConnection
─────────────────────────────────────
- _ip_address: str
─────────────────────────────────────
+ __init__()
+ ip_address: str {readOnly}
+ is_connected: bool {readOnly}
+ connect(ip_address: str)
+ disconnect()
```

**Hỏi:** Sao nó giống INetworkable thế?

**Đáp:** Giống **tên** (vì thực thi interface phải có đủ thành phần), khác **nội dung**: interface chỉ khai báo (thân `pass`, không dữ liệu, không tạo đối tượng được); NetworkConnection có dữ liệu và code thật. INetworkable là **bản hợp đồng**, NetworkConnection là **người thực hiện**. Cần interface vì nhiều lớp cùng thực thi và code bên ngoài chỉ cần biết kiểu INetworkable (bước kiểm thử 7).

**Hỏi:** Tại sao NetworkConnection cần sửa như vậy?

**Đáp:**
1. `- _ip_address` private → đóng gói, buộc phải đi qua `connect()` có kiểm tra.
2. `+ ip_address {readOnly}` → thực thi đủ interface; đọc được nhưng không sửa được.
3. `is_connected {readOnly}` là property suy ra từ IP → đảm bảo tự động "sau khi ngắt trả về false".

---

## 21. Review sơ đồ lớp

**Hỏi:** Kiểm tra thành phần. *[ảnh sơ đồ draw.io — lần 1, 2, 3]*

**Đáp (tổng hợp các lần review):**
- ✅ Đã đúng: kết tập LabRoom ◇── Device, Printer ◇── NetworkConnection; thực thi nét đứt tam giác rỗng; `«interface»`, `«enumeration»`; mũi tên kế thừa tam giác rỗng (sau khi sửa); DeviceStatus hết lặp.
- DeviceStatus không cần method — chỉ có tên và danh sách giá trị.
- Còn cần sửa:
  - Bội số `0..1` / `0..*` trên đường kết tập.
  - Device: `«abstract»`, in nghiêng; `demacial` → `decimal`; `Devicestatus()` → `DeviceStatus`; `toString()` → `__str__()`.
  - Mọi thuộc tính `+` → `-`.
  - Printer: `- _network: NetworkConnection`.
  - LabRoom: `IReadOnlyList<Device>` → `+ devices: list[Device] {readOnly}`; `remove_device(device_id: str): bool`; `find_device(...): Device`.
  - NetworkConnection: `IpAdress` → `- _ip_address: str`; thêm property `{readOnly}`.
  - INetworkable: xóa khai báo trùng ở ngăn trên; đổi `Connect(string IpAddress)` → `connect(ip_address: str)`.
  - Thống nhất kiểu đặt tên Python (`snake_case`, `str`, `float`).

**Hỏi:** Computer mấy lỗi đó là sao?

**Đáp:** `IsConnected` không nên lưu riêng (suy ra từ IP); thuộc tính phải private; cần property theo interface. Hai cách: **A** – Computer tự lưu `- _ip_address`; **B** – Computer chứa `- _network: NetworkConnection`.

**Hỏi:** Tôi không dùng cách B.

**Đáp:** Dùng **cách A**:
```
              Computer
─────────────────────────────────────
- _ram_gb: int
- _processor_type: str
- _has_dedicated_gpu: bool
- _ip_address: str
─────────────────────────────────────
+ ip_address: str {readOnly}
+ is_connected: bool {readOnly}
+ connect(ip_address: str)
+ disconnect()
+ calculate_maintenance_cost(): float
```
Giữ nét đứt tới INetworkable, không nối với NetworkConnection. Computer phải tự viết đủ 3 quy tắc kết nối; trong trade-off ghi nhược điểm "logic kết nối bị lặp giữa Computer và NetworkConnection".

---

## 22. Vì sao INetworkable phải kế thừa ABC

**Hỏi:** Tại sao class INetworkable phải kế thừa ABC trong Python?

**Đáp:** Python không có từ khóa `interface`; không kế thừa ABC thì `@abstractmethod` **không có tác dụng**.

Kết quả chạy thử:
```
=== KHÔNG kế thừa ABC ===
Tạo được cả 2, không báo lỗi
pc.connect(...) trả về: None

=== CÓ kế thừa ABC ===
Lỗi: Can't instantiate abstract class INetworkable without an implementation for abstract method 'connect'
Lỗi: Can't instantiate abstract class BadPC2 without an implementation for abstract method 'connect'
```

ABC đảm bảo: (1) không tạo đối tượng từ interface; (2) lớp thực thi quên method → báo lỗi ngay. Trong Python, lớp trừu tượng và interface viết giống nhau (cùng kế thừa ABC); khác ở cách dùng: lớp trừu tượng có dữ liệu và code chung, interface chỉ có phương thức trừu tượng.

---

## 23. `def connect(self, ip): pass`

**Hỏi:** `def connect(self, ip): pass` là sao? Giải thích kĩ.

**Đáp:**

| Phần | Ý nghĩa |
|---|---|
| `@abstractmethod` | Lớp con bắt buộc viết lại |
| `def` | Khai báo hàm/phương thức |
| `connect` | Tên phương thức |
| `self` | Chính đối tượng gọi (`pc.connect(...)` → `self` là `pc`) |
| `ip` | Tham số IP truyền vào |
| `:` | Bắt đầu thân |
| `pass` | Câu lệnh "không làm gì" — giữ chỗ vì Python bắt buộc thân có ít nhất 1 lệnh |

Tương đương C#: `void Connect(string ipAddress);`. Có thể thay `pass` bằng docstring mô tả.

**Hỏi:** Nghĩa là nó định hình phương thức connect thôi, còn connect thế nào thì lớp con tự viết?

**Đáp:** Đúng. Lớp con phải giữ đúng tên + tham số, và không được bỏ qua (ABC báo lỗi).

**Hỏi:** Các lớp dùng phương thức này là Computer và NetworkConnection?

**Đáp:** Đúng. Printer không có `connect()` — gọi qua thành phần `printer.network.connect(ip)`; Projector không có.

**Hỏi:** Phương thức này trong Computer khác gì NetworkConnection?

**Đáp:** Logic gần như giống hệt (3 kiểm tra). Khác ở nơi lưu dữ liệu và cách gọi (`pc.connect(...)` vs `printer.network.connect(...)`; `self` là máy tính vs card mạng). Có thể khác thêm nếu Computer kiểm tra trạng thái của chính nó, ví dụ không cho kết nối khi `RETIRED` (tùy chọn, ghi vào giả định).

---

## 24. Xuất hội thoại

**Hỏi:** Làm sao để xuất ra?

**Đáp:** Claude không xuất riêng từng cuộc trò chuyện; cách chính thức là xuất toàn bộ dữ liệu: bấm chữ cái tên ở góc dưới trái → **Settings** → **Privacy** → **Export data** → nhận link qua email (chỉ trên web/desktop, link hết hạn sau 24 giờ). Nguồn: [Export your Claude data](https://support.claude.com/en/articles/9450526-how-can-i-export-my-claude-data).
