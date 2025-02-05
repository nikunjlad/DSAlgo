/*
Given an array of integers, find the largest element in the array.
*/

#include <iostream>
#include <algorithm>

using namespace std;

// BRUTE FORCE:
int largestElement(vector<int> &arr, int n) {

    // sort the numbers in ascending order
    sort(arr.begin(), arr.end());

    return arr[n-1];

}

int main(){
    vector<int> arr1 = {1, 8, 7, 56, 90};
    vector<int> arr2 = {5, 5, 5, 5};
    vector<int> arr3 = {10};

    cout << largestElement(arr3, 1) << endl;
    return 0;
}

