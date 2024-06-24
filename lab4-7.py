def BMI(w, h):
    bmi = w/(h/100)**2
    return bmi

def n(bmi):
    if bmi < 18.50:
        return "น้ำหนักน้อย / ผอม"
    elif bmi >= 18.50 and bmi <= 22.90:
        return "ปกติ (สุขภาพดี)"
    elif bmi >= 23 and bmi <= 24.90:
        return "ท้วม / โรคอ้วนระดับ 1"
    elif bmi >= 25 and bmi <= 30:
        return "อ้วน / โรคอ้วนระดับ 2"
    elif bmi > 30:
        return "อ้วนมาก / โรคอ้วนระดับ 3"

w = float(input("น้ำหนัก : "))
h = float(input("ส่วนสูง : "))

bmi = BMI(w, h)
result = n(bmi)

print("ค่า BMI คือ %.2f" % BMI(w, h))
print(result)
