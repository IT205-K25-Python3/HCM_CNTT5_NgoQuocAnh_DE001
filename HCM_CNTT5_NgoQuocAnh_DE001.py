employees = []


def calculate_total_income(basic_daily_wage, number_of_working_days, allowances):
    return (basic_daily_wage * number_of_working_days) + allowances


def classify_income(total_income):
    if total_income < 9000000:
        return "Thấp"
    elif total_income < 15000000:
        return "Trung bình"
    elif total_income < 30000000:
        return "Khá"
    else:
        return "Cao"


def find_employee_by_id(employee_id):
    for emp in employees:
        if emp["employee_id"] == employee_id:
            return emp
    return None


def is_duplicate_id(employee_id):
    return find_employee_by_id(employee_id) is not None


def input_float(prompt, min_val=None):
    while True:
        raw = input(prompt).strip()
        valid = True
        dot_count = 0
        if not raw:
            valid = False
        else:
            for i, ch in enumerate(raw):
                if ch == '.':
                    dot_count += 1
                    if dot_count > 1:
                        valid = False
                        break
                elif i == 0 and ch == '-':
                    valid = False
                    break
                elif not ch.isdigit() and ch != '.':
                    valid = False
                    break
        if not valid:
            print("Giá trị không hợp lệ")
            continue
        value = float(raw)
        if min_val is not None and value <= min_val:
            print(f"Giá trị phải lớn hơn {min_val}")
            continue
        return value


def input_int(prompt, min_val=1, max_val=31):
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print(f"Vui lòng nhập số nguyên từ {min_val} đến {max_val}")
            continue
        value = int(raw)
        if value < min_val or value > max_val:
            print(f"Giá trị phải từ {min_val} đến {max_val}")
            continue
        return value


def input_nonempty(prompt):
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Không được để trống")
            continue
        return raw


def print_line(width=55):
    print("-" * width)


def print_employee_block(emp):
    print_line()
    print(f"Mã NV: {emp['employee_id']}")
    print(f"Họ tên: {emp['full_name']}")
    print(f"Lương ngày: {emp['basic_daily_wage']}")
    print(f"Ngày công    : {emp['number_of_working_days']}")
    print(f"Phụ cấp: {emp['allowances']}")
    print(f"Tổng TN: {emp['total_income']}")
    print(f"Phân loại : {emp['income_classification']}")



def display_employee_list():
    print("\n" + "=" * 55)
    print("DANH SÁCH NHÂN VIÊN")
    print("=" * 55)

    if not employees:
        print("nhân viên trống")
        print("=" * 55)
        return

    for emp in employees:
        print_employee_block(emp)

    print_line()
    print(f"Tổng: {len(employees)} nhân viên")
    print("=" * 55)



def add_new_employee():
    print("\n" + "=" * 55)
    print("TIẾP NHẬN NHÂN VIÊN MỚI")
    print("=" * 55)

    while True:
        emp_id = input_nonempty("Mã nv(VD: NV001): ").upper()
        if is_duplicate_id(emp_id):
            print(f"Mã '{emp_id}' đã tồn tại")
        else:
            break

    full_name = input_nonempty("họ và tên: ")
    basic_daily_wage = input_float("lương ngày cơ bản (VND): ", min_val=0)
    number_of_working_days = input_int("số ngày công (1-31): ", 1, 31)
    allowances = input_float("tiền phụ cấp (VND): ", min_val=0)

    total_income= calculate_total_income(basic_daily_wage, number_of_working_days, allowances)
    income_classification = classify_income(total_income)

    employee = {
        "employee_id": emp_id,
        "full_name": full_name,
        "basic_daily_wage": basic_daily_wage,
        "number_of_working_days": number_of_working_days,
        "allowances": allowances,
        "total_income": total_income,
        "income_classification" : income_classification,
    }

    employees.append(employee)

    print(f"\nĐã thêm nhân viên '{full_name}' ({emp_id}) thành công!")
    print(f"Tổng thu nhập: {total_income}  \n  Phân loại: {income_classification}")
    print("=" * 55)



def update_information_and_working_days():
    print("\n" + "=" * 55)
    print("CẬP NHẬT THÔNG TIN NHÂN VIÊN")
    print("=" * 55)

    emp_id = input_nonempty("Nhập mã nhân viên cần cập nhật: ").upper()
    emp = find_employee_by_id(emp_id)

    if emp is None:
        print(f"Không tìm thấy nhân viên mã '{emp_id}'.")
        return

    print(f"\nThông tin hiện tại của '{emp['full_name']}':")
    print(f"Lương ngày: {emp['basic_daily_wage']}")
    print(f"Số ngày công : {emp['number_of_working_days']} ngày")
    print(f"Phụ cấp: {emp['allowances']}")
    print(f"Tổng thu nhập: {emp['total_income']}")
    print(f"Phân loại: {emp['income_classification']}")
    print()

    emp["basic_daily_wage"] = input_float("Lương ngày mới (VND): ", min_val=0)
    emp["number_of_working_days"] = input_int("Số ngày công mới (1-31): ", 1, 31)
    emp["allowances"] = input_float("Phụ cấp mới (VND): ", min_val=0)

    emp["total_income"] = calculate_total_income(
        emp["basic_daily_wage"],
        emp["number_of_working_days"],
        emp["allowances"]
    )
    emp["income_classification"] = classify_income(emp["total_income"])

    print(f"\nCập nhật thành công!")
    print(f"Tổng thu nhập mới: {emp['total_income']}  \n  Phân loại: {emp['income_classification']}")
    print("=" * 55)



def remove_employee():
    print("\n" + "=" * 55)
    print("XÓA NHÂN VIÊN")
    print("=" * 55)

    emp_id = input_nonempty("Nhập mã nhân viên cần xóa: ").upper()
    emp= find_employee_by_id(emp_id)

    if emp is None:
        print(f"Không tìm thấy nhân viên '{emp_id}'.")
        return

    print(f"\nNhân viên: {emp['full_name']} ({emp['employee_id']})")

    while True:
        confirm = input("có chắc chắn muốn xóa? (Y/N): ").strip().upper()
        if confirm == 'Y':
            employees.remove(emp)
            print(f"Đã xóa nhân viên '{emp['full_name']}'")
            break
        elif confirm == 'N':
            print("Hủy xóa.")
            break
        else:
            print("Vui lòng nhập Y hoặc N.")

    print("=" * 55)



def search_employee():
    print("\n" + "=" * 55)
    print("TÌM KIẾM NHÂN VIÊN")
    print("=" * 55)
    print("1. Tìm chính xác theo id")
    print("2. Tìm gần đúng theo full name")

    while True:
        mode = input("  Chọn (1/2): ").strip()
        if mode in ('1', '2'):
            break
        print("Vui lòng chọn 1 hoặc 2.")

    if mode == '1':
        emp_id = input_nonempty("Nhập mã nhân viên: ").upper()
        emp = find_employee_by_id(emp_id)
        results = [emp] if emp else []
    else:
        keyword = input_nonempty("Nhập tên cần tìm: ").lower()
        results = [e for e in employees if keyword in e["full_name"].lower()]

    if not results:
        print("Không tìm thấy nhân viên")
    else:
        print(f"\n Tìm thấy {len(results)} kết quả:")
        for emp in results:
            print_employee_block(emp)
        print_line()

    print("=" * 55)



def payroll_and_personnel_statistics():
    print("\n" + "=" * 55)
    print("THỐNG KÊ QUỸ LƯƠNG VÀ NHÂN SỰ")
    print("=" * 55)

    if not employees:
        print("trống nhân viên")
        print("=" * 55)
        return

    total_payroll = 0
    groups = {"Cao": [], "Khá": [], "Trung bình": [], "Thấp": []}

    for emp in employees:
        total_payroll += emp["total_income"]
        groups[emp["income_classification"]].append(emp)

    print(f"tổng số nhân viên : {len(employees)} người")
    print(f" Tổng quỹ lương: {total_payroll}")
    avg = total_payroll / len(employees)
    print(f"lương tb/người: {avg}")

    print()
    print("Phân loại thu nhập:")
    print_line()

    label_order = ["Cao", "Khá", "Trung bình", "Thấp"]
    ranges = {
        "Cao": ">= 30000000",
        "Khá": "15000000 - 29999999",
        "Trung bình": "9000000 - 14999999",
        "Thấp": "< 9000000",
    }

    for label in label_order:
        emps  = groups[label]
        count = len(emps)
        bar = "*" * count
        print(f" [{label}] ({ranges[label]})")
        print(f"Số lượng : {count} người{bar}")
        if emps:
            names = ", ".join(e["full_name"] for e in emps)
            print(f"Nhân viên: {names}")
        print()

    print("=" * 55)



def automatic_income_classification():
    print("\n" + "=" * 55)
    print("PHÂN LOẠI THU NHẬP TỰ ĐỘNG")
    print("=" * 55)

    if not employees:
        print("(trống nhân viên)")
        print("=" * 55)
        return

    updated_count = 0
    for emp in employees:
        new_total = calculate_total_income(emp["basic_daily_wage"],emp["number_of_working_days"],emp["allowances"])
        new_class = classify_income(new_total)

        changed = (new_total != emp["total_income"]) or (new_class != emp["income_classification"])

        emp["total_income"]= new_total
        emp["income_classification"] = new_class

        if changed:
            updated_count += 1
            print(f"{emp['employee_id']} - {emp['full_name']}: {new_total}  ->  {new_class}")

    if updated_count == 0:
        print("đã pphân loại")
    else:
        print(f"\nĐã cập nhật lại phân loại {updated_count} nhân viên")

    print("=" * 55)



def main():
    print("=" * 55)
    print("CHƯƠNG TRÌNH QUẢN LÝ NHÂN SỰ")
    print("=" * 55)

    while True:
        print("\n" + "-" * 40)
        print("1. Hiển thị danh sách nhân viên")
        print("2. Tiếp nhận nhân viên mới")
        print(" 3. Cập nhật thông tin và ngày công")
        print("4. Xóa nhân viên")
        print("5. Tìm kiếm nhân viên")
        print("6. Thống kê quỹ lương và nhân sự")
        print("7. Phân loại thu nhập tự động")
        print("8. Thoát chương trình")
        print("-" * 40)

        choice = input("Chọn chức năng: ").strip()

        match choice:
            case "1":
                display_employee_list()
            case "2":
                add_new_employee()
            case "3":
                update_information_and_working_days()
            case "4":
                remove_employee()
            case "5":
                search_employee()
            case "6":
                payroll_and_personnel_statistics()
            case "7":
                automatic_income_classification()
            case "8":
                print("\nCảm ơn tạm biệt!")
                break
            case _:
                print("lựa chọn không hợp lệ(1-8)")


if __name__ == "__main__":
    main()