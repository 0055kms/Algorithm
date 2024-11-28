import sys
sys.setrecursionlimit(10**6)

def solution(user_id, banned_id):
    answer = 0
    case = set() # 가능한 경우의 수: 넣을 때 튜플 변환 및 sort 함
    
    def compare(uid,bid):
        if len(uid) != len(bid): return False
        for i in range(len(uid)):
            if not (bid[i] == '*' or bid[i] == uid[i]): return False
        return True
    
    visit = [False] * len(user_id)
    def dfs(cur,idx):
        if idx == len(banned_id):
            case.add(tuple(sorted(cur)))
            return
        for i in range(len(user_id)):
            if compare(user_id[i],banned_id[idx]) and not visit[i]:
                visit[i] = True
                cur.append(i)
                dfs(cur,idx+1)
                cur.pop()
                visit[i] = False
    dfs([],0)
        
    
    return len(case)