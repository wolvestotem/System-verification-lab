def BFS(self,graph,s,t):
    visit = [False]*100
    queue=[]
    result=0
    queue.append(s)
    visit[s]=True

    while queue:
        result=result+1
        for i in range(len(queue)):
            sr=queue.pop(0)
            for j in graph[sr]:
                if visit[j]==False:
                    queue.append(j)
                    visit[j]=True

    print(result-1)
    return result-1



