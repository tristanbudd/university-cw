# Loading Libraries:
# | MUST ALSO BE INSTALLED: install.packages("ggplot2")
library(ggplot2)

# Variable Assignment: (Saved as environmental values)
a_variable <- 34
another_variable <- "Hello, R!"

# Data Types
i <- 32                # Integer (32Bit)
l <- 64L               # Integer (64Bit)
d <- 3.14              # Double

is.numeric(i)
is.numeric(l)
is.numeric(d)

c <- "R Programming"   # Character

is.character(c)

b <- TRUE              # Boolean

is.logical(b)

# Checking Data Types
class(a_variable)
class(another_variable)

# Dates
today_date <- Sys.Date()
print(today_date)
class(today_date)

lecture_time <- as.Date("2026-12-31 12:00:00")
print(lecture_time)

lecture_time_timezone <- as.POSIXct("2026-12-31 12:00:00", tz="Europe/London")
print(lecture_time_timezone)

# | Date Arithmetic
next_week <- today_date + 7
print(next_week)

# | Formatting Dates
formatted_date <- format(today_date, "%B %d, %Y")
print(formatted_date)

# | Lubridate Library
# REQUIRED: install.packages("lubridate")
library(lubridate)

current_time <- now()
print(current_time)

ymd("20261231")
dmy("31-12-2026")
mdy("12/31/2026")

print(current_time + days(10))
print(current_time - months(2))
print(current_time + years(1))

# Conditional Statements
if (is.numeric(a_variable)) {
  print("a_variable is numeric")
} else {
  print("a_variable is not numeric")
}

# Loops
# | paste() function concatenates strings
for (i in 1:5) {
    print(paste("Iteration:", i))
}

i <- 5
while (i > 0) {
    print(paste("Countdown:", i))
    i <- i - 1
}

# Functions
add_numbers <- function(x, y) {
    return(x + y)
}

result <- add_numbers(5, 10)
print(paste("Sum:", result))

# Data Structures
# | Vectors
num_vector <- c(1, 2, 3, 4, 5)
char_vector <- c("A", "B", "C")
print(num_vector)
print(char_vector)

# | Lists
my_list <- list(name="John", age=30, scores=c(90, 85, 88))
print(my_list)

# | Data Frames
my_data <- data.frame(
    Name = c("Alice", "Bob", "Charlie"),
    Age = c(25, 30, 35),
    Score = c(85.5, 90.0, 88.5)
)
print(my_data)