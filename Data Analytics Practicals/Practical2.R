install.packages("lubridate")
install.packages("ggplot2")
install.packages("plotly")
install.packages("gapminder")
library(lubridate)
library(ggplot2)
library(plotly)
library(gapminder)

# Task #1: Creating Variables
numVar <- 3.14159
intVar <- 42L
strVar <- "You think that's air you're breathing now?"
strVar_2 <- 'I know Kung Fu!'
# _fail <- 66 - Won't work as starts with underscore?
logVar <- FALSE
name <- "Tristan Budd"
bDate <- as.Date("2006-07-04")
today <- Sys.Date()
todayTime <- now()

print(numVar)
print(class(numVar))
print(intVar)
print(class(intVar))
print(strVar)
print(class(strVar))
print(strVar_2)
print(class(strVar_2))
print(logVar)
print(class(logVar))
print(name)
print(class(name))
print(bDate)
print(class(bDate))
print(today)
print(class(today))
print(todayTime)
print(class(todayTime))

dav_1 <- numVar * intVar
print(dav_1)
print(class(dav_1))

# Task 2: Interacting with Data Sets (data() for full list)
data("Nile")
print(str(Nile))

data("trees")
print(str(trees))

data("penguins")
print(str(penguins))
help(penguins)

data("mtcars")
print(str(mtcars))
help(mtcars)

# Task 2b: Making a Simple Plot (Copied from document)
p <- gapminder %>%
    filter(year==2007) %>%
    ggplot( aes(gdpPercap, lifeExp, size = pop, colour=continent)) +
    geom_point() +
    theme_minimal() +
    xlab("GDP per Capita") +
    ylab("Life Expectancy")

ggplotly(p)

# Task 3: Creating Plots
# Help Documents (Moodle): https://moodle.port.ac.uk/mod/folder/view.php?id=111580
# GGPlot Documentation: https://ggplot2.tidyverse.org/reference/ggplot.html
p2 <- ggplot( data = as.data.frame(Nile), aes(x = seq_along(Nile), y = Nile)) +
    geom_line() +
    theme_minimal() +
    xlab("Year") +
    ylab("River Flow")
ggplotly(p2)

p3 <- trees %>%
    ggplot( aes(x = Girth, y = Volume)) +
    geom_point() +
    theme_minimal() +
    xlab("Girth (inches)") +
    ylab("Volume (cubic feet)")
ggplotly(p3)

p4 <- penguins %>%
    ggplot( aes(x = flipper_len, y = body_mass, colour = species)) +
    geom_point() +
    theme_minimal() +
    xlab("Flipper Length (mm)") +
    ylab("Body Mass (g)")
ggplotly(p4)

p5 <- mtcars %>%
    ggplot( aes(x = wt, y = mpg, colour = as.factor(cyl))) +
    geom_point() +
    theme_minimal() +
    xlab("Weight (1000 lbs)") +
    ylab("Miles per Gallon (mpg)")
ggplotly(p5)