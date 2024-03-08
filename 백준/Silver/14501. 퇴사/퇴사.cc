#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> T(N), P(N), arr(N + 1, 0);
    
    for (int i = 0; i < N; i++) {
        cin >> T[i] >> P[i];
    }
    
    for (int i = 0; i < N; i++) {
        if (T[i] + i <= N) {
            arr[T[i] + i] = max(arr[T[i] + i], arr[i] + P[i]);
        }
        arr[i + 1] = max(arr[i + 1], arr[i]);
    }
    
    cout << arr[N] << endl;
    
    return 0;
}
