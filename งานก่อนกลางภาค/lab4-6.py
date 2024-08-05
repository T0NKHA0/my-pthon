def circle(r):
    area = 22/7*(r**2)
    #print("พื้นที่สามเหลี่ยม %.2f" % area)
    return area

#triangle(base, height)
r = int(input("รัสมี : "))
print("พื้นที่วงกลม %.2f" % circle(r))