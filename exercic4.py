n=float(input("Entrez la valeur de n: "))
n1=n
n2=-n
while (n1-n2>0.001):
        if (((n2+n1)/2)*((n2+n1)/2))<n:
            n2=(n2+n1)/2
        else: 
            n1=(n1+n2)/2
print(str(n2)+ " et " +str(n1))
n=n1*n2
print(n)

