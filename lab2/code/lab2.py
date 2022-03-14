from re import I, M
import numpy as np
import matplotlib.pyplot as plt


def isTran(a):
    n = len(a)
    b = np.matmul(a, a)
    for i in range(n):
        for j in range(n):
            if b[i][j]:
                b[i][j] = b[i][j] / b[i][j]
    f = (a >= b).all()
    if f:
        print("Set is transitive")
        return 't'
    else:
        f1 = True
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if a[i][k] and a[k][j] and a[i][j]:
                        f1 = False
        if f1:
            print("Set is anti-transitive")
            return 'at'
        else:
            print("Set is not transitive")
            return 'nt'


def isSymm(a):
    b = a.transpose()
    if np.array_equal(a, b):
        print("Set is symmetry")
        return 's'
    else:
        f = True
        b = np.multiply(a, b)
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j] != 0 and i != j:
                    f = False
                    break
        if f:
            print("Set is anti-symmetry")
            return 'as'
        else:
            print("Set is not symmetry")
            return 'ns'


def isRefl(a):
    n = len(a)
    sum = 0
    for i in range(n):
        sum += a[i][i]
    if sum == n:
        print("Set is reflexive")
        return 'r'
    elif sum == 0:
        print("Set is anti-reflexive")
        return 'ar'
    else:
        print("Set is not reflexive")
        return 'nr'


def makeRefl(a):
    n = len(a)
    for i in range(n):
        a[i][i] = 1


def makeSymm(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                a[j][i] = 1


def makeTran(a):
    n = len(a)
    for c in range(n):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if a[i][k] and a[k][j]:
                        a[i][j] = 1

def get_set(a):
    s = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                s.append((i + 1, j + 1))
    return s

def get_slices_list(relation_matrix, for_factor_set=1, attributes=None):
    slices = []
    for i in range(len(relation_matrix)):
        some_slice = [].copy()
        for j in range(len(relation_matrix[i])):
            if relation_matrix[i][j]:
                if attributes is None:
                    some_slice.append(j + for_factor_set)
                else:
                    some_slice.append(attributes[j])
        some_slice = tuple(some_slice)
        slices.append(some_slice)
    return slices


def create_factor_set(bin_relation):
    slices = get_slices_list(bin_relation)
    print("Factor set:")
    factor_set = set(slices)
    print(factor_set)
    return factor_set


def create_representative_system(factor_set):
    representative_system = []
    factor_set = list(factor_set)
    factor_set.sort(key=len)

    elem_dict = {}

    for eq_class in factor_set:
        for representative in eq_class:
            if not(representative in representative_system):
                elem_dict[f"{representative}"] = eq_class
                representative_system.append(representative)
                break

    print("Representative set factor system:")
    print(representative_system)
    ans = ""
    print("Where:", ans)
    for k, v in elem_dict.items():
       print(f"{k} \u2208 {list(v)}; ")


def get_dividers(num, set = None):
    i = 1
    ans = []
    if set == None:
        while(num >= i):
            if num % i == 0:
                ans.append(i)
            i += 1
    else:
        for s in set:
            if num % s == 0:
                ans.append(s)
    return ans


def get_level(a, dct):
    for an in a:
        m = 0
        for h in an:
            if m < dct[h]:
                m = dct[h]
        dct[an[len(an) - 1]] = m + 1
    return dct


def visualization(levels, max_level):
    plt.xlim(-1.0, max_level * 2)
    plt.ylim(0, len(levels) * 3 + 1.5)
    lvl = 1.5
    a = []
    for i in range(len(levels)):
        x = (max_level - len(levels[i]))
        l = 0
        b = []
        for j in range(len(levels[i])):
            plt.text(x + l, i + lvl, f'{levels[i][j]}')
            plt.scatter(x + l + 0.1, i + lvl + 0.15, s=350, facecolors='none', edgecolors='black')
            b.append((x + l, i + lvl, levels[i][j]))
            if i > 0:
                div = []
                for g in range(len(a) - 1, -1, -1):
                    for c in a[g]:
                        flag = True
                        for d in div:
                            if d % c[2] == 0:
                                flag = False
                        if levels[i][j] % c[2] == 0 and flag:
                            plt.plot([c[0] + 0.15, x + l + 0.15], [c[1] + 0.65, i + lvl - 0.45], color='black')
                            div.append(c[2])
            l += 2
        a.append(b)
        lvl += 2
    plt.show()


def get_max_elem(dct, st = [], is_matrix = False):
    if not(is_matrix):
        m = -10000000
        for key in dct:
            m = max(m, key)
        return m
    else:
        a = get_slices_list(dct)
        lst = [len(b) for b in a]
        l = max(lst)
        ans = []
        for i in range(len(lst)):
            if lst[i] == l:
                ans.append(st[i])
        return ans


def get_min_elem(dct, st = [], is_matrix = False):
    if not(is_matrix):
        m = 10000000
        for key in dct:
            m = min(m, key)
        return m
    else:
        a = get_slices_list(dct)
        print(a)
        lst = [len(b) for b in a]
        l = min(lst)
        ans = []
        for i in range(len(lst)):
            if lst[i] == l:
                ans.append(st[i])
        return ans


def get_smallest_element(dct, st =[], is_matrix = False):
    if not(is_matrix):
        m = 10000000
        for key in dct:
            m = min(m, key)
        cnt = 0
        for key in dct:
            if key == m:
                cnt += 1
        if cnt == 1:
            return m
        else:
            return None
    else:
        ans = get_min_elem(dct, st, is_matrix)
        if len(ans) == 1:
            return ans[0]
        else:
            return None


def get_largest_element(dct, st = [], is_matrix = False):
    if not(is_matrix):
        m = -1000000
        for key in dct:
            m = max(m, key)
        cnt = 0
        for key in dct:
            if key == m:
                cnt += 1
        if cnt == 1:
            return m
        else:
            return None
    else:
        ans = get_max_elem(dct, st, is_matrix)
        if len(ans) == 1:
            return ans[0]
        else:
            return None


def task1():
    print("How you want enter your relation (set or matrix)?")
    enter = input()
    if enter == 'set':
        print('Enter the number of elements in relation')
        n = int(input())
        print("Enter your set")
        # st = [(1, 3), (3, 4), (1, 4), (2, 5), (5, 3)]
        s = list(map(str, input().split(' ')))
        st = []
        for c in s:
            a = ''
            i = 1
            while c[i] != ',':
                a += c[i]
                i += 1
            i += 1
            b = ''
            while c[i] != ')':
                b += c[i]
                i += 1
            st.append((int(a), int(b)))
        a = np.zeros((n, n), int)
        for s in st:
            a[s[0] - 1][s[1] - 1] = 1
        print('-----------------------------------------')
        print("Relation's matrix")
        print(a)
    else:
        print('Enter the number of elements in relation')
        n = int(input())
        print("Enter your matrix")
        a = [list(map(int, input().split())) for i in range(n)]
        a = np.array(a).reshape(n, n)
        print('-----------------------------------------')
        print("Relation's set")
        print(*get_set(a))
    print('-----------------------------------------')
    properties = {"reflexive": isRefl(a), "symmetry": isSymm(a), "transitive": isTran(a)}
    print('-----------------------------------------')
    if properties['reflexive'] == 'r' and properties['symmetry'] == 's' and properties['transitive'] == 't':
        print('Relation is equivalent')
        print('-----------------------------------------')
    if properties['reflexive'] == 'r' and properties['transitive'] == 't':
        print('Relation is the relation of the quasi-order')
        print('-----------------------------------------')
    if properties['reflexive'] == 'r' and properties['symmetry'] == 'as' and properties['transitive'] == 't':
        print('Relation is the relation of the partial order')
        print('-----------------------------------------')
    if properties['reflexive'] == 'ar' and properties['symmetry'] == 'as' and properties['transitive'] == 't':
        print('Relation is the relation of the strict order')
        print('-----------------------------------------')
    if properties['reflexive'] != 'r':
        makeRefl(a)
    if properties['symmetry'] != 's':
        makeSymm(a)
    makeTran(a)
    print('Closure matrix: ')
    print(a)
    print('-----------------------------------------')
    print('Closure set: ')
    print(*get_set(a))
    print('-----------------------------------------')

    factor_set = create_factor_set(a)
    create_representative_system(factor_set)


def get_level_matrix(matrix, st):
    dct = {st[i]: 0 for i in range(len(st))}
    i = 1
    matrix = np.array(matrix, int)
    while(matrix.any()):
        m = get_min_elem(matrix, st=st, is_matrix=True)
        for elem in m:
            dct[elem] = i
            matrix = np.delete(matrix, [st.index(elem)], 0)
            matrix = np.delete(matrix, [st.index(elem)], 1)
            st.remove(elem)
        print(matrix)
        i += 1
    return dct


def task2():
    print("The relation of divisibility on a set or on a number or matrix")
    h = input()
    if h == "number":
        print('Enter your number')
        num = int(input())
        dividers = get_dividers(num)
        print(f'Dividers of {num} : {dividers}')
        print(f"Maximum element is {get_max_elem(dividers)}")
        print(f"Minimum element is {get_min_elem(dividers)}")
        print(f"The smallest element is {get_smallest_element(dividers)}")
        print(f"The largest element is {get_largest_element(dividers)}")
        a = [get_dividers(div) for div in dividers]
        print(a)
        dct = {dividers[i]: 0 for i in range(len(a))}
        dct = get_level(a, dct)
    elif h == "set":
        print('Enter your set')
        st = list(map(int, input().split()))
        print(f"Maximum element is {get_max_elem(st)}")
        print(f"Minimum element is {get_min_elem(st)}")
        ls = get_smallest_element(st)
        bs = get_largest_element(st)
        if ls:
            print(f"The smallest element is {ls}")
        else:
            print("The smallest element doesn't exist")
        if bs:
            print(f"The largest element is {bs}")
        else:
            print("The largest element doesn't exist")
        st = list(set(st))
        a = [get_dividers(div, set=st) for div in st]
        dct = {st[i]: 0 for i in range(len(a))}
        dct = get_level(a, dct)
    else:
        print('Enter your set')
        st = list(map(int, input().split()))
        st = list(set(st))
        print("Enter your matrix")
        print("  ", *st)
        matrix = []
        a = []
        for i in range(len(st)):
            print(st[i], end="  ")
            b = []
            s = list(map(int, input().split()))
            for i in range(len(s)):
                if s[i]:
                    b.append(st[i])
            a.append(b)
            matrix.append(s)
        print(f"Maximum element is {get_max_elem(matrix, st=st, is_matrix=True)}")
        print(f"Minimum element is {get_min_elem(matrix, st=st, is_matrix=True)}")
        ls = get_smallest_element(matrix, st=st, is_matrix=True)
        bs = get_largest_element(matrix, st=st, is_matrix=True)
        if ls:
            print(f"The smallest element is {ls}")
        else:
            print("The smallest element doesn't exist")
        if bs:
            print(f"The largest element is {bs}")
        else:
            print("The largest element doesn't exist")
        dct = get_level_matrix(matrix, st)
    last_level = 1
    for key in dct:
        last_level = max(dct[key], last_level) 
    print(dct)
    levels = [[] for _ in range(last_level)]
    for key in dct:
        levels[dct[key] - 1].append(key)
    max_level = 1
    for lvl in levels:
        max_level = max(max_level, len(lvl))
    visualization(levels, max_level)


def task3():
    print("Enter your set:")
    st = list(map(int, input().split()))
    print("Enter your context:")
    context = list(input().split())
    print("Enter your matrix")
    print("  ", *context)
    matrix = []
    for i in range(len(st)):
        print(st[i], end="  ")
        s = list(map(int, input().split()))
        matrix.append(s)
    matrix = np.array(matrix)
    dct = {}
    for i in range(len(context)):
        dct[tuple(context[i])] = matrix[:, i]
    dct1 = {}
    dct2 = dct
    for i in range(len(st)):
        for key in dct:
            for k in dct2:
                a = np.multiply(dct2[k], dct[key])
                cnt = 0
                for c in a:
                    cnt += c
                if cnt and key != k:
                    g = list(key)
                    g.extend(list(k))
                    g.sort()
                    dct1[tuple(set(g))] = a
                elif cnt:
                    dct1[tuple(key)] = a
        dct2 = dct1.copy()
    dl = []
    for key in dct1:
        for k in dct1:
            if np.array_equal(dct1[key],dct1[k]):
                if len(key) > len(k):
                    dl.append(k)
                elif len(key) < len(k):
                    dl.append(key)
    dl = list(set(dl))
    for d in dl:
        del dct1[d]
    for key in dct1:
        b = dct1[key]
        a = []
        for i in range(len(b)):
            if b[i]:
                a.append(st[i])
            dct1[key] = a
    print(dct1)


if __name__ == "__main__":
    print("What are you want? (1 - Create factor set, 2 - Build Hasse diagram, 3 - build lattice concept)")
    f = int(input())
    if f == 1:
        task1()
    elif f == 2:
        task2()
    elif f == 3:
        task3()
    else:
        print("Something going wrong! Enter a number from 1 to 3")

