# * GC57 test contenitore chiave 2
from math import gcd,log
from random import randint, seed
import time
from gmpy2 import next_prime as nprime
from gmpy2 import is_prime as isprime

# **** imposto il seme di ricerca random
T=int(time.time())
seed(T)

# definisco il ciclo di ripetizione per entrambi i cicli inseriti
rip=10

# **** imposto due numeri primi
ps = 1019039871272183629436677933147
qs = 240877663362416822161232416951

# **** imposto gli esponenti
p=ps**8
q=qs**12

# **** Calcolo la chiave e l'intervallo
chiave = q-1
print("chiave Q-1 =",chiave)
campo = (chiave // (((p + 1) * (q + 1)) % chiave))*2
print("campo =", campo, " = ", " 2**", int(log(campo, 2)))
# **** Imposto variabili prograssione
v1=0
v2=1
# **** identifico il numero primo
for i in range(rip):
    trovato=0
    p_campo = randint(campo*v1, campo*v2)
    q_campo = randint(campo*v1, campo*v2)
    primo1 = nprime(p + p_campo)
    primo2=  nprime(q + q_campo)
    n=primo1*primo2
    for k in range(rip):
        r=gcd(n,(n%chiave)+chiave*k)
        if r!=1:
            print("---------------------------------------------------------------------")
            print()
            print("Test divisore 1: ", isprime(r))
            print("Test divisore 2: ", isprime(n//r))
            print("divisore       : ", r)
            print("contenitore k  : ",k)
            print("contenitore v1 : ",v1)
            print()
            print("Semiprimo analizzato: ",n)
            print()
            trovato=1
            break
    if trovato==0:
        print("attenzione: nessun divisore trovato per il contenitore :",v1)
        break
    v1+=1
    v2+=1
