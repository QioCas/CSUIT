#include "../testlib.h"
#include "bits/stdc++.h"
using namespace std;

const int N_MAX = 10;
const long long BIG = 1000000000LL; // gây tràn int
const int C_MAX = 1000000000;

int main(int argc, char **argv) {
    registerGen(argc, argv, 1);
    int type = atoi(argv[1]);
    long long seed = atoll(argv[2]);
    rnd.setSeed(seed);

    int n, m;
    vector<tuple<int,int,long long>> edges;

    switch (type) {
        case 1: { // tràn int trên cạnh
            n = 3; m = 2;
            edges.push_back({1,2,BIG});
            edges.push_back({2,3,BIG});
            break;
        }
        case 2: { // sử dụng mảng [1..n]
            n = 5; m = 6;
            for (int i=1;i<=m;i++)
                edges.push_back({rnd.next(1,n),rnd.next(1,n),rnd.next(1,10)});
            break;            break;

        }
        case 3: { // đồ thị có hướng, chỉ đi ngược
            n = 5; m = 4;
            for (int i=2;i<=n;i++)
                edges.push_back({i,i-1,rnd.next(1,100)});
            break;
        }
        case 4: { // đồ thị đa cạnh
            n = 4; m = 8;
            for (int i=0;i<m;i++)
                edges.push_back({1,2,rnd.next(1,10)});
            break;
        }
        case 5: { // không có đường đi (-1 case nhỏ)
            n = 5; m = 3;
            for (int i=0;i<m;i++)
                edges.push_back({rnd.next(3,5),rnd.next(3,5),rnd.next(1,50)});
            break;
        }
        case 6: { // multiple edges causing overwrite in naive adjacency matrix
            n = 4; m = 6;
            edges.push_back({1,2,5});
            edges.push_back({1,2,10}); // ghi đè
            edges.push_back({2,3,7});
            edges.push_back({2,3,3});
            edges.push_back({3,4,1});
            edges.push_back({3,4,2});
            break;
        }
        case 7: { // sum overflow nếu dùng int
            n = 3; m = 3;
            edges.push_back({1,2,1000000000});
            edges.push_back({2,3,1000000000});
            edges.push_back({3,1,1000000000});
            break;
        }
        case 8: { // đồ thị có hướng, code quên xử lý sẽ WA
            n = 5; m = 5;
            edges.push_back({1,2,1});
            edges.push_back({2,3,1});
            edges.push_back({3,4,1});
            edges.push_back({4,5,1});
            edges.push_back({5,1,1});
            break;
        }
        case 9: { // có đường đi (OK, nhỏ)
            n = 6;
            edges.push_back({1,2,3});
            edges.push_back({2,3,2});
            edges.push_back({3,4,1});
            edges.push_back({4,5,5});
            edges.push_back({5,6,2});
            break;
        }
        case 10: { // không có đường đi, lớn
            n = 1000; m = 200;
            for(int i=0;i<m;i++)
                edges.push_back({rnd.next(500,1000), rnd.next(500,1000), rnd.next(1,100)});
            break;
        }
        case 11: { // có đường đi, lớn, để test TLE nhẹ
            n = 1000;
            for(int i=1;i<n;i++)
                edges.push_back({i,i+1,rnd.next(1,100)});
            break;
        }
    }

    cout << n << " " << edges.size() << "\n";
    for (auto &e : edges) {
        int u,v; long long w;
        tie(u,v,w)=e;
        cout<<u<<" "<<v<<" "<<w<<"\n";
    }
}
