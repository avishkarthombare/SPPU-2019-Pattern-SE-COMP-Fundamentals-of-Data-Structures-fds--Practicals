fds = []
num = int(input("enter number of students"))
for i in range(num):
    x = int(input("enter marks of students"+str(i+1)+":"))
    if x==-1:
        print("student is absent")
        fds.append(x)
    elif(x>=0 and x<=30):
        fds.append(x)
    else:
        print("invalid input")
def avg(fds):
    sum = 0
    count = 0
    for i in range(num):
        if fds[i]!=-1:
            sum+=fds[i]
            count+=1
    avg = sum/count
    print("the saverage of marks of students is:",avg)
def absent(fds):
    count = 0
    for i in range(num):
            if(fds[i]==-1):
                count+=1
               
    print("number of absent student is:",count)
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
    print("highest frequent marks",marks)
    print("frequency of marks",freq)
def min_max(fds):
	min = 31
	max =-1
	for i in range(0,len(fds)):
		if(fds[i]!=-1):
			if(min>fds[i] and fds[i]!=-1):
				min=fds[i]
			if(max <fds[i]):
				max = fds[i]
	print("minimum marks is",min)
	print("maximum marks is",max)
while True:  
    print("enter your choice")
    print("choice 1:calculate average")
    print("choice 2:calculate frequency")
    print("choice 3:calculate max marks and min marks ")
    print("choice 4:calculate absent")
    print("choice 5: exit")
    choice = int(input("enter your choice digit"))
    if choice == 1:
	    avg(fds)
    elif choice == 2:
	    marks_with_highest_frequency(fds)
    
    elif choice == 3:
	    min_max(fds)
    elif choice == 4:
	    absent(fds)
    elif choice ==5:
	    print("thankyou for using")
	    break
    else:	
	    print("enter valid choice")
	

    