def solution(n):
    answer = 0
    if(n/7 > n//7):
        answer = n//7+1
    else:
        answer = n//7
    
    return answer

def solution(n):
    answer = 0
    for i in range(1,101):
        if((6*i) % n == 0):
            answer = i
            break
    
    return answer

def solution(slice, n):
    answer = 0
    print(n / slice)
    if(n / slice > n // slice ):
        answer = n // slice +1
    else:
        answer = n // slice
    return answer