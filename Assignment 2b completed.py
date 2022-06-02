#!/usr/bin/env python
# coding: utf-8

# ####Q1 :
# 
# Below are the dummy data given. Implement each of the function. Retun the sum from the function and print the sum.
# 
# data_list = [1, 2, 99, -1, -20] data_tuple = (1, 2, 99, -1, -20) data_set = {1, 2, 99, -1, -20}
# 
# def sum_of_numbers():
# 
# return sum 
# def sum_of_abs_value(): pass
# 
# def sum_of_neg_numbers(): pass
# 
# def sum_of_pos_numbers(): pass

# In[60]:


data_list = [1, 2, 99, -1, -20] 
def sum_of_numbers(data_list):
    if (len(data_list)==1):
     return data_list[0]
    else:
     return data_list[0] + sum_of_numbers(data_list[1:])
print("Sum of numbers in a list is",sum_of_numbers( data_list))

pass
def sum_of_abs_value(data_list):
    if (len(data_list)==1):
     return data_list[0]
    else:
     return abs(data_list[0] + sum_of_numbers(data_list[1:]))
print("Absolute Sum of numbers in a list is",sum_of_abs_value(data_list))

pass

def sum_of_neg_numbers(data_list):
    sum = 0
    for x in data_list:
        if x < 0:
            sum=sum+x
    return(int(sum))
           
print("Sum of negative numbers in a list is",sum_of_neg_numbers( data_list))
pass

def sum_of_pos_numbers(data_list): 
    sum = 0
    for x in data_list:
        if x > 0:
            sum=sum+x
    return(int(sum))
           
print("Sum of positive numbers in a list is",sum_of_pos_numbers( data_list))


# In[58]:


data_tuple = (1, 2, 99, -1, -20)
def sum_of_numbers(data_tuple):
    if (len(data_tuple)==1):
     return data_tuple[0]
    else:
     return data_tuple[0] + sum_of_numbers(data_tuple[1:])

print("Sum of numbers in a tuple is",sum_of_numbers(data_tuple ))
pass

def sum_of_abs_numbers(data_tuple):
    if (len(data_tuple)==1):
     return data_tuple[0]
    else:
     return abs(data_tuple[0] + sum_of_numbers(data_tuple[1:]))
    
print("Absolute Sum of numbers in a tuple is",sum_of_abs_value( data_tuple))

pass

def sum_of_neg_numbers(data_tuple):
    sum = 0
    for x in data_tuple:
        if x < 0:
            sum=sum+x
    return(int(sum))
           
print("Sum of negative numbers in a tuple is",sum_of_neg_numbers( data_tuple))
pass

def sum_of_pos_numbers(data_tuple): 
    sum = 0
    for x in data_tuple:
        if x > 0:
            sum=sum+x
    return(int(sum))
           
print("Sum of positive numbers in a tuple is",sum_of_pos_numbers( data_tuple))


# In[80]:


data_set = {1, 2, 99, -1, -20}

s=sum(data_set)
print("Sum of numbers ina  set is ",s)


# In[ ]:


Q2 : Build a dictionary listing all the states of USA eg: states = {'CA' :'CALIFORNIA', 'NY' : 'NEW YORK'}

implement the below functions

return the result for each of the following. Print the result after each function call.

def get_all_states(): pass

def get_total_num_states(): pass

def get_states(state1): pass

def get_states(state1, state2) pass

def get_states(state1, state2, ..) pass

ca Ny ny


# In[3]:


states={'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut',
    'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
    'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine',
    'MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MS': 'Mississippi','MT': 'Montana','NC': 'North Carolina',
    'ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada',
    'NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','RI': 'Rhode Island','SC': 'South Carolina',
    'SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia',
    'VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}

def get_all_states(states):

    
    state_value=states.values()
    return(list(state_value))
print("All states in US is ",
get_all_states( {'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut',
    'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
    'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine',
    'MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MS': 'Mississippi','MT': 'Montana','NC': 'North Carolina',
    'ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada',
    'NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','RI': 'Rhode Island','SC': 'South Carolina',
    'SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia',
    'VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}))
pass


def get_total_num_states(states):

    state_num=len(states.values())
    return(state_num)
print("Total Number of states in US are ",get_total_num_states({'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut',
    'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
    'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine',
    'MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MS': 'Mississippi','MT': 'Montana','NC': 'North Carolina',
    'ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada',
    'NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','RI': 'Rhode Island','SC': 'South Carolina',
    'SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia',
    'VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}))

pass

def get_states(states):
    first_item = list(states.items())[0]
    return(first_item)
print("First state",get_states({'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut',
    'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
    'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine',
    'MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MS': 'Mississippi','MT': 'Montana','NC': 'North Carolina',
    'ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada',
    'NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','RI': 'Rhode Island','SC': 'South Carolina',
    'SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia',
    'VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}))
pass   


   


# In[ ]:


Q3

a. What are different scope of the variables in functions. b. List the difference between global variable and local variable c. 
Use list (with dunny data) and demostrate programatically how the global variable and local variables differs


# #a. What are different scope of the variables in functions
# 
# There are 4 types of scope of variables in python
# 
# 1.Local Scope
# The Variables which are defined in the function and function body 
# 
# 
# 2.Global Scope
# The Variable which can be read from anywhere in the program is known as a global scope and accessed anywhere in the function
# 
# 3.NonLocal or Enclosing Scope. 
# It is defined in the nested function
# 
# 
# 4.Built-in Scope. 
# If a Variable is not defined in local, nonlocal or global scope then  looks for it in the built-in scope.

# In[6]:


#Global variable

x = ["apple",0,1]

def myfunc():
  x = ["plum",2,4]
  print("Python is ", x)

myfunc()

print("Python is ", x)

#variable with the same name inside a function will be local and can only be used inside the function. 
#global variable(x=["apple",0,1]) with the same name will remain as it is.


# #Q4. List different file operations available in python. 
# #(List the maximum you can) Use a sample text file, and demonstrate the above. (Use the most often used file operations)
# 
# The different Python file operations are open (), close (), read (), readlines (), remove (), 
# truncate(), tell (), next ()
# 
# #Opening a File
# 
# In python open() is used to open a file in python and it can take two arguments , the file path including the file name and file extension with type string and mode to open the string
# 
#         Syntax: open("mytextfile.txt") 
# The different modes that can be used in an open function are -r, -w, -a.
# 
# -r mode
# 
# In r mode file opens with read mode .
# 
#     Syntax:open("mytextfile.txt", r)
# 
# -w mode
# 
# In w mode file opens in a write mode and removes the existing content .
# 
# -a mode
# 
# In a mode file the file opens in append mode and adds to existing file.
# 
# #Closing a file
# 
# In python close() is used to close a file after performing the reading and writing operations.
# 
#     Syntax:file = open("myfile.txt", 'r')
#                   print(file.read())
#                   file.close()
#                   
# #reading a file
# 
# Before start reading the file, as discussed, we must open the file in ‘r’ mode, since we are going to read the contents of the file. 
# 
#            Syntax: file = open("myfile.txt", "r")
#                    print(file.read())
#                    
# #readlines ()
#  .readline()method focuses on reading individual lines from a file.
#      
#          Syntax:file = open("myfile.txt", 'r')
#                        print(file.readlines())
# #write()
# 
# If we want to add content to our existing file, myfile.txt, first we need to open it in the ‘w’ write mode and use the .write() method on our file. The content to be written into the file needs to be passed as a string.
# 
#     Syntax:file=open("myfile.txt",'w')
#             print(file.write("Thats what i write))
#                        
# #remove()
# 
# Remove the files from a directory using Python’s versatile os module. 
# 
#         Syntax:import os
#                os.remove('myfile.txt')
#                file = open('myfile.txt', 'r')                
# 
# 
#         
# 
# 
# 

# In[48]:


#Example

myfile=open("C:/Users/steph/DataScience_2022/FileOperation.txt","r")
print(myfile.read())
print(myfile.readline())


# In[51]:


myfile=open("C:/Users/steph/DataScience_2022/FileOperation.txt","w")
print(myfile.write("Hello I'm writing"))

myfile.close()


# In[52]:


import os
os.remove("C:/Users/steph/DataScience_2022/FileOperation.txt")
file = open("C:/Users/steph/DataScience_2022/FileOperation.txt", 'r')

##file has been removed so it throws error


# #5 :
# 
# Use sys module and determine
# 
# a. current working directory b In the same location follow the below steps : 
#     a. Create a empty text file 
#     b. Add a sample paragraph from a news article (from internet)
#     c. Edit two lines in the above paragraph 
#     d. Add a paragraph again from a news article (from internet)

# In[37]:


#a. current working directory
import os
print(os.getcwd())


# In[59]:


#a. Create a empty text file 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

try:
    #f = open("Sample4.txt", "x")
    
    #b.Add a sample paragraph from a news article
    f=open("C:/Users/steph/May17/Sample.txt","w")
    print(f.write("Believing her 8-year-old daughter didn’t love her anymore, a Chicago woman axphyxiated her after they said prayers before bed in the Uptown neighborhood earlier in the week, prosecutors said Friday during the woman’s bond hearing.Andreal R. Hagler, 38, was charged with first-degree murder and was denied bail before Cook County Judge Maryam Ahmad during a hearing livestreamed on YouTube.")
    )    
 
    #c. Edit two lines in the above paragraph 
    f=open("C:/Users/steph/May17/Sample.txt","r+")
    oldpara=f.read()
    f.seek(0)
    print(f.write("A Chicago woman axphyxiated her after they said prayers before bed in the Uptown neighborhood earlier in the week, prosecutors said Friday during the woman’s bond hearing.Andreal R. Hagler, 38, was charged with first-degree murder and was denied bail."+oldpara))
    #d. Add a paragraph again from a news article (from internet) 
    f= open("C:/Users/steph/May17/Sample.txt", "a")
    
    f.write(" \n Assistant State’s Attorney James Murphy said the victim’s uncle, who sometimes stayed with them, came to their apartment Wednesday morning in the 4600 block of North Winthrop Avenue to check on Hagler after calling several times and not getting a response.")
    #newline added to add as a new para
    f=open("C:/Users/steph/May17/Sample.txt","r+")
    
    content=print(f.read())
    
    
    f=open("C:/Users/steph/May17/Sample.txt","r+")
    #content=print(f.read())
    #content
    cloud=WordCloud().generate(f.read())
    plt.imshow(cloud)
    plt.show()
  
finally:
    f.close()
    


# In[2]:


get_ipython().system('pip install wordcloud')


# In[32]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

text="When masses gather and wait dutifully to catch a glimpse of Her Majesty,the color she steps out in is more important than you might think, too.Standing at 5 feet 3 inches, vivid hues like yellow, fuschia, purple, chartreuse and periwinkle make her easier to spot in large crowds. The Queen's bold wardrobe is so distinctive, it has spawned entire books dedicated to recording each beaming outfit. In Our Rainbow Queen, Welsh journalist Sali Hughes notes Her Majesty's color wheel considerations: (she) won't wear green to grassy venues, nor dark colours against dark upholstery."

cloud=WordCloud().generate(text)
plt.imshow(cloud)
plt.show()


# In[ ]:




