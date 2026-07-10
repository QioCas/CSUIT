// Wrong answer (Out bound)
#include <bits/stdc++.h>
using namespace std;

int n;
int a[100100];

signed main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    
    cin >> n;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
    }
    cout << sum;
    return 0;
}
