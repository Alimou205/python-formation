print("veuillez svp saisir un entier")
x=int(input())
a=0
while(a<=20):
     resultat=a*x
     if(resultat %3 ==0):
          print(resultat,"*",end="")
     else:
          print(resultat,end="")
     a +=1
     
