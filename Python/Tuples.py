#import builtins
if __name__ == '__main__':
    n = int(input())
    values = input()
    list = values.split(" ")
    a=0
    for i in list:
        list[a]=int(i)
        a+=1
    t = tuple(list)
    print(hash(t))
    
    