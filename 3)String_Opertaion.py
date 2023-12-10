str = "Python is not so fun"
def  longest_word(str):
    m_str = ''
    i = 0
    while(i<len(str)):
        word =" "
        word +=str[i]
        i=i+1
        if(i==len(str)):
            break
        if(i!=len(str)):
            while(str[i] == " "):
                i = i+1
        if(len(m_str)<len(word)):
            m_str = word
    print("the longest word is",m_str,len(m_str))

def char_occur(str):
    strin = input("enter the string:")
    char = input("enter the charecter:")
    count = 0
    for i in range(len(str)):
    	if(str[i]==char):
    	  count+=1
    print("the count of the substring" ,char,"in the string ",strin ,"is",count)
def palindrome(str):
    strin = input("enter the string:")
    b = 0
    e = len(str)-1
    while(True):
        if(strin[b]!=str[e]):
            break
        b+=1
        e-=1
        if(b<e):
            print("string is not palindrome")
        else:
            print("given string is palindrome")	 


def occur(str):
	word_array=[]
	count = []
	i = 0
	while(i<len(str)):
		word = ""
		while(str[i]!=" "):
			word +=str[i]
			i = i+1
			if(i==len(str)):
				break
		if(i!=len(str)):
			while(str[i]==" "):
				i = i+1
		if(len(word_array)==0):
			word_array.append(word)
			count.append(1)
		else:
			flag=1
			for j in range(len(word_array)):
				if(word_array[j]==word):
					count[j] +=1
					flag = 0
			if(flag==1):
				word.array_append(word)
				count.appen(1)
	print(word_array)
	print(count)
choice = int(input("enter your choice"))
if(choice==1):
	occur(str)
	
	
		
