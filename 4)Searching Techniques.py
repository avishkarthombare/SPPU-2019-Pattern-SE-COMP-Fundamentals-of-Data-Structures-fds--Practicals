
def linear_search(A,n,x):
	
	for i in range(n):
		if(x==A[i]):
			print("The Element is found at : ",i)
		else:
			print("Element not found !")


def sentinel_search(A,n,x):
	last = A[n-1]
	A[n-1] == x
	i=0
	while(A[i]!=x):
		i = i+1
	A[n-1] == last
	if(i<n-1)or(x==A[n-1]):
		print("Element found at : ",i)
	else:
		return -1
	


	
def binary(A,n,x):
	start = 0
	end = n-1
	
	while(start<=end):
		mid =int((start + end)/2)
		if(x==A[mid]):
			print("Element found at :",mid)
		elif(x>A[mid]):
			start = mid+1
		else:
			end =mid-1
			
def fibonaccisearch(A,n,x):
	
	start=-1
	f0=0
	f1=1
	f2=1
	
	while(f2<len(A)):
		f0=f1
		f1=f2
		f2=f1+f0
	
	while(f2>1):
		i=min(start+f0,len(A)-1)
		if (A[i]<x):
			f2=f1
			f1=f0
			f0=f2-f1
			start=i
		elif (A[i]>x):
			f2=f0
			f1=f1-f0
			f0=f2-f1
		else:
			return i
		
		if (f1) and (A[len(A)-1]==x):
			return len(A)-1
		
		
		
#main function
A = []
n = int(input("Enter the number of elements"))

for i in range(n):
	element = int(input(""))
	A.append(element)
x = int(input("Enter the element to be Searched"))
print("Choose your choice for type of search")
print("choice 1:Linear search")
print("choice 2:Sentinel search")
print("choice 3:Binary search")
print("choice 4:Fibonacci search")
print("choice 5:EXIT")
ch = int(input("Enter your desired choice"))
if(ch==1):
	linear_search(A,n,x)
elif(ch== 2):
	sentinel_search(A,n,x)
elif(ch == 3):
	binary(A,n,x)
elif(ch == 4):
	print(fibonaccisearch(A,n,x))
	
elif(ch==5):
	print("Thanks for using Code done by Avishkar")
else:
	print("Enter valid input!")
