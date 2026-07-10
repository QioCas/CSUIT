// Solution
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 700005;

int n; ll m;
ll w[N];
vector<int> G[N];
pair<ll, ll> dp[N];

void dfs(int u) {
    if (G[u].empty()) {
        dp[u] = {0, w[u]};
        return;
    }

    for(int v : G[u]) dfs(v);
    
    sort(G[u].begin(), G[u].end(), [&] (int a, int b) { return dp[a].second < dp[b].second; });

    ll sumFired = 0;
    ll cap = w[u] + (int) G[u].size();
    ll numFired = 0;

    for (int v : G[u]) {
        auto [fired_v, cap_v] = dp[v];
        sumFired += fired_v;

        if (cap + cap_v - 1 <= m) {
            cap += cap_v - 1;
            numFired++;
        } 
    }

    dp[u] = {sumFired + numFired, cap};
    return;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);

    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        cin >> w[i];
    }

    for (int i = 1; i < n; i++) {
        int p; cin >> p;
        G[p].push_back(i + 1);
    }

    dfs(1);
    cout << dp[1].first << "\n";

    return 0;
}
