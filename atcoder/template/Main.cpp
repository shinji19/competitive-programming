#include<iostream>
using namespace std;
int main() {
    // 整数の入力
    int D, T, S;
    cin >> D >> T >> S;


    // 出力
    if (D <= T * S) cout << "Yes" << endl;
    else cout << "No" << endl;

    return 0;
}
