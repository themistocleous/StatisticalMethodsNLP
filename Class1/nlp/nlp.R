rm(list = ls(all=T))
library("NLP")
library("stringr")
library("stylo")
library(xtable)
# Import text in R
text<-scan("alice.txt", what="char", sep="\n", quote="", comment.char="") 
head(text)

# Make all words to lower case
text <- tolower(text) 

# Create a word list
words.list <-  strsplit(text, " ")

# Split the list and get the words
words.vector <-unlist(words.list)

# Some data cleaning
# Remove empty strings
words.vector <- words.vector[words.vector != ""]

# Clear punctuation marks and trailing spaces
words.vector <- gsub('[[:punct:] ]+',' ', words.vector)
words.vector <- str_trim(words.vector)


#Calculate the frequencies of words in table, sort the table, and calculate probabilities
freq.list <- table(words.vector)

freq.list.sorted <- sort(freq.list, decreasing=T)
freq.list.prop.sorted <- prop.table(freq.list.sorted)

# Create a nice table
frequencies <- as.data.frame(freq.list.sorted)
frequencies.prop <- as.data.frame(freq.list.prop.sorted)
frequencies <- cbind(frequencies,frequencies.prop[,2])
colnames(frequencies) <- c("Word", "Freq", "Prop")
write.csv(frequencies, "frequency.csv")

# This is the table that appears in the text
head(frequencies,20)


# Frequencies and Zipf
freq.table <- frequencies[,1:2]
rank <- 1:nrow(freq.table) 
zipf <- frequencies$Freq * rank
freq.table <- cbind(freq.table, as.data.frame(rank),as.data.frame(zipf))
colnames(freq.table) <- c("Word", "Freq(f)", "Rank(r)", "f.r")
# This is the second table that apperars in the text
xtable(head(freq.table,20))

# Create plot
plot(log(freq.table$`Rank(r)`), log(freq.table$`Freq(f)`), xlab = "Rank", ylab="frequency")
a <- log(freq.table$`Rank(r)`)
b <- log(freq.table$`Freq(f)`)
abline(a=lm(a~b))
plot(log(mandel), log(freq.table$`Freq(f)`), xlab = "Rank", ylab="frequency")





  