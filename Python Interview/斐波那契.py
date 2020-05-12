def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


# fibonacci=memo (fibonacci)
@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)


print(fib(6))


def fibonacciCache(n,cache=None):
    if cache is None:
        cache={}
    
    if n in cache:
        return cache[n]
 
    if(n<=2):
        return 1

    cache[n]=fibonacciCache(n - 1,cache) + fibonacciCache(n - 2,cache)

    return cache[n]