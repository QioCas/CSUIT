// Wrong answer (Out bound)
#include <bits/stdc++.h>
using namespace std;

int n;

signed main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    
    cin >> n;
    long long sum = 0;
    int a[n];
    for(int i = 1; i <= n; ++i) {
        cin >> a[i];
        sum += a[i];
    }
    cout << sum << "\n";
    return 0;
}
