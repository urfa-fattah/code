# code
GCD Problem:
#include<stdio.h>
int main(){
    int A,B;
    scanf("%d %d",&A,&B);
    int j=A*B;
    for(int i=j-1;i>=1;i--){
        if(i==A||i==B){
            continue;
        }
        else if(A%i==0 && B%i==0){
            printf("%d",i);
            break;
        }
    }
}
divisor problem:
#include<stdio.h>
int main(){
    int N;
    scanf("%d",&N);
    for(int i=1;i<=N;i++){
        if(N%i ==0){
            printf("%d\n",i);
        }
    }
}
prime:
#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);
    for (int j = 2; j <= N; j++)
    {
        int flag = -1;
        for (int i = 2; i < j; i++)
        {
            if (j % i == 0)
            {
                flag = 1;
            }
        }
        if (flag == -1)
        {
            printf("%d ", j);
        }
    }
    return 0;
}
factorial:
#include<stdio.h>
int main(){
    int T,N;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%d",&N);
        long long F=1;
        for(int j=1;j<=N;j++){
            F=F*j;
        }
        printf("%lld\n",F);
    }
    return 0;
}
