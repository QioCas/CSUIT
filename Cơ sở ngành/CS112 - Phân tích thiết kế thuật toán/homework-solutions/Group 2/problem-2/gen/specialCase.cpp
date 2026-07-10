#include "../testlib.h"
#include "bits/stdc++.h"
using namespace std;

int main(int argc, char **argv) {
    registerGen(argc, argv, 1);
    int type = atoi(argv[1]);
    long long seed = atoll(argv[2]);
    rnd.setSeed(seed);

    vector<tuple<int,int,int>> e;
    int n=0;

    if(type==1){ // cycle có hướng
        n=6;
        for(int i=1;i<=n;i++) e.push_back({i,(i%n)+1,1});
    }
    else if(type==2){ // hai đường cùng độ dài
        n=6;
        e.push_back({1,2,1});
        e.push_back({2,6,1});
        e.push_back({1,3,1});
        e.push_back({3,6,1});
    }
    else if(type==3){ // đồ thị dày nhưng tồn tại nhiều song song
        n=10;
        for(int i=0;i<200;i++) e.push_back({rnd.next(1,n),rnd.next(1,n),rnd.next(1,100)});
    }
    else if(type==4){ // dense complete nhưng chưa tới TLE
        n=400;
        for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) if(i!=j)
            e.push_back({i,j,1});
    }
    else if(type==5){ // reverse only (không tới n)
        n=50;
        for(int i=2;i<=n;i++)
            e.push_back({i,i-1,1});
    } else if(type == 6) {
        n=5;
        e.push_back({1,2,1});
        e.push_back({2,3,1});
        e.push_back({3,4,1});
        e.push_back({4,5,1});
        e.push_back({5,1,1}); // tạo chu trình
    }

    cout<<n<<" "<<e.size()<<"\n";
    for(auto [u,v,w]:e) cout<<u<<" "<<v<<" "<<w<<"\n";
}
