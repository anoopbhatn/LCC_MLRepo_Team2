//program to find the sum inclusive of the start and the end no. mentioned
#include<stdio.h>
int main()
{
int n1,n2,i,sum=0;
scanf("%d %d",&n1,&n2);
for(i=n1;i<=n2;i++)
sum=sum+i;
printf("%d",sum);
return 0;
}
