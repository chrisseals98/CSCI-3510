import numpy as np
import string as st
from sympy import Matrix


originalArray = np.array([[9,5],[3,4]])
newArray = Matrix(originalArray)
invsymmatrix = newArray.inv_mod(26)
inverseModMatrix = np.array(invsymmatrix)
print (inverseModMatrix)

while(True):
    set = input("Next two letters: ")
    setArray = []
    for letter in set:
        setArray.append(st.ascii_lowercase.index(letter))
    
    print("\nNumbers: " + str(setArray))
    result = originalArray.dot(setArray)
    print("Before modulo: " + str(result))
    result %= 26
    print("After modulo: " + str(result))
    setBack = ""
    for index in result:
        setBack += st.ascii_lowercase[index]
    print("Back to string: " + setBack)
