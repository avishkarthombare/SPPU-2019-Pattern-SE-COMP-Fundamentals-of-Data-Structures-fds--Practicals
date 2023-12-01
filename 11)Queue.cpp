#include<iostream>
#define MAX 3
using namespace std;
 
struct Que{
int queue[MAX];
}s;

class Queue{
public: int ele,i;
int r,f;    
void insert();
void del();
void display();
Queue() {
r=f=-1;
}
};
void Queue::insert(){
if(r == MAX-1){
cout<<"QUEUE IS FULL"<<endl;
}else{
cout<<"Enter the job element:";
cin>>ele;
r=r+1;
s.queue[r]=ele;
}
 
if(r == 0){
	f=0;
}
}
void Queue::del(){
if(f==-1){
cout<<"QUEUE IS EMPTY"<<endl; 
}else
{ 
cout<<"DELETED JOB IS:"<<s.queue[f]<<endl;
f=f+1;
}

if(f>r) {
cout<<"QUEUE IS EMPTY"<<endl;
}
}
void Queue::display(){
cout<<"JOB QUEUE IS:";
for(i=f;i<=r;i++){
cout<<s.queue[i];
}
}

int main() {

int ch;
Queue q;
do{
 
cout<<"\n-----MENU-----"<<endl;
 
cout<<"1.INSERT THE JOB IN THE QUEUE"<<endl;
 
cout<<"2.DELETE THE JOB IN THE QUEUE"<<endl;
 
cout<<"3.DISPLAY THE QUEUE"<<endl;
 
cout<<"4.EXIT"<<endl;
 
cout<<"Enter the choice:";
 
cin>>ch;
 
switch(ch){ 
case 1: 
q.insert(); 
break;
 
case 2:
q.del();
break;
 
case 3:
q.display();
break;
 
case 4:
return 0;
break;

default: cout<<"INVALID CHOICE"<<endl; 
break;
}
}while(ch!=4);
return 0;
}

