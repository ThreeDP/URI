#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

#define n 3.14159

int main() {
    cout << fixed;
    cout << setprecision(4);
    double A, R;


    cin >> R;
    A = n * pow(R, 2.00);
    cout << "A=" << A << "\n";
    
    cin.get();
    return 0;
}