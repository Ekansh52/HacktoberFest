// C++ implementation to generate 
// an array of size N by following 
// the given rules 
#include <bits/stdc++.h> 
using namespace std; 

// Function to search the most recent 
// location of element N 
// If not present in the array 
// it will return -1 
int search(int a[], int k, int x) 
{ 
	int j; 
	
	for ( j = k - 1; j > -1 ; j--) 
	{ 
		if(a[j] == x) 
			return j ; 
	} 
				
		return -1 ; 
} 

// Function to generate an array 
// of size N by following the given rules 
void genArray(int arr[], int N) 
{ 

	// Loop to fill the array 
	// as per the given rules 
	for(int i = 0; i < N - 1; i++) 
	{ 

		// Check for the occurrence 
		// of arr[i - 1] 
		if(search(arr, i, arr[i]) == -1) 
				arr[i + 1] = 0 ; 

		else
			arr[i + 1] = (i-search(arr, i, arr[i])) ; 
	} 
} 

// Driver code 
int main() 
{ 
	int N = 5 ; 
	int size = N + 1 ; 
	int a[] = {0, 0, 0, 0, 0}; 
	genArray(a, N) ; 
	
	for (int i = 0; i < N ; i ++) 
		cout << a[i] << " " ; 
		return 0; 
} 


// This code is contributed by shivanisinghss2110 
