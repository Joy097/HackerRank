n = int(input().strip())
    

if n % 2!=0:
    print('Weird')
elif n % 2==0 and n>=2 and 5>=n:
    print('Not Weird')
elif n % 2==0 and 6<=n and 20>=n:
    print('Weird')
elif n % 2==0 and 20<=n:
    print('Not Weird')