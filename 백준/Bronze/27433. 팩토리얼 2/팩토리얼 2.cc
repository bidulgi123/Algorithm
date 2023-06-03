
#include <iostream>

using namespace std;
typedef long long ll;

int main()
{
    int a;
    cin >> a ;
    ll ans = 1;
    for (int i = 1; i <= a; i++)
        ans *= i;
    cout << ans;
    return 0;
}
