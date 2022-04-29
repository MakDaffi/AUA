import numpy as np
from itertools import product

def get_set(a):
    s = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                s.append((i + 1, j + 1))
    return s


def subsets(n):
    nums = [i for i in range(n)]
    from functools import reduce
    return reduce(lambda res, x: res + [subset + [x] for subset in res],
                  nums, [[]])[1:]


def get_res(matrixes):
    res = []
    for subset in subsets(len(matrixes)):
        podres = matrixes[subset[0]]
        for index in subset[1:]:
            podres *= matrixes[index]
        for relation in get_set(podres):
            res.append(relation)
    return set(res)


def add_correlation(cur_word, alph, dct, semigroup_elems):
    new_words = []
    for letter in alph:
        new_word = cur_word + letter
        m = []
        for i in dct[cur_word]:
            if i != '*':
                m.append(dct[letter][semigroup_elems.index(i)])
            else:
                m.append('*')
        flag = True
        for key in dct:
            if m == dct[key]:
                print(new_word, '->', key)
                flag = False
        if flag:
            dct[new_word] = m
            new_words.append(new_word)
    return new_words


def find_correlation(ans):
    result = {}
    correlations = {}
    for key, value in ans.items():
        if not any(np.array_equal(value, i) for i in result.values()):
            result[key] = value
        else:
            for k, v in result.items():
                if np.array_equal(v, value):
                    correlations[key] = k
    print("Coopresentation: ")
    for key, value in result.items():
        print(key, ":\n", value)

    print("The resulting ratios: ")
    for key, value in correlations.items():
        print(key, "->", value)


def task1():
    print("Enter your set")
    st = list(input().split())
    print('Enter Cayley table')
    print("  ", *st)
    matrix = []
    for i in range(len(st)):
        print(st[i], end="  ")
        s = list(input().split())
        matrix.append(s)
    print("Enter your subset")
    subst = list(input().split())
    x_i = subst.copy()
    while True:
        x_l = []
        for x in x_i:
            for y in subst:
                x_l.append(matrix[st.index(x)][st.index(y)])
        x_0 = x_i.copy()
        x_0.sort()
        x_i = list(set(x_i).union(set(x_l)))
        x_i.sort()
        if x_0 == x_i:
            print('Subsemigroup is', *x_i)
            break


def task2():
    print("Enter the elements of the set: ")
    input_list = input().replace(",", "").split()
    n = len(input_list)
    print("Enter the number of binary relations")
    bin_relation_amount = int(input())
    bin_relation_matrices = {}
    for i in range(1, bin_relation_amount + 1):
        print(f"Enter boolean matrix Values {i} binary relation: ")
        print(" ", *input_list)
        matrix = [list(map(int, input(f"{input_list[i]} ").split())) for i in range(n)]
        matrix = np.array(matrix).reshape(n, n)
        bin_relation_matrices[str(i)] = matrix

    combinations_list = []
    for i in range(1, bin_relation_amount + 1):
        combinations = list(product(''.join([str(elem) for elem in range(1, bin_relation_amount + 1)]), repeat=i))
        combinations_list += combinations

    for comb in combinations_list:
        cur_matrix = bin_relation_matrices[comb[0]].copy()
        word = comb[0]
        for comb_i in range(1, len(comb)):
            cur_matrix *= bin_relation_matrices[comb[comb_i]]
            word += comb[comb_i]
        bin_relation_matrices[word] = cur_matrix

    find_correlation(bin_relation_matrices)


def task3():
    print("Enter semigroup elements: ")
    semigroup_elems = [elem for elem in input().replace(",", "").split()]
    print("Enter the elements of the transformation set: ")
    generators_list = input().replace(",", "").split()
    translation_dict = {}
    for i in range(len(generators_list)):
        print(f"Enter transformation values '{generators_list[i]}' elements of the semigroup, respectively: ")
        print((str(semigroup_elems)[1:-1]).replace(", ", " ").replace("'", ""))
        translation = input().split()
        translation_dict[generators_list[i]] = translation
    print("Coopresentation: ")
    gl = generators_list.copy()
    while gl:
        gl1 = []
        for s in gl:
            gl1.extend(add_correlation(s, generators_list, translation_dict, semigroup_elems))
        gl = gl1
    print("The resulting ratios: ")
    print(translation_dict)

if __name__ == "__main__":
    print("What are you want? (1 - Build subsemigroup by Cayley table, 2 - Build semigroup binary relations, 3 - Build semigroup by generating set and transformation set)")
    f = int(input())
    if f == 1:
        task1()
    elif f == 2:
        task2()
    elif f == 3:
        task3()
    else:
        print("Something going wrong! Enter a number from 1 to 3")