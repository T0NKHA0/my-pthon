base = int(input("base : "))
height = int(input("height : "))

def triangle(base, height):
    area = 1/2*base*height
    #print("พื้นที่สามเหลี่ยม %.2f" % area)
    return area

#triangle(base, height)
print("พื้นที่สามเหลี่ยม %.2f" % triangle(base, height))