#include <fstream>
#include<vector>
#include<queue>
#include<algorithm>
#include<iostream>

using namespace std;

void addedge(vector<pair<int,int>> graph[], int x, int y, int w){
  graph[x].push_back(make_pair(y,w));
  graph[y].push_back(make_pair(x,w));
}

void addwedge(vector<pair<int,pair<int,int>>>& wgraph, int x, int y, int w){
  wgraph.emplace_back(w,make_pair(x,y));
}

bool comparison(pair<int,pair<int,int>> a, pair<int,pair<int,int>> b){
  return a.first<b.first;
}

bool bipartite(vector<int>& colormap, vector<pair<int,int>> graph[],int src){
  queue<int> q;
  colormap[src]=1;
  q.push(src);
  while(!q.empty()){
    int head = q.front();
    q.pop();

    for(auto p:graph[head]){
      if(colormap[p.first]==-1){
        colormap[p.first]=1-colormap[head];
        q.push(p.first);
      }
      if(colormap[p.first]==colormap[head])
        return false;
      
    }
  }
  return true;
}

int find(int i,vector<int>& group){
  if(group[i]==i)
    return i;
  else{
    return find(group[i], group);
  }
}

void uni(vector<int>& group, int u, int v){
  group[u] = group[v];
}

vector<pair<int,int>> kruskal(vector<pair<int,pair<int,int>>>& wgraph,int V, int E){
  vector<pair<int,int>> mst;
  vector<int> group(V);
  for(int v=0; v<V; v++){
    group[v]=v;
  }
  for(int e=0; e<E; e++){
    int one = find(wgraph[e].second.first, group);
    int another = find(wgraph[e].second.second, group);
    if(one != another){
      mst.push_back(wgraph[e].second);
      uni(group, one, another);
    }
  }
  return mst;
}

int main(int argc, char* argv[]) 
{ 
  if(argc < 2)
    return 1;
  ifstream fin(argv[1]);
  
  int V,E;
  fin>>V>>E;
  vector<pair<int,int>> graph[V];
  vector<pair<int,pair<int,int>>> wgraph;
  //node,weight

  int x,y,w;
  for(int i=0; i<E; i++){
    fin>>x>>y>>w;
    addedge(graph,x,y,w);
    addwedge(wgraph,x,y,w);
  }
  

  vector<int> colormap(V,-1);
  //0,1 two colors
  bool result = true;
  for(int v=0;v<V;v++){
    if(colormap[v]==-1){
      if(bipartite(colormap,graph,v)==false)
        result = false;
    }
  }

  sort(wgraph.begin(),wgraph.end(),comparison);
  vector<pair<int,int>> mst;
  mst = kruskal(wgraph, V, E);

  ofstream fileout("./result.txt");
  if(result){
    fileout<<"Yes";
  }
  else
    fileout<<"No";

  for(auto t:mst){
    // cout<<t.first<<' '<<t.second<<endl;
    fileout<<endl<<t.first<<' '<<t.second;
  }
  
  fileout.close();
  fin.close();
  

  return 0;
} 