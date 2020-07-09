def getNorm(vector):
    return ("{0:.2f}").format((int(vector[0])**2+int(vector[1])**2+int(vector[2])**2)**(1/2))

vectorA = input("Enter vector A:\n").split()
vectorB = input("Enter vector B:\n").split()

print('A+B =',[int(vectorA[0])+int(vectorB[0]),int(vectorA[1])+int(vectorB[1]),int(vectorA[2])+int(vectorB[2])])
print('A.B =',int(vectorA[0])*int(vectorB[0]) + int(vectorA[1])*int(vectorB[1]) + int(vectorA[2])*int(vectorB[2]))
print('|A| =',getNorm(vectorA))
print('|B| =',getNorm(vectorB))