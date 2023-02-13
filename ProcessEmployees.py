'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile = open("employee_data.csv", "r")
employee = csv.reader(infile, delimiter=",")
next(employee)


#create an empty dictionary
employee_dict = {}
for x in employee:
    name = x[1] + " " + x[2]
    current_salary = x[5]
    new_salary = float(current_salary) * 1.1
    employee_dict[name] = {"New Salary": new_salary}
    

#use a loop to iterate through the csv file


print(employee_dict)


    #check if the employee fits the search criteria


    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout



          
        

        
    
