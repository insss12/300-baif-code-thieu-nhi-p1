try:
    toan=int(input("enter diem toan"))
    van=int(input("enter diem van"))
    anh=int(input("enter diem anh"))
    tb=(toan+van+anh)/3
    if tb >= 8:
        print("hoc sinh gioi")
    elif tb < 8:
        print("hoc sinh bth")
    elif tb >=3:
        print("hoc sinh tb")
    elif tb < 3:
        print("hoc sinh da den")
except ValueError:
    print("invalid input")