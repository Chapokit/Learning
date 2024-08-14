s_id1 = input("First ID: ")
s_id2 = input("Second ID: ")
g1 = 2.8
g2 = 3.5
cp1 = "B"
cp2 = "B"
cal1_id1 = "C"
cal2_id1 = "C"
cal1_id2 = "A"
cal2_id2 = "A"

passed_grade = ['A','B','C']

id1 = True
id2 = True

if cp1 != "A" or cal1_id1 not in passed_grade or cal2_id1 not in passed_grade:
    id1 = False
if cp2 != "A"  or cal1_id2 not in passed_grade or cal2_id2 not in passed_grade:
    id2 = False

if id1 == True and id2 == True:
    if g1 > g2:
        id2 = False
        pass
    elif g2 > g1:
        id1 = False
        pass
    else:
        
        if passed_grade.index(cal1_id1) < passed_grade.index(cal1_id2):
            id2 = False
        elif passed_grade.index(cal1_id1) > passed_grade.index(cal1_id2):
            id1 = False
        else:
            pass

print(-4%3)



