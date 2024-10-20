s = input("Enter any string: ")
l = ""
max_len = 0
n = 0
while n < len(s):
    m = n + 1
    while m <= len(s):
        substr = ""
        revstr = ""     
        
        i = n
        while i < m:
            substr += s[i]
            i += 1

        i = m - 1
        while i >= n:
            revstr += s[i]
            i -= 1
        
        if substr == revstr and len(substr) > max_len:
            l = substr
            max_len = len(substr)
        
        m += 1
    n += 1

print("Longest palindromic string :", l)