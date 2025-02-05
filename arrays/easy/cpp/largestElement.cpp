/*
Given an array of integers, find the largest element in the array.
*/

#include <iostream>
#include <algorithm>

using namespace std;

// BRUTE FORCE:
// Time Complexity: O(nlogn)
// Space Complexity: O(1)
// int largestElement(vector<int> &arr, int n) {

//     // sort the numbers in ascending order
//     sort(arr.begin(), arr.end());

//     return arr[n-1];

// }


// OPTIMAL:
// Time Complexity: O(n)
// Space Complexity: O(1)
int largestElement(vector<int> &arr, int n) {

    int largest = arr[0];

    for(int i=0; i<n; i++) {
        if(arr[i] > largest){
            largest = arr[i];
        }
    }

    return largest;

}


int main(){
    vector<int> arr1 = {1, 8, 7, 56, 90};
    vector<int> arr2 = {5, 5, 5, 5};
    vector<int> arr3 = {10};

    cout << largestElement(arr1, 5) << endl;
    return 0;
}

