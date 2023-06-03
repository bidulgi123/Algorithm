#include <iostream>
using namespace std;

int main() {
    int j[10], s[10], flag = 0, total_j = 0, total_s = 0;

    for (int i = 1; i <= 9; i++) cin >> j[i];
    for (int i = 1; i <= 9; i++) cin >> s[i];

    for (int i = 1; i <= 9; i++) {
        total_j += j[i];
        if (total_j > total_s)
            flag = 1;
        total_s += s[i];
    }

    if (flag == 1 && total_s > total_j)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}