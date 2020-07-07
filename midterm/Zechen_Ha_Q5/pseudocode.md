# pseudocode of BFS

```python
def BFS(self,s,t):
    visit=[False]*100

    result=0
    queue.append(s)
    visit[s]=True

    while(queue):
        for i in range(len(queue)):
            sr=queue.pop(0)
            for adj_node in s_adj:
                if(visit[adj_node]==False):
                    queue.append(adj_node)
                    visit[adj_node]=True
    return result-1
```
