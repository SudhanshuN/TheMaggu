## TheMaggu.py
## @author SudhanshuAN
##
## Program description:
##          The progarm takes in a file listing RollNo and Marks in csv format
##          Enter Roll Numbers continously one by one
##          To stop, type in stop
##
## In Shell Window:
##          input: Roll No
##          output: Marks: _marks_, Rank: _rank_, Tied Between: _same_
##                  _marks_  Marks obtained by person with input RollNo
##                  _rank_   Rank obtained
##                  _same_   No of people having same rank
##
## Customisables:
##          file_name= name of input csv file (must be in same folder as the code) (default: "Marksheet.csv")
##          same_rank_allowed= Is same rank allowed??? (default: True)


import pandas as pd


file_name="Marksheet.csv"
same_rank_allowed = True



head=["RollNo","Marks"]                                                             ## Headers
data = pd.read_csv(file_name, names = head)                                         ## Import csv file
data['rnk_min'] = data['Marks'].rank(ascending=False, method='min')                 ## Find MINimum rank possible for a specific mark
data["rnk_max"] = data['Marks'].rank(ascending=False, method='max')                 ## Find MAXimum rank possible for a specific mark
data["same"] = data['rnk_max'] - data['rnk_min'] + 1                                ## Number of people having same rank

if same_rank_allowed:
    data['rank'] = data['Marks'].rank(ascending=False, method='dense')              ## If same rank is ALLOWED, then skip through the indices (ie dense mode)
else:
    data['rank'] = data['rnk_min']                                                  ## If NOT ALLOWED, then minimum possible rank is taken

RNoStr = input("Enter Roll Number: ")                                               ## First input

while (RNoStr.lower()!="stop"):                                                     ## Continue looping untill "stop" or any of it's uppercases is typed in
    if RNoStr.isnumeric():                                                          ## Check if input is a number
        argm=int(RNoStr) - 1                                                        ## Convert to number then to index
        if(argm>=0 and argm<1000):                                                  ## Check if in range
            print("Marks: {}, Rank: {}, Tied Between: {}".format(data['Marks'][argm],data['rank'][argm],data['same'][argm]))    ## Print out data
        else:
            print("You don't EXIST...\n...\n...\n...\n...\nIn the database :p")
    else:
        print("Roll Number is a NUMBER")
    
    RNoStr = input("Enter Roll Number: ")                                           ## Take data for next iteration

