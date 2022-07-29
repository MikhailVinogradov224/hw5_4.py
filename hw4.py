def do_this(string):
    func = ""  
    i = 0
    while i < len(string):       
        count = 1 
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count = count + 1
            i = i + 1
 
        
        func += str(count) + string[i]
        i = i + 1 
    return func
if __name__ == '__main__':
 
    string = 'AAAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCCCCCDDDDDDDDCAAAAEEEFGGGG'
    print(do_this(string))