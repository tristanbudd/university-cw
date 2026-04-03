# Installing Packages
install.packages("ggplot2")
install.packages("dplyr")
install.packages("tidyr")
install.packages("readxl")
install.packages("scales")
library(ggplot2)
library(dplyr)
library(tidyr)
library(readxl)
library(scales)

# Load & Clean Data
# | The CSV uses commas in numbers (e.g. "5,024,279") so its stripped first
us_raw <- read.csv("data/US-PopulationDataByState.csv", header = TRUE, check.names = FALSE)

colnames(us_raw)[1] <- "State"
us_raw <- us_raw[, 1:10]
colnames(us_raw) <- c(
  "State",
  "Pop2020", "Density2020", "Rank2020",
  "Pop2010", "Density2010", "Rank2010",
  "Pop2000", "Density2000", "Rank2000"
)

# Remove blank rows
us_raw <- us_raw[us_raw$State != "" & !is.na(us_raw$State), ]

# Strip commas and convert to numbers
clean_num <- function(x) as.numeric(gsub(",", "", x))
us_raw[, 2:10] <- lapply(us_raw[, 2:10], clean_num)

us_raw

# Split national total from state rows
us_total  <- us_raw[us_raw$State == "United States", ]
us_states <- us_raw[us_raw$State != "United States", ]

# Task #1 - Population Change
us_states <- us_states %>%
  mutate(
    PctChange_00_10 = round((Pop2010 - Pop2000) / Pop2000 * 100, 2),
    PctChange_10_20 = round((Pop2020 - Pop2010) / Pop2010 * 100, 2),
    PctChange_00_20 = round((Pop2020 - Pop2000) / Pop2000 * 100, 2)
  )

us_states

# Fastest and slowest growing states 2000-2020
us_states %>% arrange(desc(PctChange_00_20)) %>% head(10)
us_states %>% arrange(PctChange_00_20) %>% head(10)

# | Nevada, Arizona, Utah and Idaho grew the fastest - warm climate and low costs.
# | Puerto Rico and West Virginia are the only ones that actually shrank.
# | Puerto Rico lost people due to economic collapse and Hurricane Maria (2017).
# | West Virginia shrank due to the decline of the coal industry.

# Task #2 - Plot: Fastest vs Slowest Growing States
top10    <- us_states %>% arrange(desc(PctChange_00_20)) %>% head(10) %>% mutate(Group = "Fastest")
bottom10 <- us_states %>% arrange(PctChange_00_20)      %>% head(10) %>% mutate(Group = "Slowest / Declining")

ggplot(bind_rows(top10, bottom10),
       aes(x = reorder(State, PctChange_00_20), y = PctChange_00_20, fill = Group)) +
  geom_col() +
  coord_flip() +
  scale_fill_manual(values = c("Fastest" = "#2ecc71", "Slowest / Declining" = "#e74c3c")) +
  labs(title = "US States: % Population Change 2000-2020",
       subtitle = "Top 10 fastest vs. slowest",
       x = "State", y = "% Change", fill = "") +
  theme_minimal() + theme(legend.position = "bottom")
ggsave(path = "export", filename = "us_pop_change_extremes.pdf", width = 10, height = 6)

# Task #3 - Plot: All States Population Change
ggplot(us_states, aes(x = reorder(State, PctChange_00_20), y = PctChange_00_20,
                      fill = PctChange_00_20 >= 0)) +
  geom_col() +
  coord_flip() +
  scale_fill_manual(values = c("TRUE" = "#3498db", "FALSE" = "#e74c3c"),
                    labels = c("TRUE" = "Growth", "FALSE" = "Decline")) +
  labs(title = "US States: % Population Change 2000-2020",
       x = "State", y = "% Change", fill = "") +
  theme_minimal(base_size = 8) + theme(legend.position = "bottom")
ggsave(path = "export", filename = "us_pop_change_all.pdf", width = 10, height = 12)

# Task #4 - Population Density
us_states %>% arrange(desc(Density2020)) %>% head(10)  # most dense
us_states %>% arrange(Density2020)       %>% head(10)  # least dense

# | DC is the densest (11,280/sq mile) because it is just one city with no rural land.
# | Alaska, Wyoming and Montana are the least dense - massive land areas, few people.
# | Dense areas have better services but are more expensive and polluted.
# | Sparse areas are cheaper but have poor access to services.

# Log scale needed because DC is such an extreme outlier it crushes all other bars
ggplot(us_states, aes(x = reorder(State, Density2020), y = Density2020)) +
  geom_col(fill = "#8e44ad") +
  coord_flip() +
  scale_y_log10(labels = comma) +
  labs(title = "US States: Population Density 2020 (log scale)",
       subtitle = "People per square mile",
       x = "State", y = "Density (log scale)") +
  theme_minimal(base_size = 8)
ggsave(path = "export", filename = "us_density_2020.pdf", width = 10, height = 12)

# Task #5 - US National Trend
us_total_long <- data.frame(
  Year       = c(2000, 2010, 2020),
  Population = c(us_total$Pop2000, us_total$Pop2010, us_total$Pop2020)
)

ggplot(us_total_long, aes(x = Year, y = Population)) +
  geom_line(colour = "#2980b9", linewidth = 1.2) +
  geom_point(colour = "#2980b9", size = 3) +
  scale_y_continuous(labels = comma) +
  scale_x_continuous(breaks = c(2000, 2010, 2020)) +
  labs(title = "US National Population Trend 2000-2020",
       x = "Census Year", y = "Resident Population") +
  theme_minimal()
ggsave(path = "export", filename = "us_national_trend.pdf", width = 8, height = 5)

# Task #6 - Regional Breakdown
sun_belt   <- c("Florida", "Georgia", "South Carolina", "North Carolina",
                "Texas", "Arizona", "Nevada", "California", "New Mexico", "Utah")
rust_belt  <- c("Michigan", "Ohio", "Pennsylvania", "Indiana", "Illinois",
                "Wisconsin", "West Virginia", "Kentucky", "Missouri")
north_east <- c("New York", "New Jersey", "Massachusetts", "Connecticut",
                "Rhode Island", "Vermont", "New Hampshire", "Maine",
                "Maryland", "Delaware", "District of Columbia")

us_states <- us_states %>%
  mutate(Region = case_when(
    State %in% sun_belt   ~ "Sun Belt",
    State %in% rust_belt  ~ "Rust Belt",
    State %in% north_east ~ "North-East",
    TRUE                  ~ "Other"
  ))

region_summary <- us_states %>%
  group_by(Region) %>%
  summarise(AvgChange = mean(PctChange_00_20, na.rm = TRUE))
region_summary

ggplot(region_summary, aes(x = Region, y = AvgChange, fill = Region)) +
  geom_col() +
  scale_fill_brewer(palette = "Set2") +
  labs(title = "Average % Population Change 2000-2020 by Region",
       x = "Region", y = "Avg % Change") +
  theme_minimal() + theme(legend.position = "none")
ggsave(path = "export", filename = "us_region_change.pdf", width = 8, height = 5)

# | Sun Belt grew the fastest - warm weather, lower taxes and lots of new jobs.
# | Rust Belt grew the slowest - manufacturing collapsed over recent decades.

# Task #7 - Anomaly: Puerto Rico
# | Puerto Rico lost around 523,000 people between 2000 and 2020 (about 14%).
# | Main causes: economic recession, bankruptcy in 2017, and Hurricane Maria
# | which killed thousands and pushed 130,000+ to permanently move to Florida.
# | This links to the gun crime coursework - you need population to calculate
# | per-capita rates, otherwise the numbers are meaningless.

pr_long <- us_states %>%
  filter(State == "Puerto Rico") %>%
  select(State, Pop2000, Pop2010, Pop2020) %>%
  pivot_longer(cols = c(Pop2000, Pop2010, Pop2020), names_to = "Year", values_to = "Population") %>%
  mutate(Year = as.integer(gsub("Pop", "", Year)))

ggplot(pr_long, aes(x = Year, y = Population)) +
  geom_line(colour = "#e74c3c", linewidth = 1.2) +
  geom_point(colour = "#e74c3c", size = 3) +
  scale_y_continuous(labels = comma, limits = c(3000000, 4000000)) +
  scale_x_continuous(breaks = c(2000, 2010, 2020)) +
  labs(title = "Puerto Rico: Declining Population 2000-2020",
       subtitle = "Economic crisis + Hurricane Maria (2017) drove emigration to the mainland",
       x = "Census Year", y = "Resident Population") +
  theme_minimal()
ggsave(path = "export", filename = "puerto_rico_decline.pdf", width = 8, height = 5)

# Task #8 - Climate Change: Coastal States
# | States near sea level face rising seas and more hurricanes.
# | If people are moving away, we'd expect slower population growth there.

coastal <- c("Florida", "Louisiana", "Virginia", "New Jersey", "Maryland",
             "North Carolina", "South Carolina", "Delaware", "Connecticut", "Rhode Island")

us_states %>%
  filter(State %in% coastal) %>%
  select(State, PctChange_00_10, PctChange_10_20, PctChange_00_20) %>%
  arrange(PctChange_00_20)

# | Florida and South Carolina are still growing fast - people aren't leaving yet.
# | Louisiana barely grew 2000-2010 because of Hurricane Katrina (2005).
# | One big event can completely distort a decade of data.

# Task #9 - Why Does Population Data Matter for Gun Crime?
# | Raw death counts mean nothing without knowing how many people live there.
# | You divide deaths by population to get a rate you can actually compare.
# | Dense urban areas have more deaths in total, but rural states often have
# | higher rates because of gun suicide. Population size explains a lot.

# Task #12 - UK vs US Population Comparison
# | UK census years (2001, 2011, 2021) are slightly off from the US ones but
# | close enough to compare growth decade by decade.

uk_pop <- read_excel("data/uk-population-growth-since-1982.xls")
uk_pop$Estimates <- as.numeric(uk_pop$Estimates)
uk_pop$Year <- as.numeric(uk_pop$Year)
uk_pop

uk_census <- uk_pop %>%
  filter(Year %in% c(2001, 2011, 2020)) %>%
  select(Year, Estimates) %>%
  arrange(Year)
uk_census

uk_change <- uk_census %>%
  mutate(
    PctChange = round((Estimates - lag(Estimates)) / lag(Estimates) * 100, 2),
    Decade    = case_when(Year == 2011 ~ "2000-2010", Year == 2020 ~ "2010-2020", TRUE ~ NA_character_),
    Country   = "United Kingdom"
  ) %>%
  filter(!is.na(PctChange)) %>%
  select(Decade, PctChange, Country)
uk_change

us_change <- data.frame(
  Decade    = c("2000-2010", "2010-2020"),
  PctChange = c(
    round((us_total$Pop2010 - us_total$Pop2000) / us_total$Pop2000 * 100, 2),
    round((us_total$Pop2020 - us_total$Pop2010) / us_total$Pop2010 * 100, 2)
  ),
  Country = "United States"
)
us_change


combined <- bind_rows(uk_change, us_change)
combined

# Task #13 - Plot: UK vs US % Change by Decade
ggplot(combined, aes(x = Decade, y = PctChange, fill = Country)) +
  geom_col(position = "dodge") +
  scale_fill_manual(values = c("United Kingdom" = "#003087", "United States" = "#B22234")) +
  labs(title = "UK vs US: Decadal Population % Change",
       x = "Decade", y = "% Change", fill = "") +
  theme_minimal() + theme(legend.position = "bottom")
ggsave(path = "export", filename = "uk_us_pop_change.pdf", width = 8, height = 5)

# Task #14 - Plot: UK vs US Growth Index (2000 = 100)
# | Indexing to 100 lets us compare growth regardless of country size

uk_index <- data.frame(
  Year    = c(2000, 2010, 2020)[seq_len(nrow(uk_census))],
  Index   = uk_census$Estimates / uk_census$Estimates[1] * 100,
  Country = "United Kingdom"
)

us_index <- data.frame(
  Year = c(2000, 2010, 2020),
  Population = c(us_total$Pop2000, us_total$Pop2010, us_total$Pop2020)
) %>%
  mutate(Index = Population / first(Population) * 100,
         Country = "United States") %>%
  select(Year, Index, Country)

ggplot(bind_rows(uk_index, us_index),
       aes(x = Year, y = Index, colour = Country, group = Country)) +
  geom_line(linewidth = 1.2) +
  geom_point(size = 3) +
  geom_hline(yintercept = 100, linetype = "dashed", colour = "grey50") +
  scale_colour_manual(values = c("United Kingdom" = "#003087", "United States" = "#B22234")) +
  scale_x_continuous(breaks = c(2000, 2010, 2020)) +
  labs(title = "UK vs US Population Growth Index (2000 = 100)",
       x = "Census Year", y = "Index (2000 = 100)", colour = "") +
  theme_minimal() + theme(legend.position = "bottom")
ggsave(path = "export", filename = "uk_us_index.pdf", width = 8, height = 5)

# Observations - UK vs US
# | Both countries slowed down 2010-2020 and both were hit by the 2008 financial crisis.
# | The US grows faster overall due to higher immigration and birth rates.
# | The UK grew more in 2000-2010 because of a big wave of EU migrants after 2004.
# | US hurricanes (Katrina 2005, Maria 2017) have no UK equivalent.
# | Good tie-breaker countries: Canada (similar to US), Australia (similar to UK).
# | Events that affected both: 2008 financial crisis and COVID-19 in 2020.
