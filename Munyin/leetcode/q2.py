def rev_list(l):
    
    l.reverse()
    num = ''.join(map(str, l))
    print(num)
    return int(num)

def add_num(l1,l2):
    
    n1 = rev_list(l1)
    n2 = rev_list(l2)

    numsum = n1 + n2
    numsum_str = str(numsum)
    l = [int(digit) for digit in numsum_str]

    l.reverse()
    
    answer = ''.join(map(str, l))
    list_answer = [int(digit) for digit in answer]
    return list_answer


l1 = [2,4,3]
l2 = [5,6,4]
print(add_num(l1,l2))