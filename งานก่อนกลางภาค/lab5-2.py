
def prod(num):
    
    sum = 0
    
    for i in range(num):
        price = int(input("ราคาสินค้า %d : "% (i+1)))
        sum += price
    return sum

def tax(total):
    vat = (7/100)*total
    return vat

def change(money,netp):
    c = money - netp
    return c


n = int(input("จำนวนสินค้า : "))
total = prod(n)
print("ราคารวม %d"% total)
print("ภาษีมูลค่าเพิ่ม %d"% tax(total))
net = total + tax(total)
print("รวมเป็นเงิน %.2f"% net)
money = int(input("จำนวนเงินที่ได้รับ : "))
print(change(money,net))