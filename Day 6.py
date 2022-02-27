# Enter your code here. Read input from STDIN. Print output to STDOUT

num = int(input())
sl = []
for i in range(0,num):
    s = input()
    s0 = ""
    s1 = ""
    for j in range(0,len(s)):
        
        if j%2 == 0:
            s0 += s[j]
        else:
            s1 += s[j]
    sl.append(s0+" "+s1) 
for i in sl:
    print(i)
