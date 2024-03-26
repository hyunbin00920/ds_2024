from stack.listStack import *

def palindrome_check(str) :
    st = ListStack()
    i = 0
    while (str[i] != '$') :
        st.push(str[i])
        i += 1
    i += 1
    if(st.size() * 2 + 1 == len(str)) :
        while (i < len(str)) :
            tmp = st.pop()
            if (tmp != str[i]) :
                return False
            i += 1
        return True
    else :
        return False

def main() :
    Input1 = "abc$cba"
    Input2 = "abc$abc"
    print("Input 1 :", Input1)
    print("IS_PALINDROME :", palindrome_check(Input1))
    print("Input 2 :", Input2)
    print("IS_PALINDROME :", palindrome_check(Input2))

if __name__ == "__main__" :
    main()
