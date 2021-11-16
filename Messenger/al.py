import sys;input=sys.stdin.readline;from collections import deque
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
adj, dfsn, cnt, S = [[] for _ in range(N)], [0]*N, 0, [] # dfsn는 노드별 id 기록, cnt는 id 세는 변수, S는 스택
finished, SCC, SN, sn = [False] * N, [], 1, [-1]*N # 아예 SCC로 추출이 끝난 노드들 기록

# SCC를 찾는 함수
def dfsSCC(curr):
    global dfsn, cnt, S, SN, finished, SCC, sn
    
    cnt += 1
    dfsn[curr] = cnt # dfsn 결정
    S.append(curr) # 스택에 자신을 push
    
    # 자신의 dfs, 자식들의 결과나 dfsn 중 가장 작은 번호를 result에 저장
    result = dfsn[curr]
    for n in adj[curr]:
        # 아직 방문하지 않은 이웃
        if dfsn[n] == 0:
            result = min(result, dfsSCC(n))
        # 방문은 했으나 아직 SCC로 추출되지는 않은 이웃
        elif not finished[n]:
            result = min(result, dfsn[n])
        
    # 자신, 자신의 자손들이 도달 가능한 제일 높은 정점이 자신일 경우
    if result == dfsn[curr]:
        currSCC = []
        # 스택에서 자신이 나올 때까지 pop
        while(1):
            temp = S.pop()
            currSCC.append(temp)
            finished[temp] = True
            sn[temp] = SN
            if temp == curr:
                break
                
        # 출력을 위해 원소 정렬
        currSCC.sort()
        # SCC 추출
        SCC.append(currSCC)
        SN += 1
        
    return result

# 그래프 입력
for _ in range(M):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
for i in range(N):
    if dfsn[i] == 0:
        dfsSCC(i)
        
# 각 교차로의 현금 정보 입력
cash = [int(input().strip()) for _ in range(N)]
# 레스토랑 정보 입력
hasRest = [False] * N
start, P = map(int, input().split())
start -= 1
for i in map(int, input().split()):
    hasRest[i-1] = True
    
sAdj = [[0]*SN for _ in range(SN)] # 이 SCC와 인접한 SCC를 담고 있는 리스트
sStart = 0 # 시작점을 포함하는 SCC 번호
sCash = [0] * SN # 해당 SCC의 현금 액수 총합
sIndegree = [0]*SN # 해당 SCC의 indegree
sHasRest = [0] * SN # 해당 SCC의 레스토랑 포함 여부

for i in range(N):
    si = sn[i]
    sCash[si] += cash[i]
    if hasRest[i]:
        sHasRest[si] = True
    if i == start:
        sStart = si
        
    # sAdj 채우기
    for j in adj[i]:
        sj = sn[j]
        if si == sj:
            continue
        # i와 j가 서로 다른 SCC에 포함될 때만 간선 생성
        sAdj[si].append(sj)
        sIndegree[sj] += 1
        
q = deque()
sMax = [0] * SN # 각 SCC의 결과값
sCal = [0]*SN # 시작점에서 이 SCC에 도달할 수 있는가?
for i in range(SN):
    sMax[i] = sCash[i] # 결과값 초기화: 자신의 액수만큼은 챙길 수 있다.
    if i == sStart:
        sCal[i] = True
    if sIndegree[i] == 0:
        q.append(i)
        
# 위상정렬 시작
while q:
    curr = q.popleft()
    for n in sAdj[curr]:
        if sCal[curr]: # 이 SCC에 도달 가능해야만 n읮 정보 갱신
            sMax[n] = max(sMax[n], sMax[curr] + sCash[n])
            sCal[n] = True 
        sIndegree[n] -= 1
        if sIndegree[n] == 0:
            q.append(n)
            
ans = 0

for i in range(SN):
    if sHasRest[i] and sCal[i]:
        ans = max(ans, sMax[i]) 
print(ans)