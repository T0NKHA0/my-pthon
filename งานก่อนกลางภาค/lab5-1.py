def avg(n):
    
    sum = 0
    
    for i in range(n):
        score = float(input("คะแนนที่ได้ : "))
        sum += score
    sum = sum/n
    return sum
        
n = int(input("จำนวนนักศึกษา : "))
print("คะแนนเฉลี่ย %.1f" % avg(n))