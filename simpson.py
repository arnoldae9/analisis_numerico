import numpy as np
 
def prod(A):
    a = 1
    for i in range(len(A)):
        a = a*A[i]
    return a
 
def lagrange(A,n):
    results = []
    lfun = np.arange((len(A[0]))**2,dtype=float)
    lfun.shape = (len(A[0]),len(A[0]))\
 
    for i in range(len(A[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:   lfun[i,j] = (n-A[0][j])/(A[0][i]-A[0][j])\
 
    for i in range(len(A[1])):
        results.append(prod(lfun[i])*A[1][i])\
 
    return sum(results)
 
def main():
    cantPoints = int(input("Ingrese cantidad de puntos conocidos> "))
 
    if cantPoints < 2:
        print ("\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n")
        main()\
 
    integs = []
    points = [[],[]]
    midPoints = [[],[]]\
 
    for i in range(cantPoints):
        print ("\n( x",i,",y",i,")")
        x = float(input("Ingrese 'x'> "))
        y = float(input("Ingrese 'y'> "))
        points[0].append(x)
        points[1].append(y)\
 
    for i in range(len(points[0])-1):
        midPoints[0].append((points[0][i+1]+points[0][i])/2)
        midPoints[1].append(lagrange(points,midPoints[0][i]))\
 
    for i in range(len(midPoints[0])):
        intg = ((points[0][i+1]-points[0][i])/6)*\
               (points[1][i]+(4*midPoints[1][i])+points[1][i+1])
        integs.append(intg)\
 
    print ("\n\tIntegral: ",sum(integs))
    input()
 
print ("\n\tREGLA DE SIMPSON\n\n")
main()