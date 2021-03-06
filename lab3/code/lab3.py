import numpy as np


def get_set(a):
    s = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                s.append((i + 1, j + 1))
    return s


def get_matrix(st, n):
    a = np.zeros((n, n), int)
    for s in st:
        a[s[0] - 1][s[1] - 1] = 1
    return a


def inversion(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                a[i][j] = 0
            else: a[i][j] = 1
    print(a)
    print(*get_set(a))


def dis(a):
    n = len(a)
    print("Enter second matrix")
    b = [list(map(int, input().split())) for _ in range(n)]
    c = get_set(a)
    c.extend(get_set(b))
    c = list(set(c))
    print(get_matrix(c, n))
    print(c)


def con(a):
    n = len(a)
    print("Enter second matrix")
    b = [list(map(int, input().split())) for _ in range(n)]
    a = np.array(a, int)
    b = np.array(b, int)
    c = a * b
    print(c)
    print(get_set(c))


def reverse(a):
    a = np.array(a, int)
    b = a.T
    print(b)
    print(*get_set(b))

def composition(a):
    n = len(a)
    print("Enter second matrix")
    b = [list(map(int, input().split())) for _ in range(len(a[0]))]
    c = np.zeros((n, len(b[0])), int)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                for g in range(len(b[j])):
                    if b[j][g] == 1:
                        c[i][g] = 1
    print(c)
    print(get_set(c))

def task2():
    print('Enter the number of elements in relation')
    n = int(input())
    print("Enter your matrix")
    a = [list(map(int, input().split())) for _ in range(n)]
    print('What are you want to do with this binary relation?\n 1.Disjunction with another binary relation\n 2.Conjunction with another binary relation\n 3.Inversion binary relation\n 4.Reverse binary relation\n 5.Composition with another binary relation')
    d = int(input())
    if d == 1:
        dis(a)
    elif d == 2:
        con(a)
    elif d == 3:
        inversion(a)
    elif d == 4:
        reverse(a)
    elif d == 5:
        composition(a)

def task3():
    print('Enter len of your matrix')
    n = int(input())
    print("Enter your matrix")
    a = np.array([list(map(int, input().split())) for _ in range(n)])
    print('What are you want to do with this matrix?\n 1.Transpose matrix\n 2.Add matrix\n 3.Subtract matrix\n 4.Multiply by a constant\n 5.Multiply matrix\n 6.Find inverse matrix')
    d = int(input())
    if d == 1:
        print(a.T)
    elif d == 4:
        print('Enter your constant')
        h = float(input())
        print(h * a)
    elif d == 6:
            print(np.linalg.inv(a))
    else:
        print("Enter another matrix")
        if d == 5:
            n1 = len(a[0])
        else: n1 = n
        b = np.array([list(map(int, input().split())) for _ in range(n1)])
        if d == 2:
            print(a + b)
        elif d == 3:
            print(a - b)
        elif d == 5:
            print(np.dot(a, b))


def isAssociative(matrix, st):
    flag = True
    for i in range(len(st)):
        st1 = [matrix[i][j] for j in range(len(st))]
        matrix1 = np.zeros((len(st), len(st)), int)
        for j in range(len(st)):
            for g in range(len(st)):
                matrix1[j][g] = matrix[j][st.index(st1[g])]
        st2 = [matrix[j][i] for j in range(len(st))]
        matrix2 = np.zeros((len(st), len(st)), int)
        for j in range(len(st)):
            for g in range(len(st)):
                matrix2[j][g] = matrix[st.index(st2[j])][g]
        flag = (matrix1 == matrix2).all()
        if not(flag):
            break
    if flag:
        print('This operation is associative!')
    else:
        print('This operation is not associative!')


def isCommutative(matrix):
    matrix1 = matrix.T
    if (matrix1 == matrix).all():
        print('This operation is commutative!')
    else:
        print('This operation is not commutative!')


def isIdempotent(matrix, st):
    flag = True
    for i in range(len(matrix)):
        if not(matrix[i][i] == st[i]):
            flag = False
            break
    if flag:
        print('This operation is idempotent!')
    else:
        print('This operation is not idempotent!')


def isReversible(matrix, st):
    rev = []
    for i in range(len(st)):
        flag = True
        for j in range(len(st)):
            if not(matrix[i][j] == matrix[j][i] == 1):
                flag = False
                break
        if flag:
            rev.append(st[i])
    if rev:
        print(f'Reverse elements of the operation: {rev}')
    else:
        print('This operation is not reversible!')


def isDistributive(matrix, st):
    print('Enter Cayley table for another operation')
    print("  ", *st)
    matrix1 = []
    for i in range(len(st)):
        print(st[i], end="  ")
        s = list(map(int, input().split()))
        matrix1.append(s)
    matrix1 = np.array(matrix1)
    flag = True
    for i in range(len(st)):
        for j in range(len(st)):
            for g in range(len(st)):
                if not(matrix[i][st.index(matrix1[j][g])] ==
                matrix1[st.index(matrix[i][j])][st.index(matrix[i][g])]
                and matrix[st.index(matrix1[j][g])][i] ==
                matrix1[st.index(matrix[j][i])][st.index(matrix[g][i])]):
                    flag = False
                    break
    if flag:
        print('This operation is distributive with respect to the introduced operation!')
    else:
        print('This operation is not distributive with respect to the introduced operation!')


def task1():
    print("Enter your set")
    st = list(map(int, input().split()))
    print('Enter Cayley table')
    print("  ", *st)
    matrix = []
    for i in range(len(st)):
        print(st[i], end="  ")
        s = list(map(int, input().split()))
        matrix.append(s)
    matrix = np.array(matrix)
    isAssociative(matrix, st)
    isCommutative(matrix)
    isIdempotent(matrix, st)
    isReversible(matrix, st)
    isDistributive(matrix, st)


def task4(lambda_digit=2):
    st = [1, 2, 3, 4]
    matrix = np.array([[1, 2, 1, 2],
                             [1, 2, 1, 2],
                             [1, 2, 3, 4],
                             [1, 2, 3, 4]])
    print("Task 1:")
    isAssociative(matrix, st)
    matrix_a = np.array([[1, -2], [-3, lambda_digit]])
    koef = lambda_digit / 2
    print("Task 2:")
    print(np.matmul(matrix_a, matrix_a) + (10 - koef) * matrix_a + koef * np.ones((2, 2)))
    matrix_a = np.array([[-1, lambda_digit, 3], [lambda_digit / 3, 2, 8 - lambda_digit / 3]])
    matrix_b = np.array([[-lambda_digit, 2], [1, 10 - lambda_digit / 2], [-3, lambda_digit]])
    print("Task 3:")
    print(np.dot(matrix_a, matrix_b))



if __name__ == "__main__":
    print("What are you want? (1 - Checking properties of a binary operation, 2 - Perform an operation on a binary relation, 3 - Perform an operation on a matrix, 4 - Check tasks)")
    f = int(input())
    if f == 1:
        task1()
    elif f == 2:
        task2()
    elif f == 3:
        task3()
    elif f == 4:
        task4()
    else:
        print("Something going wrong! Enter a number from 1 to 3")