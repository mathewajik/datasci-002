# Set working directory
setwd("~/Documents/Books and Tutorials/Coursera/Introduction to Data Science/src/working copy/A5")

# Load data file
seaflow_21min <- read.csv("seaflow_21min.csv")

#Q1
summary(seaflow_21min$pop)

#Q2
summary(seaflow_21min$fsc_small)

#Q3
#??createDataPartition
library(caret)
inTrain <- createDataPartition(seaflow_21min$pop, times=1, p=0.5, list = FALSE)
train <- seaflow_21min[inTrain, ]
test <- seaflow_21min[-inTrain, ]
summary(train$time)

#Q4
library(ggplot2)
qplot(pe, chl_small, data = seaflow_21min, color=pop)

# Q5 Q6 Q7
library(rpart)
model <- rpart(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, method="class", data=train)
print(model)

#Q8
Prediction <- predict(model, test, type='class')
summary(Prediction == test$pop)
30947 / (30947 + 5224)

# Q9
library(randomForest)
model <- randomForest(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=train)
Prediction <- predict(model, test, type='class')
summary(Prediction == test$pop)
33343 /(2828 + 33343)

# Q10
importance(model)

# Q11
library('e1071')
model <- svm(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=train)
Prediction <- predict(model, test, type='class')
summary(Prediction == test$pop)
33261 / (33261 + 2910)

# Q12
# Confusion Matrix
# the column names in this table mean the correct pop, and the row names mean the predicted pop.
table(pred = Prediction, true = test$pop)

#Q13
plot(seaflow_21min$fsc_big)

plot(seaflow_21min$time, seaflow_21min$chl_big)
qplot(chl_big, data=seaflow_21min, geom="bar")

library(ggplot2)
p <- ggplot(seaflow_21min, aes(x = time, y = chl_big, colour = pop))
p + geom_point()

#Q14
# Cleanup
#cleaned <- subset(seaflow_21min, file_id != 208)
#incleanedTrain <- createDataPartition(cleaned$pop, times=1, p=0.5, list = FALSE)

#cleanedtrain <- seaflow_21min[incleanedTrain, ]
#cleanedtest <- seaflow_21min[-incleanedTrain, ]

cleanedtrain <- subset(train, file_id != 208)
cleanedtest <- subset(test, file_id != 208)
  
model <- svm(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=cleanedtrain)
Prediction <- predict(model, cleanedtest, type='class')
summary(Prediction == cleanedtest$pop)

29283 / (29283 +  860)

(29283 / (29283 +  860)) - (33261 / (33261 + 2910))
