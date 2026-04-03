# Load required package
install.packages("tidyverse")
library(tidyverse)

# View the mpg dataset
mpg

# Select specific columns by name
# Extract model, city mileage (cty), and highway mileage (hwy)
extract_data <- select(mpg, model, cty, hwy)
extract_data

# Select columns by position
# First four columns of the dataset
select(mpg, 1:4)

# Select columns using a vector of positions
# Columns 1, 3, and 5 through 7
select(mpg, c(1, 3, 5:7))

# Select the first and last columns
new_frame <- select(mpg, 1, ncol(mpg))
new_frame

# Rename columns
# Make a copy of mpg
df <- mpg

# Rename hwy to mwy
df1 <- rename(df, mwy = hwy)

# Rename cty to urban
df1 <- rename(df1, urban = cty)

# Check column names
colnames(df1)

# Select and rename at the same time
# Renamed columns appear first, then all remaining columns
df2 <- select(df,
              mwy = hwy,
              urban = cty,
              everything())

# Check column order and structure
colnames(df2)
str(df2)

# Create a new column
# Engine displacement per cylinder
df3 <- mutate(df, cap_per_cyl = displ / cyl)
df3

# Select columns from the modified data frame
df4 <- select(df3, manufacturer, model, year, cap_per_cyl)
df4