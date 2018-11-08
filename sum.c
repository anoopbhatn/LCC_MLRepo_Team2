//program to find the sum inclusive of the start and the end no. mentioned
/*
Created on november 8, 2018
@author: sumangala rao
*/
#include<stdio.h>
  int main()
   {
     int n1,n2,i,sum=0;         //initialization
     scanf("%d %d",&n1,&n2);    //taking user input
       //computing sum
     for(i=n1;i<=n2;i++)
        sum=sum+i; 
     printf("%d",sum);           //display the sum
    return 0;
   }
