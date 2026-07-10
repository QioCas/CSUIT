#include <bits/stdc++.h>
using namespace std;

mt19937 rng(time(NULL));
int myrand(int l, int r) {
    return uniform_int_distribution<int>(l, r) (rng);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<long long> a(n);
    vector<long long> cpx;
    for (int i = 0; i < n; i++) cin >> a[i], cpx.push_back(a[i]);
    sort(cpx.begin(), cpx.end());
    for (int i = 0; i < n; i++) a[i] = lower_bound(cpx.begin(), cpx.end(), a[i]) - cpx.begin();
    // Build pos[value]
    vector<vector<int>> pos(n);

    for (int i = 0; i < n; i++) {
        pos[a[i]].push_back(i + 1);
    }

    const int K = 30;
    vector<long long> result;
    result.reserve(q);

    while (q--) {
        int L, R;
        cin >> L >> R;
        int len = R - L + 1;
        int need = len / 2;

        long long ans = -1;

        for (int t = 0; t < K; t++) {
            int x = myrand(L, R);       // random index
            int v = a[x - 1];     // element value

            int left  = lower_bound(pos[v].begin(), pos[v].end(), L) - pos[v].begin();
            int right = upper_bound(pos[v].begin(), pos[v].end(), R) - pos[v].begin();
            int cnt = right - left;

            if (cnt > need) {
                ans = v;
                break;
            }
        }
        
        result.push_back(ans == -1 ? -1 : cpx[ans]);
    }

    // Output
    for (int i = 0; i < (int)result.size(); i++) {
        cout << result[i];
        if (i + 1 < (int)result.size()) cout << " ";
    }
    return 0;
}
