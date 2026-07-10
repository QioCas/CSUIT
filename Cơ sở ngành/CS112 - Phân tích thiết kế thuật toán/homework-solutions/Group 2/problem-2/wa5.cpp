#include <bits/stdc++.h>

#define INF 1000000000000000000

template<typename T> using pqueue_inv = std::priority_queue<T, std::vector<T>, std::greater<T> >;

int main() {
    std::cin.tie(0)->sync_with_stdio(false);

    int n, m; std::cin >> n >> m;
    int s = 0, t = n - 1;
	std::vector<std::vector<std::pair<int, int> > > hen(n);
	for (int i = 0; i < m; i++) {
        int a, b, c; std::cin >> a >> b >> c;
        --a; --b;
		hen[a].push_back({b, c});
	}
	std::vector<int64_t> dist(n, INF);
	std::vector<int> from(n, -1);
	pqueue_inv<std::pair<int64_t, int> > que;
	que.push({dist[s] = 0, s});
	while (que.size()) {
		auto i = que.top();
		que.pop();
		if (i.first != dist[i.second]) continue;
		for (auto j : hen[i.second]) if (dist[j.first] > i.first + j.second) 
			que.push({dist[j.first] = i.first + j.second, j.first}), from[j.first] = i.second;
	}
	std::cout << dist[t];
	return 0;
}