print('hello world')
print('commit from dev2 branch')
print('next change')
print('commit from dev1 branch and next change')
print('change from main branch')

def summ(a, b):
    """

    >>> summ(2, 3)
    5
    >>> summ(-3, 5)
    2
    """
    return a + b

if __name__ == '__main__':
    print(summ(1, 2))
