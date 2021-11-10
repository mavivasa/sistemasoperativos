import os
import pandas as pd

#Functions to be created

function1 = ['OS name, for instance: "posix", "nt", "dos", etc.', os.name]
function2 = ['Current Process ID', os.getpid()]
function3 = ['Get parent process ID', os.getppid()]
function4 = ['Current working directory for current of a process', os.getcwd()]
function5 = ['Number of CPUs installed in current executing system', os.cpu_count()]

#Function array holding function descriptions along with results

functions = [function1,function2,function3,function4,function5]

#Excel file to hold results

file = pd.ExcelWriter('OSInformation.xlsx', engine='xlsxwriter')

#Arrays are embedded inside a Dataframe to be written into the Excel file

df = pd.DataFrame([function1, function2, function3, function4, function5],columns=['Function Description', 'Result'])
df.to_excel('OSInformation.xlsx')
