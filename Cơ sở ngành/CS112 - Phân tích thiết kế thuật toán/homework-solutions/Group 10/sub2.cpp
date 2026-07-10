#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 700005;

int n; ll m;
ll w[N];
vector<int> G[N];
pair<ll, ll> dp[N];
ll numFired[370];

void dfs(int u) {
    if (G[u].empty()) {
        dp[u] = {1, w[u]};
        return;
    }

    for(int v : G[u]) dfs(v);

    ll min_kept = 0;
    ll cap = w[u] + (int) G[u].size();

    for(int i = 0; i <= m; ++i) numFired[i] = -1;
    
    numFired[cap] = 0;
    for(int v : G[u]) {
        auto [kept_v, cap_v] = dp[v];
        min_kept += kept_v;

        if(cap_v == 0) {
            numFired[cap-1] = numFired[cap] + 1;
            --cap;
        }
    }


    for (int v : G[u]) {
        auto [kept_v, cap_v] = dp[v];
        if(cap_v == 0) continue;
        for(int i = m - cap_v + 1; i >= cap; --i) {
            if(numFired[i] != -1) {
                numFired[i + cap_v - 1] = max(numFired[i + cap_v - 1], numFired[i] + 1);
            }
        }
    }

    int best = cap;
    for(int i = cap; i <= m; ++i) {
        if(numFired[best] < numFired[i]) {
            best = i;
        }
    }

    dp[u] = {1 + min_kept - numFired[best], best};
    return;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);

    cin >> n >> m;
    assert(m <= 369);
    for (int i = 1; i <= n; i++) {
        cin >> w[i];
    }

    for (int i = 1; i < n; i++) {
        int p; cin >> p;
        G[p].push_back(i + 1);
    }

    dfs(1);
    ll ans = n - dp[1].first;
    cout << ans << "\n";

    return 0;
}
