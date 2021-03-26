#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

#define n 3.14159

int main() {
    float A, R;
    cout << setprecision(8);
    setiosflags(ios::left);
    setiosflags(ios::showpoint);
    cin >> R;
    
    A = n * pow(R, 2.0);
    cout << "A=" << A << "\n";
    
    cin.get();
    return 0;
}