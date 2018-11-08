/*
Created on november 8, 2018
@author: sumangala rao
*/
//program to find the sum inclusive of the start and the end no. mentioned
#include<stdio.h>

int main()
{
     //initialization
     int n1,n2,i,sum=0;
    
     //taking user input
     scanf("%d %d",&n1,&n2);
    
     //computing sum
     for(i=n1;i<=n2;i++)
          sum=sum+i;
    
     //display the sum
     printf("%d",sum);  
    
     return 0;
}
