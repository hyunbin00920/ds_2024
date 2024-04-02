from Queue.listQueue import *

def isinSet(A) :
    q = ListQueue()

    if ('$' not in A) :
        return False
    
    check = False

    for i in range(len(A)) :
        if A[i] == '$' :
            check = True
        else :
            if not check :
                q.enqueue(A[i])
            else :
                if q.front() == A[i] :
                    q.dequeue()
                else :
                    return False

        
    if q.isEmpty() :
        return True
    else :
        return False
        
    
        
            

def main() :
    str1 = 'abc$abc'
    str2 = 'abc$cba'
    str3 = 'abc$abcd'
    str4 = 'abc$ab'
    str5 = 'abc$'
    str6 = 'abcabc'

    print("\ncase :", str1)
    print("str1 is in Set? :", isinSet(str1), '\n')

    print("case :", str2)
    print("str2 is in Set? :", isinSet(str2), '\n')

    print("case :", str3)
    print("str3 is in Set? :", isinSet(str3), '\n')

    print("case :", str4)
    print("str4 is in Set? :", isinSet(str4), '\n')

    print("case :", str5)
    print("str5 is in Set? :", isinSet(str5), '\n')

    print("case :", str6)
    print("str6 is in Set? :", isinSet(str6), '\n')    
        
if __name__ == "__main__" :
    main()