#include<iostream>
#include<stdlib.h>
#include<cstring>
using namespace std;
int k = 0;//store the length of postfix expression
class stack// declare stack as ADT
{
char st[20];
int top;
public:
stack()
{
top=-1;
}
int empty()//check is stack empty or not
{
if(top==-1)
return 1;
return 0;
}
char gettop()//f7unction will return top element of stack
{
return st[top];
}
void push(char ch)//insert elemnet into stack
{
st[++top]=ch;
}
char pop()//removeing top value from stack
{ if(!empty())
return st[top--];
}
};
// get priority of operators as per precedence
// higher priority given to operators with higher precedence
// for non operators, return 0
int getpriority(char ch) {
switch (ch) {
case '/':
case '*': return 2;
case '+':
case '-': return 1;
default : return 0;
}
}
// convert infix expression to postfix using a stack
void infix2postfix(char infix[], char postfix[], int size)
{
stack s;
int priority;
int i = 0;
int k = 0;
char ch;
while (i < size)//read while infix expression not ended
{
ch = infix[i];
if (ch == '(') {// if left paranthesis occur---simply push the opening parenthesis
s.push(ch);
i++;
continue;
}
if (ch == ')') { // if right parenthesis encountered,
// pop of all the elements and append it to
// the postfix expression till we encounter
// a opening parenthesis
while (!s.empty() && s.gettop() != '(') {
postfix[k++] = s.gettop();
s.pop();
}
// pop off the opening parenthesis also
if (!s.empty()) {
s.pop();
}
i++;
continue;
}
priority = getpriority(ch);
if (priority == 0) { // we saw an operand
// simply append it to postfix expression
postfix[k++] = ch;
}
else { // we saw an operator
if (s.empty()) { // simply push the operator onto stack if
// stack is empty
s.push(ch);
}
else {
// pop of all the operators from the stack and
// append it to the postfix expression till we
// see an operator with a lower precedence that
// the current operator
while (!s.empty() && s.gettop() != '(' &&
priority <= getpriority(s.gettop())) {
postfix[k++] = s.gettop();
s.pop();
}
// push the current operator onto stack
s.push(ch);
}
}
i++;
} // pop of the remaining operators present in the stack
// and append it to postfix expression
while (!s.empty()) {
postfix[k++] = s.gettop();
s.pop();
}
postfix[k] = 0; // null terminate the postfix expression
}

// Stack type 
struct Stack 
{ 
	int top; 
	unsigned capacity; 
	int* array; 
}; 

// Stack Operations 
struct Stack* createStack( unsigned capacity ) 
{ 
	struct Stack* stack = (struct Stack*) malloc(sizeof(struct Stack)); 

	if (!stack) return NULL; 

	stack->top = -1; 
	stack->capacity = capacity; 
	stack->array = (int*) malloc(stack->capacity * sizeof(int)); 

	if (!stack->array) return NULL; 

	return stack; 
} 

int isEmpty(struct Stack* stack) 
{ 
	return stack->top == -1 ; 
} 

char peek(struct Stack* stack) 
{ 
	return stack->array[stack->top]; 
} 

char pop(struct Stack* stack) 
{ 
	if (!isEmpty(stack)) 
		return stack->array[stack->top--] ; 
	return '$'; 
} 

void push(struct Stack* stack, char op) 
{ 
	stack->array[++stack->top] = op; 
} 
// evaluates the postfix operation
int evaluatePostfix(char* exp) 
{ 
	// Create a stack of capacity equal to expression size 
	struct Stack* stack = createStack(strlen(exp)); 
	int i; 

	// See if stack was created successfully 
	if (!stack) return -1; 

	// Scan all characters one by one 
	for (i = 0; exp[i]; ++i) 
	{ 
		// If the scanned character is an operand (number here), 
		// push it to the stack. 
		if (isdigit(exp[i])) 
			push(stack, exp[i] - '0'); 

		// If the scanned character is an operator, pop two 
		// elements from stack apply the operator 
		else
		{ 
			int val1 = pop(stack); 
			int val2 = pop(stack); 
			switch (exp[i]) 
			{ 
			case '+': push(stack, val2 + val1); break; 
			case '-': push(stack, val2 - val1); break; 
			case '*': push(stack, val2 * val1); break; 
			case '/': push(stack, val2/val1); break; 
			} 
		} 
	} 
	return pop(stack); 
}
// main
int main() {
char infix[20];
cout<<"enter the infix expression";
cin>>infix;
int size = strlen(infix);
char postfix[size];
infix2postfix(infix,postfix,size);
cout<<"\nInfix Expression :: "<<infix;
cout<<"\nPostfix Expression :: "<<postfix;
cout<<"\nExpression evaluates to "<<evaluatePostfix(postfix);
cout<<endl;
cout<<endl;
return 0;
}
