# Gurobi Model for OSM Healthcare Navigator Project

# Import the gurobipy library
from gurobipy import *
import csv

# Step 1: Data

# Read in csv file. The 'rU' option makes sure the text fields are read in properly
file = open("Income_data.csv", 'rU')
csvFile = csv.reader(file)

# Pull out headers
Header = csvFile.next()

# Make a multidict with all information

# Fix data type for certain fields

# User-specified parameters of the problem. These need to be selected through expert knowledge, trial-and-error, or a multi-objective approach.

# Step 2: Create Model

PortfolioModel = Model("Healthcare Optimization Model")

# Step 3: Create Decision Variables

# Step 4: Update

PortfolioModel.update()

# Step 5: Objective

RiskScoreRank = 0

TargetPopulationWeight = 0
TargetPopulation = 0

PortfolioModel.setObjective(RiskScoreRank + (TargetPopulationWeight*TargetPopulation), GRB.MAXIMIZE)

# Step 6: Constraints


# Step 7: Solve the model!

PortfolioModel.optimize()

# Step 8: Print the solution.


