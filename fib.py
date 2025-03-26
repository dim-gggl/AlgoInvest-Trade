def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(6))

# fib(5) + fib(4)
# fib(5) + fib(3) + fib(2)
# fib(5) + fib(3) + fib(1) + fib(0)
# fib(5) + fib(2) + fib(1) + fib(1) + fib(0)
# fib(5) + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
# fib(4) + fib(3)  + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
# fib(4) + fib(2) + fib(1)  + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
# fib(4) + fib(1) + fib(0)  + fib(1)  + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
# fib(3) + fib(2)  + fib(1) + fib(0)  + fib(1)  + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
# fib(3) + fib(1) + fib(0)  + fib(1) + fib(0)  + fib(1)  + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
# fib(2) + fib(1) + fib(1) + fib(0)  + fib(1) + fib(0)  + fib(1)  + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
# fib(1) + fib(0) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0)  + fib(1)  + fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
