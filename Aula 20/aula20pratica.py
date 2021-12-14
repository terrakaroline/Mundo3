def exponenciacao(x,y):
    if (type(y)) != int:
        return -1
    else:
        expo = x**y
        return expo
    
    return 0

def fatorial(x):
    if (type(x)) == int and x >= 0:
        c = 1
        r = 1

        while c <= x:
            r *= c
            c += 1
        return r
    else:
        return -1

## Função para calcular o número de permutações de dois números Permutacao(n,p)=n!/(n-p)!,
# onde n é um número inteiro não negativo e p é um número inteiro e deve ser maior 
# ou igual a 0 e menor ou igual a n, caso contrário, a função deve retornar -1
# Dica: Use a função fatorial declarada acima.
# P(10,5)=30.240

def permutacao(n,p):
    if (type(n)) == int and n >= 0 and (type(p)) == int and p >= 0 and p <= n:
        result = fatorial(n) / fatorial(n - p)
        return result
    else:
        return -1
print(permutacao(10, 5))
print(permutacao(10, 20))
print(permutacao(-1, 0))
print(permutacao(2, -1))

## Função para calcular o número de combinações de dois números Combinacao(n,p)=n!/((n-p)! * p!),
# onde n é um número inteiro não negativo e p é um número inteiro e deve ser maior 
# ou igual a 0 e menor ou igual a n, caso contrário, a função deve retornar -1.
# Dica: Use a função fatorial declarada acima.
# C(10,5)=252
def combinacao(n,p):
    if (type(n)) == int and n > 0 and (type(p)) == int and p >= 0 and p <= n:
        result = fatorial(n) / ((fatorial(n - p) * fatorial(p)))
        return result
    else:
        return -1

print(combinacao(10, 5))
print(combinacao(2, -1))

def somatorio(i, f):
    if i > f:
        return 0
    elif i == f:
        return i
    else:
        c = i
        total = 0
        while c != (f + 1):
            c += 1
            total += i
            i += 1
        return(total)
print(somatorio(1,10))
print(somatorio(3, 10))
print(somatorio(10, 20))

## Função para calcular o número de Euler elevado a x (e^x ou expˆx), 
## onde x é um número real.
## A função deve calcular 100 termos da série:
## e^x = x^0/0!+x^1/1!+x^2/2!+x^3/3!+...
## Ex.: exp(1)==2,7182818285
## Ex.: exp(0)==1
## Ex.: exp(-1)==0,3678794412
def exp(x):
    y = 0
    tot = 0
    for i in range(100):
        tot += exponenciacao(x, y) / fatorial(y)
        y += 1
    return tot
print(exp(1))
print(exp(0))
print(exp(-1))

## Função para calcular o logaritmo neperiano (ln x ou log_e x)
## onde x é um real maior que zero.
## A função deve calcular 100 termos da série:
## ln x = 2*((x-1)/(x+1))*(  1/1*((x-1)/(x+1))^0 + 1/3*((x-1)/(x+1))^2 + 1/5*((x-1)/(x+1))^4 + ... )
## Ex.: ln(exp(x))==1
## Ex.: ln(1)==0
## Ex.: ln(2)==0,6931471806
## Ex.: ln(3)==1,0986122887
## Ex.: ln(10)==2,302585093
def ln(x):
    h = 0
    y = 1
    z = 0
    c = 0
    expo = 0
    for i in range(100):
        h = exponenciacao(1/1*(x-1)/(x+1),z)
        c += 2*((x-1)/(x+1))*(h)
        y += 2
        z += 2
    return c
print(ln(1))
print(ln(2))
print(ln(3))
print(ln(10))