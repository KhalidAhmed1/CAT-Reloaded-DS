#swap case 
def swap_case(s):
    a=''
    for i in range(len(s)):
        if(0<len(s) and len(s)<=1000):
            if s[i].islower() :
                a+=s[i].capitalize()
            else:
                a+=s[i].lower()
    return a 
 
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

