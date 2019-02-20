def rev(n):       
    list = []
    i = len(n) - 1
    while i >= 0:        
        list.append(n[i])
        i -= 1
    if list[0] == '0':
        list.pop(0)     
    new_number = ''.join(list[:])    
    return int(new_number)


def reverse(n):
    n = str(n)
    n1 = n.split('-')
    print(n1)
    if len(n1) > 1:        
        num = rev(n1[1])
        return -num
    else:
        return rev(n1[0])
        
print(reverse(123))
print(reverse(120))
print(reverse(-123)) 
    
