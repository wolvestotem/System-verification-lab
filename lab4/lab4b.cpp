#include <fstream>
#include<iostream>
#include<vector>
#include<set>

using namespace std;

void addedge(vector<vector<int>>& graph, int u, int v){
  graph[u].push_back(v);
}

vector<int> tysort(vector<vector<int>>& graph, int V, int E){
  vector<int> indegree(V,0);
  for(int v=0; v<V; v++){
    for(int u=0; u<graph[v].size(); u++)
      indegree[graph[v][u]]++;
  }
  multiset<int> s;
  for(int i=0; i<indegree.size(); i++){
    if(indegree[i]==0)
      s.insert(i);
  }
  vector<int> result;

  while(!s.empty()){
    // int size=s.size();
    int head = *s.begin();
    s.erase(head);
    result.push_back(head);

    for(int u=0;u<graph[head].size();u++){
      indegree[graph[head][u]]--;
      if(indegree[graph[head][u]]==0)
        s.insert(graph[head][u]);
    }
  }
  return result;
}

int main(int argc, char* argv[]) 
{ 
  if(argc<2)
    return 1;
  ifstream fin(argv[1]);
  ofstream fileout("./result.txt");
  int V,E;
  fin>>V>>E;
  vector<vector<int>> graph(V);

  for(int e=0; e<E; e++){
    int x,y;
    fin>>x>>y;
    addedge(graph,x,y);
  }
  vector<int> result;
  result = tysort(graph,V,E);

  for(int ele:result){
    fileout<<ele<<' ';
  }

  fin.close();
  fileout.close();

  return 0;
}