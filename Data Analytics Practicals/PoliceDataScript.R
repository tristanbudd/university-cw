# import packages
install.packages("sp")
install.packages("leaflet")
install.packages("tidyverse")
install.packages("data.table")
library(sp)
library(leaflet)
library(tidyverse)
library(data.table)

# load july 2025 data
july <- read_csv('data/2025-07-hampshire-street.csv')
july <- rename(july, CrimeID = 'Crime ID')
july <- rename(july, CrimeType = 'Crime type')
july <- rename(july, LSOA = 'LSOA name')

# filter data examples
 # t1 <- filter(jan,CrimeID== '5640ebafe67b329359274d8b9617a200228fe80d4bd837a24a9bbd37257c2c6c')
 # t2 <- filter(jan,CrimeID == '5ecaac5aaee7300af5fd97b5ab0c9a4674760bda90d101da58e2522c2be5b471')
portsmouth <- filter(july, LSOA == 'Portsmouth 001A')
iow <- filter(july, grepl("Wight", LSOA, fixed = TRUE))

# TEST AREA
# leaflet(t1) %>% addTiles() %>%
#   addMarkers(popup = ~as.character(CrimeType), label = ~as.character(CrimeType))
# 
# leaflet(t2) %>% addTiles() %>% 
#   addMarkers(popup = ~as.character(CrimeType), label = ~as.character(CrimeType))


leaflet(july) %>% addTiles() %>%
  addMarkers(popup = ~as.character(CrimeType), label = ~as.character(CrimeType))

leaflet(portsmouth) %>% addTiles() %>%
  addMarkers(popup = ~as.character(CrimeType), label = ~as.character(CrimeType))

leaflet(iow) %>% addTiles() %>%
  addAwesomeMarkers(popup = ~as.character(CrimeType), label = ~as.character(CrimeType))
