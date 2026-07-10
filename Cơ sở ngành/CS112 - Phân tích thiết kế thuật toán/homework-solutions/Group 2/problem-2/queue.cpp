#include <bits/stdc++.h>
#define INF 1000000000000000000

// SPFA with SLF(Small Label First)
// O(NM)

int main() {
	int n; std::cin >> n;
	int m; std::cin >> m;
	int s = 1;
	int t = n;
    -- s; -- t;
	struct Hen {
		int to;
		int cost;
		int id;
	};
	std::vector<std::vector<std::pair<int, int> > > hen(n);
	for (int i = 0; i < m; i++) {
        int a, b; std::cin >> a >> b;
        -- a; -- b;
        int c; std::cin >> c;
		hen[a].push_back({b, c});
	}
	std::vector<int64_t> dist(n, INF);
	std::vector<int> from(n, -1);
	std::vector<bool> inqueue(n, false);
	std::deque<int> que;
	que.push_back(s);
	dist[s] = 0;
	inqueue[s] = true;
	while (que.size()) {
		auto i = que.front();
		que.pop_front();
		inqueue[i] = false;
		for (auto j : hen[i]) if (dist[j.first] > dist[i] + j.second) {
			dist[j.first] = dist[i] + j.second;
			from[j.first] = i;
			if (!inqueue[j.first]) {
				inqueue[j.first] = true;
				que.push_front(j.first);
			}
		}
	}
	if (dist[t] == INF) std::cout << "-1";
	else {
		std::vector<int> path;
		for (int cur = t; cur != -1; cur = from[cur]) path.push_back(cur);
		std::reverse(path.begin(), path.end());
        std::cout << dist[t];
	}
	return 0;
}