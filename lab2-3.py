weight = int(input("น้ำหนัก : "))
tall = int(input("ส่วนสูง : "))
BMI = round(weight/(tall/100)**2,2)
print(BMI)
if BMI < 18.50:
    print("น้ำหนักน้อย / ผอม")
elif BMI >= 18.50 and BMI <= 22.90:
    print("ปกติ (สุขภาพดี)")
elif BMI >= 23 and BMI <= 24.90:
    print("ท้วม / โรคอ้วนระดับ 1")
elif BMI >= 25 and BMI <= 30:
    print("อ้วน / โรคอ้วนระดับ 2")
elif BMI > 30:
    print("อ้วนมาก / โรคอ้วนระดับ 3")
