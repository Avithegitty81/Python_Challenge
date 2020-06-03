import os
import csv
budget_data = os.path.join("..")

budget_data = os.path.join("../Resources","budget_data.csv");
csv_reader = csv.reader(csv_file, delimiter = ',')
 

with open(budget_data, 'r') as csv_file:
    Total_month= 0
    Total_amount=0
    Average_change=0
    Greatest_increase=0
    Greatest_decrease=0

    #  total number of months:
    Total_months=[]
    Total_amount=[]
    for row in csv_reader:
        Total_months.append(int(row [0])
        Total_amount.append(int(row[1]))
        Total_amount += int(row[1])
 

 # Calculating Average change:
 def Average(numbers):
     Average(number)= 0
     length=len(numbers)
     for number in numbers:
         total+= number
     return (total/length) 
    

  # Calculating Greatest Increase & Decrease in Profit: 

       Date= []
       P&L= []
       Inc=[]
       for row in csv_reader:
           dt=row[0]
           P&L= row[1]
           date.append(dt)
           P&L.append(p&l)

           for i in range(len(P&L)-1):
               inc=int(P&L[n+1])- int(P&L[n])
               Inc.append.(inc)
               Greatest_profit=max(Inc)
               Greatest_profit_date= date[inc.index(Greatest_profit)+1]
               print Greatest_profit=Greatest_profit_date + (Greatest_profit)
               Greatest_decrease = min(Inc)
               Greatest_decrease_date=date[inc.index(Greatest_decrease)+1]
               print Greatest_decrease= Greatest_decrease_date + (Greatest_decrease)
      

        print("Financial Analysis")
        print("----------------------------") 
        print("Total:" + " ",(Total_months))
        print("Total:" + " ", (Total_amount))
        print("Average:" + " ",(round(Average(Numbers))))
        print("Greatest_increase:" + " " + str(Greatest_increase))
        print("Greatest_Decrease:" + " " + str(Greatest_decrease))


        #Publish summary through text file:
        file_to_output = os.path.join("analysis", "PyBank_analysis.txt")
        with open(file_to_output, "w") as txt_file:
            txt_file.write(output)
            Save print files as
            output = (print .....
            print ....
            print ... )"/n"
    


