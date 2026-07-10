// Solution Code O(N)
#include <bits/stdc++.h>
using namespace std;

int n;
unsigned int a[100100];

signed main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    
    cin >> n;
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
    }
    cout << sum << "\n";
    return 0;
}
