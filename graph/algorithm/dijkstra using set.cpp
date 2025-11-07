// User Function Template
#include <vector>
#include <set>
#include <stdio.h>
#include <climits> // for INT_MAX
using namespace std;
class Solution {
  public:
    vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {
        // Code here
        set<pair<int,int>> st;
        vector<int> result(V,INT_MAX);
        vector<vector<pair<int,int>>> adj(V);
        
       
        for(auto edj:edges){
            int u=edj[0];
            int v=edj[1];
            int w=edj[2];
            adj[u].push_back({v,w});

        }
        
        
        result[src]=0;
        st.insert({0,src});
        while(!st.empty()){
            auto &it= *st.begin(); //since its a ordered set hence it always gives smallest ele
        
            int d=it.first;
            int u=it.second;
            
            st.erase(it);
            for (auto &node:adj[u]){
                int v=node.first;
                int wt=node.second;
                
                if (d+wt< result[v]){
                    if (result[v] !=INT_MAX){
                        st.erase({result[v],v});
                    }
                    result[v]=d+wt;
                    st.insert({d+wt,v});
                    
                }
            }
        }
        return result;
    }
};