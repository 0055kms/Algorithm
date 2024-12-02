def solution(tickets):
    from collections import defaultdict

    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for key in graph:
        graph[key].sort()

    path = []

    def dfs(cur):
        while graph[cur]:
            next_destination = graph[cur].pop(0)
            dfs(next_destination)
        path.append(cur)

    dfs("ICN")
    return path[::-1]
