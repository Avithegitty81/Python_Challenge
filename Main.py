import os
import csv

# set the file path
budget_data = os.path.join("..", "Resources","budget_data.csv")

 



    Total_month= 0
    Total_profit=0
    Previous_net=0
    Greatest_increase=[" ",0]
    Greatest_decrease=[" ",999999999999999]
    month_change=[]
    netchange_list=[]

    #open the file
    with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    #skip the  header
    header  =  next(csvreader)

    # skip the first row data
    firstrow = next(csvreader)

# counting the no. of months in  the data
    Total_month +=1
    Total_profit += int(firstrow[1])
    Previous_net += int(firstrow[1]
   
    for row in csv_reader:
        Total_month +=1
        Total_profit += int(row[1])

        #calculate average change

        netchange   = int(row[1]) - Previous_net
        Previous_net = int(row[1])

        #creating  a list of net change 
        netchange_list = netchange_list  + [netchange]
        month_change = month_change  + [row[0]
    
# Calculating Greatest Increase & Decrease in Profit: 

       Date= []
       Profit_Loss= []
       Inc=[]
       for row in csv_reader:
           dt=row[0]
           profit_loss= row[1]
           Date.append(dt)
           Profit_Loss.append(profit_loss)

           for i in range(len(Profit_Loss)-1):
               inc=int(Profit_Loss[n+1])- int(Profit_Loss[n])
               Inc.append.(inc)
               Greatest_profit=max(Inc)
               Greatest_profit_date= date[inc.index(Greatest_profit)+1]
               print Greatest_profit=Greatest_profit_date + (Greatest_profit)
               Greatest_decrease = min(Inc)
               Greatest_decrease_date=date[inc.index(Greatest_decrease)+1]
               print Greatest_decrease= Greatest_decrease_date + (Greatest_decrease)
     netmonthlyaverage = sum(netchange_list)/len(netchange_list)         
      

        print("Financial Analysis")
        print("----------------------------") 
        print("Total:" + " ",(Total_month))
        print("Total:" + " "  + "${:,.2f}.format(Total_profit))
        print("Average:" + " " + "${:,.2f}.format(netmonthlyaverage))
        print("Greatest_increase:" + " " + str(Greatest_increase))
        print("Greatest_Decrease:" + " " + str(Greatest_decrease))


        #Publish summary through  csvfile:
        
        with open(file_to_output, "w") as csvfile:
           csvwriter  = csv.writer(csvfile,  delimiter=',')


