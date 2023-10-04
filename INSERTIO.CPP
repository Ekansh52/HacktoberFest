#include <bits/stdc++.h>

using namespace std;

int binarySearch (int ar [], int n, int x) {
    int low = 0, high = n - 1, mid;

    while (low <= high) {
        mid = (low + high) / 2;

        if (ar [mid] == x) {
            return mid;
        }

        else if (mid < x) {
            low = mid + 1;
        }

        else {
            high = mid - 1;
        }
    }

    return -1;
}

int main () {
    int n, x;

    cout << "Enter number of elements : ";
    cin >> n;

    int ar [n];

    cout << "Enter elements : \n";

    for (int i = 0; i < n; i++) {
        cin >> ar [i];
    }

    cout << "Enter element to search : ";
    cin >> x;

    cout << "found at index : " << binarySearch (ar, n, x) << endl;

    return 0;

}
