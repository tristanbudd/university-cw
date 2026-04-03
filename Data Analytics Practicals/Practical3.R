# Installing Packages
install.packages("tidyverse")
install.packages("ggplot2")
install.packages("nycflights13")
install.packages("lubridate")
library(tidyverse)
library(ggplot2)
library(nycflights13)
library(lubridate)

# Task #1
# | Code for Lecture Slides under TidyverseLect.R
print(mpg)

help(fl)
help(drv)
help(class)

select(mpg, 1, 4, 7, 8)

df <- select(mpg, 1, 4, 7, 8)
df

df2 <- mutate(mpg, cap_per_cyl = displ / cyl)
df2

# Task #2
flights <- nycflights13::flights
??flights

sub_data <- select(nycflights13::flights, carrier, origin, dest, flight, distance)
sub_data

jfk_flights <- filter(nycflights13::flights, origin == "JFK")
jfk_flights

jfk_flights_sub <- select(jfk_flights, month, day, dep_time, sched_dep_time, arr_time, carrier, dest, hour)
jfk_flights_sub

ggplot(jfk_flights, aes(x = distance, y = air_time, colour = carrier)) + geom_point()
ggsave(path = "export", filename = "jfk_flights_plot.pdf")

# Task #3
data <- read.csv("data/BoE-Database_export.csv", header=TRUE)
data

df_jan_2014 <- filter(data, month(dmy(data$Date)) == 1, year(dmy(data$Date)) == 2014)
df_jan_2016 <- filter(data, month(dmy(data$Date)) == 1, year(dmy(data$Date)) == 2016)
df_jan_2020 <- filter(data, month(dmy(data$Date)) == 1, year(dmy(data$Date)) == 2020)
df_dec_2020 <- filter(data, month(dmy(data$Date)) == 12, year(dmy(data$Date)) == 2020)
df_jan_2014
df_jan_2016
df_jan_2020
df_dec_2020

ggplot(df_jan_2014, aes(x = dmy(Date), y = Value)) + geom_line() + ggtitle("January 2014")
ggsave(path = "export", filename = "jan_2014_plot.pdf")

ggplot(df_jan_2016, aes(x = dmy(Date), y = Value)) + geom_line() + ggtitle("January 2016")
ggsave(path = "export", filename = "jan_2016_plot.pdf")

ggplot(df_jan_2020, aes(x = dmy(Date), y = Value)) + geom_line() + ggtitle("January 2020")
ggsave(path = "export", filename = "jan_2020_plot.pdf")

ggplot(df_dec_2020, aes(x = dmy(Date), y = Value)) + geom_line() + ggtitle("December 2020")
ggsave(path = "export", filename = "dec_2020_plot.pdf")

# Extension
co2_data <- read.csv("data/co2_per_person.csv", header=TRUE)
co2_data

countries <- filter(co2_data, country %in% c("United States", "China", "United Kingdom", "India", "Germany"))
years <- select(countries, country, X2000, X2005, X2010, X2015, X2018)

ggplot(years, aes(x = X2000, y = country, fill = country)) + geom_col()
ggsave(path = "export", filename = "co2_2000_plot.pdf")

ggplot(years, aes(x = X2018, y = country, fill = country)) + geom_col()
ggsave(path = "export", filename = "co2_2018_plot.pdf")

uk <- filter(co2_data, country == "United Kingdom")
uk_years <- data.frame(
  year = c(1850, 1900, 1950, 2000, 2018),
  co2 = c(uk$X1850, uk$X1900, uk$X1950, uk$X2000, uk$X2018)
)

ggplot(uk_years, aes(x = year, y = co2)) + geom_line() + geom_point()
ggsave(path = "export", filename = "uk_co2_plot.pdf")