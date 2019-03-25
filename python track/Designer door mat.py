'''Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''


N,M= map(int,input().split())
dot = -1
line = 0
lis = [[] for _ in range(N)]
for i in range(0,N//2):
    dot +=2
    line +=1
    dash = (M+1)//2 -(dot+line)
    
    for _ in range(0,dash):
        lis[i].append('-')
    lis[i].append('.|')
    
    for _ in range(i):
        lis[i].append('..|')
    for _ in range(i):
        lis[i].append('..|')
    lis[i].append('.')
    
    for _ in range(0,dash):
        lis[i].append('-')
    print(''.join(str(x) for x in lis[i]))

dash = M//2 -3
for _ in range(0,dash):
    lis[N//2].append('-')
lis[N//2].append('WELCOME')
for _ in range(0,dash):
    lis[N//2].append('-')
print(''.join(str(x) for x in lis[N//2]))

for i in range((N//2)+1,N):
    
    dash = (M+1)//2 -(dot+line)
    dot -=2
    line -=1
    
    for _ in range(0,dash):
        lis[i].append('-')
    lis[i].append('.|')
    
    for _ in range(N-i-1):
        lis[i].append('..|')
    for _ in range(N-i-1):
        lis[i].append('..|')
    lis[i].append('.')
    
    for _ in range(0,dash):
        lis[i].append('-')
    print(''.join(str(x) for x in lis[i]))


