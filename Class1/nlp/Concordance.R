# Concordance
rm(list = ls(all=T))
library(xtable)
# Import text in R
text<-scan("alice.txt", what="char", sep="\n", quote="", comment.char="") 


# A function for creating a basic concordance

concordance <- function(search, text, removepunc=FALSE){
findtext <- search
text <- text
if(removepunc == TRUE){text <- gsub('[[:punct:] ]+',' ', text)}
tmp <-grep(paste("\\b(",findtext,")\\b",sep=""), text, ignore.case=TRUE, value=TRUE)
conc <- gsub(paste("\\b(",findtext,")\\b",sep=""),"\t\\1\t",tmp,ignore.case=T)
data <- read.csv(t=conc, sep="\t")
colnames(data) <- c("Left", "Keyword", "Right")
return(data)
}

alice1 <- concordance("Alice", text, TRUE)
View(alice1)
xtable(alice1[1:10, ])
