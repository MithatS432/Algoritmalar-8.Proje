# Fibonacci sayıları - Memoization örneği
def fibonacci(n, memo={}):
    if n in memo:  # Daha önce hesaplandıysa direkt dön
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(10))  # Çıktı: 55


#Fibonacci İçin bu Kısım