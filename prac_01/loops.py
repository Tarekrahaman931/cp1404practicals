"""
Program to display various sequences and patterns using for loops.
"""

def main():
    print("Part a:")
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()

    print("Part b:")
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    print("Part c:")
    n = int(input("Number of stars: "))
    for _ in range(n):
        print('*', end='')
    print()

    print("Part d:")
    for i in range(1, n + 1):
        print('*' * i)
    print()

main()
