fds = []
num = int(input("Enter number of students :"))
for i in range(num):
    x = int(input("Enter marks of students"+str(i+1)+":"))
    if x==-1:
        print("Student is absent")
        fds.append(x)
    elif(x>=0 and x<=30):
        fds.append(x)
    else:
        print("Invalid input !")
def avg(fds):
    sum = 0
    count = 0
    for i in range(num):
        if fds[i]!=-1:
            sum+=fds[i]
            count+=1
    avg = sum/count
    print("The Average of marks of students is : ",avg)
def absent(fds):
    count = 0
    for i in range(num):
            if(fds[i]==-1):
                count+=1
               
    print("Number of absent student is :",count)
def marks_with_highest_frequency(fds):
    freq = 0
    for i in range(len(fds)):
        count = 0
        if(fds[i]!=-1):
            for j in range(len(fds)):
                if(fds[i]==fds[j]):
                    count+=1
        if(freq<count):
            marks = fds[i]
            freq = count
    print("\Highest frequent marks",marks)
    print("Frequency of marks",freq)
def min_max(fds):
	min = 31
	max =-1
	for i in range(0,len(fds)):
		if(fds[i]!=-1):
			if(min>fds[i] and fds[i]!=-1):
				min=fds[i]
			if(max <fds[i]):
				max = fds[i]
	print("Minimum marks is",min)
	print("Maximum marks is",max)
while True:  
    print("Enter your choice")
    print("choice 1:Calculate average")
    print("choice 2:Calculate frequency")
    print("choice 3:Calculate max marks and min marks ")
    print("choice 4:Calculate absent")
    print("choice 5: Exit")
    choice = int(input("Enter your choice digit"))
    if choice == 1:
	    avg(fds)
    elif choice == 2:
	    marks_with_highest_frequency(fds)
    
    elif choice == 3:
	    min_max(fds)
    elif choice == 4:
	    absent(fds)
    elif choice ==5:
	    print("Thankyou for using code created by Avishkar!")
	    break
    else:	
	    print("Plz Enter valid choice")
	

    
