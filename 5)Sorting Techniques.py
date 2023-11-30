#bubble sort
def bubble(arr,n):
	for i in range(n-1):
		for j in range(n-i-1):
			if(arr[j]>arr[j+1]):
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	print(arr)

# insertion sort
def insert(arr,n):
	for i in range(1,n):
		temp = arr[i]
		j = i-1
		while(j>=0 and  arr[j]>temp):
			arr[j+1] = arr[j]
			j = j-1
		arr[j+1] = temp
	print(arr)


#selection sort
def select(arr,n):
	for i in range(0,n):
		mid = i
		for j in range(i+1,n):
			if(arr[j]<arr[mid]):
				mid = j
		temp = arr[i]
		arr[i] = arr[mid]
		arr[mid] = temp
				
	print(arr)
# quick sort
def partition(arr,low,high):
	pivot = arr[high]
	i = low -1
	for j in range(low,high):
		if arr[j]<=pivot:
			i = i + 1
			(arr[i],arr[j]) = (arr[j],arr[i])
	(arr[i+1],arr[high]) = (arr[high],arr[i+1])
	return i + 1
def quick(arr,low,high):	
	if(low<high):
		pi  = partition(arr,low,high)
		quick(arr,low,pi-1)
		quick(arr,pi+1,high)
	
		
				
arr = [20,12,15,13]
print("the origial array")
print(arr)
n = len(arr)
#bubble(arr,n)
#insert(arr,n)
#select(arr,n)
#quick(arr,0,n-1)
print("the sorted array is")
print(arr)

				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				

