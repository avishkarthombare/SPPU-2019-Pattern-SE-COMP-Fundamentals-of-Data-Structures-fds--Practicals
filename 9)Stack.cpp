#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;
int top = -1;
char stack[100];

void push(char);
void pop();
void find_top();
int main()
{
int i;
char a[100];
cout<<"enter expression\n";
cin>>a;
for (i = 0; a[i] != '\0';i++)
{
if (a[i] == '('||a[i] == '{'||a[i] == '[')
{
push(a[i]);
}
else if (a[i] == ')'||a[i] == '}'||a[i] == ']')
{
pop();
}
}
find_top();
}

void push(char a)
{
stack[top] = a;
top++;
}

void pop()
{
if (top == -1)
{
cout<<"expression is invalid\n";
exit(0);
}
else
{
top--;
}
}

void find_top()
{
if (top == -1)
cout<<"expression is valid\n";
else
cout<<"\nexpression is invalid\n";
}

