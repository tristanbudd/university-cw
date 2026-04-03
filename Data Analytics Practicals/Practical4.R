# Installing Packages
install.packages("readxl")
install.packages("treemap")
install.packages("plotrix")
install.packages("tibble")
install.packages("ggplot2")
library(readxl)
library(treemap)
library(plotrix)
library(tibble)
library(ggplot2)

# Loading Data (Using new libaries)
# | Note: Had to use latin1 due to dodgy characters in the data, such as "£" and "€" (and old encoding)
excel_data <- read_excel("data/country-of-birth.xlsx")
csv_data <- read.csv("data/house-price-index.csv", header = TRUE, fileEncoding = "latin1")
excel_data
csv_data

# Task #1
uk_pop <- read_excel("data/uk-population-growth-since-1982.xls")
uk_pop

# Task #2
ggplot(uk_pop, aes(x = Year, y = Estimates)) + geom_point()

# Task #3
ggplot(uk_pop, aes(x = Estimates, y = Year)) + geom_point()

# Task #4
ggplot(uk_pop, aes(x = Year, y = Estimates)) + geom_point() + theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))
ggplot(uk_pop, aes(x = Year, y = Estimates)) + geom_point() + theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) + ggtitle("UK Population Growth")

# Task #5 - Library loaded under Installing Packages section.

# Task #6
vector_one <- c("Group-1", "Group-2", "Group-3", "Group-4")
vector_two <- c(13, 25, 22, 17)

# Task #7
df <- data.frame(Group = vector_one, Value = vector_two)
df

# Task #8
treemap(df, index="Group", vSize="Value", type="index")

# Task #9
itreemap(df, index="Group", vSize="Value", type="index")

# Task #10
treemap(df, index="Group", vSize="Value", type="value")
treemap(df, index="Group", vSize="Value", type="categorical")

# Task #11
# When viewing the treemap in a web browser, you can hover over each group to see the corresponding value.
# The size of each rectangle in the treemap represents the value of that group, with larger rectangles
# indicating higher values. In this case, Group-2 has the largest rectangle, indicating it has the highest
# value (25), followed by Group-3 (22), Group-4 (17), and Group-1 (13).

# Task #12
treemap::treecolors()

# Task #13
slices <- c(10, 12, 4, 16, 8)
lbls <- c("US", "UK", "Australia", "Germany", "France")
pct <- round(slices/sum(slices)*100)
lbls <- paste(lbls, pct) # Adding percentages to labels
lbls <- paste(lbls,"%",sep="") # Adding % to labels
pie(slices,labels = lbls, col=rainbow(length(lbls)), main="Pie Chart of Countries")

# Extension Task
# | External task under PoliceDataScript.R