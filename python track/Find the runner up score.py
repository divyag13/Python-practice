'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
'''


if __name__ == '__main__':
    n = int(input())
    lis = list(map(int, input().split()))
    
    winner = -101
    runner_up = -101
    for i in lis:
        if(winner < i):
            runner_up = winner
            winner = i
        if(winner > i and runner_up < i):
            runner_up = i
    
    print(runner_up)
    
    

