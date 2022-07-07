#The plot() function is used to draw points (markers) in a diagram.

#The function takes parameters for specifying points in the diagram.

#Parameter 1 specifies points on the x-axis.

#Parameter 2 specifies points on the y-axis.

plot(1, 3)

plot(c(1, 8), c(3, 10))

plot(c(1, 2, 3, 4, 5), c(3, 7, 8, 9, 12))

plot(1:10)

plot(1:10, type="l")

plot(1:10, main="My Graph", xlab="The x-axis", ylab="The y axis")

plot(1:10, col="red")

#drawing line

plot(1:10, type="l", lwd=2)

line1 <- c(1,2,3,4,5,10)
line2 <- c(2,5,7,8,9,10)

plot(line1, type = "l", col = "blue")
lines(line2, type="l", col = "red")


#scatter plot

x <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)

plot(x, y)

###
x <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)

plot(x, y, main="Observation of Cars", xlab="Car age", ylab="Car speed")

