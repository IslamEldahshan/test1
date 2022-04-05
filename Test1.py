#
# n, h = input().split()
# ai = input().split()
#
# i = 0
# roadWith = 0
# while i < int(n):
#     if int(ai[i]) > int(h):
#         roadWith += 2
#     else:
#         roadWith +=1
#     i = i + 1
#
# print(roadWith)


# --------------------------------------------------

# n = int(input())
# s = input()
# anton = 0
# danik = 0
# for i in range(n):
#     if s[i] == 'A':
#         anton += 1
#     else:
#         danik += 1
#
# if anton > danik:
#     print('Anton')
# elif danik > anton:
#     print('Danik')
# else:
#     print('Friendship')


# ----------------------------------------------------

# a,b = input().split()
# years = 0
# while int(a) <= int(b):
#     a = int(a) * 3
#     b = int(b) * 2
#     years += 1
#
# print(years)

# ----------------------------------------------

# n = int(input())
# problem_number = 0
# for i in range(n):
#     areSure = 0
#     solutions = input().split()
#     for j in range(3):
#         if int(solutions[j]) == 1:
#             areSure += 1
#     if areSure >= 2:
#         problem_number += 1
#
# print(problem_number)

# ----------------------------------------
# moves = 0
# for i in range(5):
#     lines = input().split()
#     for j in range(5):
#         if int(lines[j]) == 1:
#             moves = abs(2 - j) + abs(2 - i)
# print(moves)

# ----------------------------------------

# n = int(input())
# columns = input().split()
# for i in range(n-1):
#     if columns[i] > columns[i+1]:
#         columns[i] = columns[i] + columns[i] - columns[i+1]
# print(columns)


# ----------------------------------------
#
# first_string  = input().lower()
# secound_string  = input().lower()
# if(first_string < secound_string):
#     print(-1)
# elif(first_string > secound_string):
#     print(1)
# else:
#     print(0)

# ----------------------------------------

# odd = male  ,   even = female

# name = input()
# name_char = []
# for i in range(name.__len__()):
#     if name[i] not in name_char:
#         name_char.append(name[i])
#
# if name_char.__len__() %2 == 0:
#     print('CHAT WITH HER!')
# else:
#     print('IGNORE HIM!')

# ------------------------------

# word = input()
# lower = 0
# upper = 0
# for i in range(len(word)):
#     if word[i].islower():
#         lower += 1
#     else:
#         upper += 1
# if lower >= upper :
#     print(word.lower())
# else:
#     print(word.upper())

# ---------------------------------------
#
# n = int(input())
# places = 0
# for i in range(n):
#     pi, qi = input().split()
#     if int(qi) - int(pi) >= 2:
#         places += 1
# print(places)

# --------------------------------------------

# n = int(input())
# pi = input().split()
# for i in range(n):
#     for j in range(n):
#         if i+1 == int(pi[j]):
#             print(j+1)

# ---------------------------------------------

# n = int(input())
# direction = input()
# coordinates = input().split()
# time = -1
# for i in range(n-1):
#     if direction[i] == 'R' and direction[i+1] == 'L':
#         if time == -1:
#             time = abs(int(coordinates[i]) - int(coordinates[i + 1])) // 2
#         elif abs(int(coordinates[i]) - int(coordinates[i + 1])) // 2 < time:
#             time = abs(int(coordinates[i]) - int(coordinates[i + 1])) // 2
#
# print(time)

# ------------------------------------------------------

# ratio = input().split()
# p = int()
# q = int()
# if ratio[1] > ratio[0]:
#     p = int(ratio[0]) / int(ratio[1])
# else:
#     p = int(ratio[1]) / int(ratio[0])
#
# if ratio[3] > ratio[2]:
#     q = int(ratio[2]) / int(ratio[3])
# else:
#     q = int(ratio[3]) / int(ratio[2])
#
# print(f'{abs(p-q)}')

# -------------------------------------
# import  math
# n = int(input())
# groupMember = input().split()
# minTaxi = 0
# for i in range(len(groupMember)):
#     minTaxi += int(groupMember[i])
# minTaxi = math.ceil(minTaxi/4)
# print(minTaxi)

# ------------------------------------------

# Problem Link : https://codeforces.com/problemset/problem/4/A

# n = int(input())
# if n % 2 == 0:
#     if (n/2) % 2 == 0 or ((n-2) % 2 == 0 and n-2 != 0):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# ------------------------------------------


moves = 0
for i in range(5):
    lines = input().split()
    for j in range(5):
        if int(lines[j]) == 1:
            moves = abs(2 - j) + abs(2 - i)
print(moves)

# 0 0 0 0 0     =>0
# 0 0 0 0 1     =>1
# 0 0 0 0 0     2
# 0 0 0 0 0     3
# 0 0 0 0 0     4
