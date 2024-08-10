
def merge_array(l1,l2):
    main_list = l1 + l2
  
    return sorted(main_list)
    

l1 = [1,2,3,5]
l2 = [4,7,1]
print(merge_array(l1,l2))