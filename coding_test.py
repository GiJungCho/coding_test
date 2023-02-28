from collections import deque

# N = 노드 수 , M = 에지 수(연결 선 수) , Start = 시작점
N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1):
    A[i].sort()  # 번호가 작은 노드부터 방문하기 위해 정렬하기


def DFS(V):
    ### 중요 부분 ###
    print(V, end='')
    visited[V] = True
    for i in A[V]:
        if not visited[i]:
            DFS(i)
    ### 중요 부분 ###


visited = False * (N + 1)  # 리스트 초기화
DFS(Start)  # 실행


# BFS 구현
def BFS(V):
    # 큐 자료구조에 시작 노드 삽입
    queue = deque()
    queue.append(V)
    visited[V] = True

    while queue:  # 큐가 비어있을 떄 까지
        ### 중요 부분
        now_Node = queue.popleft()
        print(queue, end='')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        ### 중요 부분


visited = [False] * (N + 1)  # 리스트 초기화
BFS(Start)  # 실행