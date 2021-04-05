#include <iostream>
#include <iomanip>

using namespace std;

int main(void)
{
    cout << fixed;
    cout << setprecision(5);
    double A, B, MEDIA;
    cin >> A;
    cin >> B;

    MEDIA = ((A * 3.5) + (B * 7.5)) / (3.5 + 7.5);
    cout << "MEDIA = " << MEDIA << endl;
}