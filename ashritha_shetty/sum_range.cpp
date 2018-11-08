/*
Created on Novemberer 08, 2018
@author: ashritha27
*/
//Program to find the sum of numbers in a given range in C++
#include <iostream>

using namespace std;

int main()
{
    //Declaring the range variables and initialising the sum variable
    int min,max,sum=0;
    
    cout<<"Enter the limits";
    
    //Read the minimum and maximum input
    cin>>min;
    cin>>max;
    
    //Summing all the numbers in the given range using for loop
    for(int i=min;i<=max;i++)
    {
         sum+=i;
    }
    
    //Prints the sum of numbers in the given range 
    cout<<sum;
    
    return 0;
}
