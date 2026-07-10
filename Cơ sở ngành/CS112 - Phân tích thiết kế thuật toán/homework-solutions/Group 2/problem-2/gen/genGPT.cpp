#include "../testlib.h"
#include "bits/stdc++.h"
using namespace std;

const int N_MIN = 2;
const int N_MAX = 100000;
const long long C_MIN = 1;
const long long C_MAX = 1000000000LL;

int main(int argc, char **argv) {
    registerGen(argc, argv, 1);
    int type = atoi(argv[1]);        // chọn special case 1..10
    long long seed = atoll(argv[2]); // random seed
    rnd.setSeed(seed);

    vector< tuple<int,int,long long> > edges;
    int n = 0;

    auto add_edge = [&](int u, int v, long long w) {
        // u,v are 1-based
        edges.emplace_back(u, v, w);
    };

    switch (type) {
        case 1: {
            // 1. Nhiều cạnh song song giữa 1 và 2; rẽ tới n
            n = 4;
            // many parallel edges 1->2
            for (int k = 0; k < 12; ++k) {
                add_edge(1, 2, rnd.next(1, 100));
            }
            // small chain to n
            add_edge(2, 3, rnd.next(1, 100));
            add_edge(3, 4, rnd.next(1, 100));
            // some extra random edges
            for (int i = 0; i < 5; ++i) add_edge(rnd.next(1,n), rnd.next(1,n), rnd.next(1,100));
            break;
        }
        case 2: {
            // 2. Self-loop present (but shouldn't affect shortest path)
            n = rnd.next(5, 20);
            // chain 1->2->...->n to ensure path exists
            for (int i = 1; i < n; ++i) add_edge(i, i+1, rnd.next(1, 50));
            // add some self-loops
            int loops = min(5, n);
            for (int i = 0; i < loops; ++i) {
                int v = rnd.next(1, n);
                add_edge(v, v, rnd.next(1, 100));
            }
            // some extra random edges
            for (int i = 0; i < n; ++i) add_edge(rnd.next(1,n), rnd.next(1,n), rnd.next(1,200));
            break;
        }
        case 3: {
            // 3. Không có đường tới n (1 và n ở 2 thành phần tách biệt)
            n = rnd.next(5, 60);
            // split: left = [1..k], right = [k+1..n] with 1 in left and n in right
            int k = rnd.next(1, n-2);
            // random edges inside left
            for (int i = 0; i < k*2; ++i) add_edge(rnd.next(1,k), rnd.next(1,k), rnd.next(1,100));
            // random edges inside right
            for (int i = 0; i < (n-k)*2; ++i) add_edge(rnd.next(k+1,n), rnd.next(k+1,n), rnd.next(1,100));
            // optionally add reverse edges from right -> left (still no path from 1->n)
            for (int i = 0; i < 5; ++i) {
                int u = rnd.next(k+1, n);
                int v = rnd.next(1, k);
                add_edge(u, v, rnd.next(1,100));
            }
            break;
        }
        case 4: {
            // 4. Nhiều đường cùng độ dài (tạo 2 đường node-disjoint cùng tổng trọng số)
            int path_len = rnd.next(2, 5); // số cạnh mỗi đường
            // build nodes: 1, A1..A_pathlen, B1..B_pathlen, n
            n = 2 + 2*path_len;
            int start = 1;
            int fin = n;
            // path A: 1 -> 2 -> ... -> 1+path_len -> n
            int baseA = 2;
            for (int i = 0; i < path_len; ++i) {
                int u = (i==0 ? start : baseA + i - 1);
                int v = baseA + i;
                add_edge(u, v, 1);
            }
            add_edge(baseA + path_len - 1, fin, 1);

            // path B: 1 -> baseB -> ... -> n (make indices after A)
            int baseB = baseA + path_len;
            for (int i = 0; i < path_len; ++i) {
                int u = (i==0 ? start : baseB + i - 1);
                int v = baseB + i;
                add_edge(u, v, 1);
            }
            add_edge(baseB + path_len - 1, fin, 1);

            // add a few extra edges
            for (int i = 0; i < 5; ++i) add_edge(rnd.next(1,n), rnd.next(1,n), rnd.next(1,100));
            break;
        }
        case 5: {
            // 5. Chu trình xuất hiện (cycle) nhưng vẫn có đường tới n
            n = rnd.next(6, 20);
            // create a cycle among nodes 2..k
            int k = rnd.next(3, min(5, n-2));
            int cycle_start = 2;
            for (int i = 0; i < k; ++i) {
                int u = cycle_start + i;
                int v = cycle_start + ((i+1)%k);
                add_edge(u, v, rnd.next(1,50));
            }
            // connect 1 -> cycle_start
            add_edge(1, cycle_start, rnd.next(1,50));
            // connect some node in cycle to n
            add_edge(cycle_start + rnd.next(0,k-1), n, rnd.next(1,50));
            // add other random edges
            for (int i = 0; i < n; ++i) add_edge(rnd.next(1,n), rnd.next(1,n), rnd.next(1,200));
            break;
        }
        case 6: {
            // 6. Có cạnh trực tiếp 1->n nhưng nốt đường khác ngắn hơn
            n = rnd.next(5, 20);
            // direct heavy edge
            add_edge(1, n, rnd.next(1000, 10000));
            // create short chain 1->2->...->n with small weights
            for (int i = 1; i < n; ++i) add_edge(i, i+1, rnd.next(1, 5));
            // some extra noise
            for (int i = 0; i < n; ++i) add_edge(rnd.next(1,n), rnd.next(1,n), rnd.next(1,100));
            break;
        }
        case 7: {
            // 7. Trọng số lớn (kiểm tra long long)
            n = 3;
            add_edge(1, 2, 1000000000LL); // 1e9
            add_edge(2, 3, 1000000000LL); // 1e9 => total = 2e9
            // add a direct heavy but larger than sum maybe (but <= 1e9 constraint per edge prevents >1e9)
            add_edge(1, 3, rnd.next(1, 1000000000)); // could be <=1e9
            break;
        }
        case 8: {
            // 8. Cạnh thừa (redundant edges)
            n = rnd.next(20, 100);
            // shortest path chain
            for (int i = 1; i < n; ++i) add_edge(i, i+1, 1);
            // many redundant edges with large weights
            int extras = min(5 * n, 200000); 
            for (int i = 0; i < extras; ++i) {
                int u = rnd.next(1, n);
                int v = rnd.next(1, n);
                add_edge(u, v, rnd.next(1000, 1000000));
            }
            break;
        }
        case 9: {
            // 9. Complete directed graph (stress dense)
            // choose n such that n*(n-1) <= 200000
            int nmax = 400; // 400*399 = 159600
            n = min(nmax, N_MAX);
            for (int u = 1; u <= n; ++u) {
                for (int v = 1; v <= n; ++v) if (u != v) {
                    add_edge(u, v, rnd.next(1, 100));
                }
            }
            break;
        }
        case 10: {
            // 10. Đồ thị hướng ngược: chỉ có cạnh từ higher -> lower => không thể đi từ 1 -> n
            n = rnd.next(5, 100);
            // add edges only from i -> j if i > j
            for (int i = 2; i <= n; ++i) {
                // connect i -> i-1
                add_edge(i, i-1, rnd.next(1, 100));
            }
            // add some extra backward edges
            for (int i = 0; i < n * 2 && (int)edges.size() < 200000; ++i) {
                int u = rnd.next(2, n);
                int v = rnd.next(1, u-1);
                add_edge(u, v, rnd.next(1, 1000));
            }
            break;
        }
        default: {
            // default: small random graph
            n = rnd.next(2, 20);
            int m = rnd.next(1, min(200, n*(n-1)));
            for (int i = 0; i < m; ++i) add_edge(rnd.next(1,n), rnd.next(1,n), rnd.next(1,100));
            break;
        }
    }

    // final output
    // ensure we don't exceed m limit
    if ((int)edges.size() > 200000) {
        // trim (only for safety)
        edges.resize(200000);
    }

    cout << n << " " << edges.size() << "\n";
    for (auto &e : edges) {
        int u,v; long long w;
        tie(u,v,w) = e;
        if (w < C_MIN) w = C_MIN;
        if (w > C_MAX) w = C_MAX;
        cout << u << " " << v << " " << w << "\n";
    }

    return 0;
}
