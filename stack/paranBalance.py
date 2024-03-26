from stack.listStack import *

def paranBalance(str) :
    st = ListStack()
    for i in range(len(str)) :
        if (str[i] == "(" or str[i] == "{" or str[i] == "[") :
            st.push(str[i])
        elif (str[i] == ")" or str[i] == "}" or str[i] == "]") :
            if st.isEmpty() :
                return False
            st.pop()
    return st.isEmpty()

def main() :
    Input1 = "((800/(3+5)*2)"
    Input2 = "(82+2)/4)"
    Input3 = "(91*(40-35)+2)"
    print("Input 1 :", Input1)
    print("PARANBALANCE_CHECK :", paranBalance(Input1))
    print("Input 2 :", Input2)
    print("PARANBALANCE_CHECK :", paranBalance(Input2))
    print("Input 3 :", Input3)
    print("PARANBALANCE_CHECK :", paranBalance(Input3))

if __name__ == "__main__" :
    main()