
def score(sc,mt,et):
    
    sum_score = sc + mt + et
    return sum_score
    
def ev_score(total_score):
    if total_score > 80:
        return "ดีมาก"
    elif total_score > 50:
        return "ผ่าน"
    else:
        return "ไม่ผ่าน"
    
    
sc = int(input("คะแนนเก็บ : "))
mt = int(input("คะแนนสอบกลางภาค : "))
et = int(input("คะแนนสอบปลายภาค : "))

total_score = score(sc,mt,et)
ev = ev_score(total_score)

print("รวมคะแนนทั้งหมดเป็น %d คะแนน"% total_score)
print(ev)
        
        
    
    
    
    

