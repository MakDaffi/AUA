import numpy as np

order = []
component = []

def check_associative(set_list, a):
  n = len(set_list)
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if a[i][set_list.index(str(a[j][k]))] != \
          a[set_list.index(str(a[i][j]))][k]:
          return False
  return True

def dfs(graph, used, v):
    used[v] = True
    for i in range(len(graph)):
        to = i
        if (not(used[to]) and graph[v][to]):
            dfs(graph, used, to)
    order.append(v)


def dfs2(graph, used, v):
    used[v] = True
    component.append(v)
    for i in range(len(graph)):
        to = i
        if (not(used[to]) and graph[v][to]):
            dfs2(graph, used, to)


def find_ideals(st, cayley_table):
    right_ideal = [set(i) for i in cayley_table]
    left_ideal = []
    for i in range(len(cayley_table)):
        s = set()
        for j in range(len(cayley_table)):
            s.add(cayley_table[j][i])
        left_ideal.append(s)
    full_ideal = []
    for i in range(len(cayley_table)):
        full_ideal.append(right_ideal[i].union(left_ideal[i]))
        print(f'Right ideal {st[i]} : {right_ideal[i]}')
        print(f'Left ideal {st[i]} : {left_ideal[i]}')
        print(f'Full ideal {st[i]} : {full_ideal[i]}')
    return right_ideal, left_ideal, full_ideal


def build_green_relation(right_ideal, left_ideal):
    mr = []
    for i in range(len(right_ideal)):
        m = []
        for j in range(len(right_ideal)):
            if right_ideal[i] == right_ideal[j]:
                m.append(1)
            else:
                m.append(0)
        mr.append(m)
    ml = []
    for i in range(len(left_ideal)):
        m = []
        for j in range(len(left_ideal)):
            m.append(int(left_ideal[i] == left_ideal[j]))
        ml.append(m)
    mr = np.array(mr)
    ml = np.array(ml)
    green_realtion = mr + ml
    for i in range(len(green_realtion)):
        for j in range(len(green_realtion)):
            if green_realtion[i][j] > 1:
                green_realtion[i][j] = 1
    print("Green relation: ")
    print(green_realtion)
    return green_realtion


def gen_cayley_table(set_list, presentation):
    semigroup = set_list.copy()
    while True:
        new_elements = []
        for el1 in semigroup:
            for el2 in semigroup:
                new_word = el1 + el2
                while True:
                    tmp = str(new_word)
                    for key, val in presentation.items():
                        if key in new_word:
                            new_word = new_word.replace(key, val)
                    if tmp == new_word:
                        break
                new_elements.append(new_word)
        check_semgr = set(semigroup.copy())
        for el in new_elements:
            if el not in semigroup:
                semigroup.append(el)
        if check_semgr == set(semigroup):
            break

    cayley_table = []
    for i in range(len(semigroup)):
        t = []
        for j in range(len(semigroup)):
            new_word = semigroup[i] + semigroup[j]
            while True:
                tmp = str(new_word)
                for key, val in presentation.items():
                    if key in new_word:
                        new_word = new_word.replace(key, val)
                if tmp == new_word:
                    break
            t.append(new_word)
        cayley_table.append(t)

    print("Semigroup:")
    print(*semigroup)
    print("Cayley table: ")
    print(cayley_table)
    return semigroup, cayley_table


def task1():
    print("Enter your set")
    st = input().split()
    print('Enter Cayley table')
    print("  ", *st)
    cayley_table = [input(f'{i}  ').split() for i in st]
    if check_associative(st, cayley_table):
        find_ideals(st, cayley_table)
    else:
        print('Your Cayley table is not associative!')


def task2():
    print("Enter your set")
    st = input().split()
    print('Enter Cayley table')
    print("  ", *st)
    cayley_table = [input(f'{i}  ').split() for i in st]
    if check_associative(st, cayley_table):
        right_ideal, left_ideal, _ = find_ideals(st, cayley_table)
        build_green_relation(right_ideal, left_ideal)
    else:
        print('Your Cayley table is not associative!')


def task3():
    print('Enter elements of set:')
    s = input()
    set_list = [i for i in s.split(' ')]
    print('Number of elements in presentation:') 
    k = int(input())
    presentation = {}
    for i in range(k):
        print(f'Enter element №{i + 1}')
        key = input()
        print(f'Enter equivalent of element №{i + 1}')
        val = input()
        presentation[key] = val
    semigroup, cayley_table = gen_cayley_table(set_list, presentation)
    if check_associative(semigroup, cayley_table):
        right_ideal, left_ideal, _ = find_ideals(semigroup, cayley_table)
        green_relation = build_green_relation(right_ideal, left_ideal)
        used = [False for _ in range(len(green_relation))]
        for i in range(len(green_relation)):
            if (not(used[i])):
                dfs(green_relation, used, i)
        used = [False for _ in range(len(green_relation))]
        egg_box = [[1]]
        for i in range(len(green_relation)):
            v = order[len(green_relation) - 1 - i]
            if (not(used[v])):
                dfs2(green_relation.T, used, v)
                c = []
                for el in component:
                    c.append(semigroup[el])
                egg_box.append(c.copy())
                component.clear()
        print(egg_box)
    else:
        print('Your Cayley table is not associative!')


def task4():
    print("Enter your set")
    st = input().split()
    print('Enter Cayley table')
    print("  ", *st)
    cayley_table = [input(f'{i}  ').split() for i in st]
    right_ideal, left_ideal, _ = find_ideals(st, cayley_table)
    green_relation = build_green_relation(right_ideal, left_ideal)
    used = [False for _ in range(len(green_relation))]
    for i in range(len(green_relation)):
        if (not(used[i])):
            dfs(green_relation, used, i)
    used = [False for _ in range(len(green_relation))]
    egg_box = []
    for i in range(len(green_relation)):
        v = order[len(green_relation) - 1 - i]
        if (not(used[v])):
            dfs2(green_relation.T, used, v)
            egg_box.append(component.copy())
            component.clear()
    print(egg_box)

if __name__ == "__main__":
    print("What are you want? (1 - Find ideals, 2 - Build green relation, 3 - Build green relation and egg-boxes by generating set and transformation set)")
    f = int(input())
    if f == 1:
        task1()
    elif f == 2:
        task2()
    elif f == 3:
        task3()
    else:
        print("Something going wrong! Enter a number from 1 to 3")