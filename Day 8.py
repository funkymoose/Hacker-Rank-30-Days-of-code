# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
name = [input().split(" ") for i in range(0,n)]
d = {key:value for key,value in name}



while True:
    try:
        i = input()
        if i in d:
            print(f"{i}={d[i]}")
        else:
            print("Not found")
    except:
        break        
