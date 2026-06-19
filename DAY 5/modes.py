# # OPEN MODE 
# file = open('C:/Users/SRIRI/OneDrive/Desktop/AGENTIC AI/DAY 5/error.txt','r')
# content = file.read()
# print(content)
# file.close()

# WRITE MODE
# file1 = open('C:/Users/SRIRI/OneDrive/Desktop/AGENTIC AI/DAY 5/error.txt','w')
# content = input("Enter a data to write: ")
# file1.write(content)
# print("Data saved Successfully.")
# file1.close()

# With Statement 
with open('C:/Users/SRIRI/OneDrive/Desktop/AGENTIC AI/DAY 5/data.txt','w') as file:
    content = input("Enter your data to write in a file : ")
    file.write(content)
    print("saved!")