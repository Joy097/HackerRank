if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    s=[]   # avg nubmer list
    for i in student_marks:
        z=(student_marks[i][0]+student_marks[i][1]+student_marks[i][2])/3
        
        t = "{:.2f}".format(z)
 
        s.append(t)
    
    
    
    r=0   # names
    for i in student_marks:
        student_marks[i]=s[r]
        r+=1
    
    
    for i in student_marks:
        if i == query_name:
            print(student_marks[i])
        