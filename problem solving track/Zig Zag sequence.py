'''In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given two dates each in the format dd-mm-yyyy, you have to find the number of lucky dates between them (inclusive). To see if a date is lucky,

Firstly, sequentially concatinate the date, month and year, into a new integer  erasing the leading zeroes.
Now if  is divisible by either  or , then we call the date a lucky date.
For example, let's take the date "02-08-2024". After concatinating the day, month and year, we get  = 2082024. As  is divisible by  so the date "02-08-2024" is called a lucky date.

Debug the given function findPrimeDates and/or other lines of code, to find the correct lucky dates from the given input.

Note: You can modify at most five lines in the given code and you cannot add or remove lines to the code.

To restore the original code in the editor, create a new buffer by clicking on the top left icon in the editor.

Input Format

The only line of the input contains two strings  and  denoting the two dates following the format dd-mm-yyyy. Consider,  is the day number,  is the month number and  is the year number.

Note: Here  means January,  means February,  means March and so on and all the dates follow the standard structure of English calender including the leap year.

Constraints

 
 

Output Format

For each test cases, print a single integer the number of lucky dates between  and  in a single line.

Sample Input 0

02-08-2025 04-09-2025
Sample Output 0

5
'''
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



