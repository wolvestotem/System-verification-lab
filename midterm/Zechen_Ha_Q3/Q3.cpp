#include"Q3.h"

int solve(int n){
    int result = 0;
    //return result;
    //This is the primary code for tdd test to get a failture

    //This is the code after failture tests
    if(n==1) return 1;
    if(n==2) return 1;
    vector<int> table(n+1,0);
    table[1] = 1;
    table[2] = 1;
    for(int i=3;i<=n;i++){
        table[i] = table[i-1]+table[i-2];
    }
    return table[n];
}

void check(int aim, int result){
    if(aim==result)
        cout<<"Correct"<<endl;
    if(aim!=result)
        cout<<"Incorrect"<<endl;
}

int main(){
    int res;
    res = solve(1);
    check(res,1);
    res = solve(2);
    check(res,1);
    res = solve(3);
    check(res,2);
}