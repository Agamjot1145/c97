introString=input("Enter your introduction: ")
characterCount=0
wordCount=3
for i in introString:
         characterCount=characterCount+1
         if(i==''):
             wordCount=wordCount+1
print("Number of words in the string : ")
print(wordCount)
print("No. of characters in the string: ")
print(characterCount)