# Gurobi Model for OSM Healthcare Navigator Project

# Import the gurobipy library
from gurobipy import *
import csv

# Step 1: Data

# Read in csv file. The 'rU' option makes sure the text fields are read in properly
file = open("combined_data.csv", 'rU')
csvFile = csv.reader(file)

# Pull out headers
Header = csvFile.next()

# Make a multidict with all information
County, HealthRank, TargetPop, TotalPop, AvgIncome = multidict({row[0]: row[1:len(Header)] for row in csvFile})

for c in County:
    HealthRank[c] = float(HealthRank[c])
    TargetPop[c] = float(TargetPop[c])
    TotalPop[c] = float(TotalPop[c])
    AvgIncome[c] = float(AvgIncome[c])

file = open("income_data.csv", 'rU')
csvFile = csv.reader(file)

# Pull out headers
Header = csvFile.next()

# Make a multidict with all information
County, HealthRank, TargetPop, TotalPop, AvgIncome = multidict({row[0]: row[1:len(Header)] for row in csvFile})

for c in County:
    HealthRank[c] = float(HealthRank[c])
    TargetPop[c] = float(TargetPop[c])
    TotalPop[c] = float(TotalPop[c])
    AvgIncome[c] = float(AvgIncome[c])

# User-specified parameters of the problem. These need to be selected through expert knowledge, trial-and-error, or a multi-objective approach.


# Step 2: Create Model
NavigatorModel = Model("Healthcare Navigator Optimization Model")

# Step 3: Create Decision Variables
NumNavigators = dict.fromkeys(County,0)

for c in County:
	NumNavigators[c] = NavigatorModel.addVar(vtype=GRB.INTEGER, name = "NumNavigators_"+c)

# Diminishing returns piecewise function
ConversionRate1 =  dict.fromkeys(County,0)
ConversionRate2 = dict.fromkeys(County,0)
ConversionRate3 = dict.fromkeys{County,0}

# Step 4: Update
NavigatorModel.update()

# Step 5: Objective (which we are trying to MAXIMIZE)
TotalHealthRank = 0

TargetPopulationWeight = 0 #this is the weight for the multi-objective function
TotalTargetPopulation = 0 #weighted-average insured rate

for c in County:
	TotalHealthRank += HealthRank[c] * NumNavigators[c] * ConversionRate[c]

NavigatorModel.setObjective(TotalHealthRank + (TargetPopulationWeight*TotalTargetPopulation), GRB.MAXIMIZE)

# Step 6: Constraints

# budget*number of navigators < total budget
# navigators per capita constraint < some absolute value


# Step 7: Solve the model!
NavigatorModel.optimize()

# Step 8: Print the solution.

