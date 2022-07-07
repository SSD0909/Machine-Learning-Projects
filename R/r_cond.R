b <- 200

if (b > a) {
  print("b is greater than a")
}


###

a <- 33
b <- 33

if (b > a) {
  print("b is greater than a")
} else if (a == b) {
  print ("a and b are equal")
}

####
for (x in 1:10) {
  print(x)
}

####

#A vector is simply a list of items that are of the same type.

# Vector of strings
pl <- c("c", "c++", "python")

# Print fruits
pl


####

# List of strings
thislist <- list("apple", "banana", "cherry")

# Print the list
thislist

####

# Create a data frame
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

# Print the data frame
Data_Frame

####
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame

summary(Data_Frame)

####

Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame[1]

Data_Frame[["Training"]]

Data_Frame$Training


####


