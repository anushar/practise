str=raw_input("enter a string:")
n=len(str)
i=1
rev_str=""
#print str[::-1]  #extended slicing of sting to print string in reverse way
for i in range (1,n+1):
        rev_str+=str[-i]

print rev_str
