import math
import time

inicioR = time.time()

p = [1,5,8,9,10,17,17,20,24,30] #Precios de la varilla
varilla1 = 4
varilla2 = 6
varilla3 = 10
varilla4 = 25

#Solucion recursiva
def cutRod(p,n): #p = precio de las varillas, y n = longitud de la misma
    if n == 0:
        return 0
    q = -(math.inf)
    for i in range(1, min(n, len(p)) + 1):
        q = max(q, p[i - 1] + cutRod(p, n - i))
    return q


print("Solucion recursiva con varilla 4: ", cutRod(p,varilla1))

finR = time.time()
print("Tiempo de ejecución recursivo", finR-inicioR, " segundos", "\n")
#Solución con programación dinamica

inicioDP = time.time()

memo = [-1] * (varilla4 + 1)
def cutRodDP(p,n,memo):
    
    if memo[n] == -1:
        if n == 0:
            memo[n] = 0
            return 0 
        q = -(math.inf)
        for i in range(1, min(n, len(p)) + 1):
            q = max(q, p[i -1] + cutRodDP(p, n - i, memo))
        memo[n] = q
    return memo[n]


print("Solución programación dinamica con varilla 1: ", cutRodDP(p,varilla1,memo))

finDP = time.time()

print("Tiempo de ejecución con programacion dinamica: ", finDP - inicioDP, "segundos","\n")

#Solucion bottom-up

inicioBU = time.time()

def cutRodBottomUp(p,n):
    
    dp = [0] * (n+1)
    
    for i in range(1,n+1):
        q = -(math.inf)
        
        for j in range(1, i + 1):
            if(j <= len(p)):
                q = max(q, p[j - 1] + dp[i - j])
            dp[i] = q
    
    return dp[n]


print("Solucion con Bottom Up con varilla 1: ", cutRodBottomUp(p,varilla1))

finBU = time.time()

print("Tiempo de ejecución con Bottom Up: ", finBU - inicioBU, "segundos", "\n")
