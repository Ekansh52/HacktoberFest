#include<stdio.h>
int a[10];
int top=-1;
void push(int x)
{
    if(top==9)
    {
        printf("overflow");
        return;
    }
    a[++top]=x;


}
void pop()
{
    if(top==-1)
    {
        printf("underflow");
        return;
    }
    top--;
}
int upper()
{
    return a[top];
}
void show()
{
    int i;
    printf("stack is");
    for(i=0;i<=top;i++)
    printf("%d    ",a[i]);
    
}
void main()
{
    push(2);
    show();
    push(3);
    show();
    push(4);
    show();
    pop();
    show();
    pop();
    show();
    int y=upper();
    printf("%d",y);
    pop();
    pop();
    show();


}