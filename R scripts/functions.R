#Buid in functions
# print(seq(22,33))
# print(sum(41:42))
# cat("mean is : " ,mean(2,2))

# custom fun

square <- function(a){
  
  
  for(i in 1:a){
    
    cat(i^2 , " , ")
    
  }

  
}

# square(10)

# sum <- function(a, b , c ){
#   
#   
#   print(a+b+c)
#   
# }
# 
# sum(c=1,2,3)
# 
# 
# # default args 
# default=function(a = 10 , b= 20 ){
#   
#   print(a+b)
#   
#   
# }
# 
# 
# default(10,10)


a <- "Hello"
b <- 'How'
c <- "are you? "

print(paste(a,b,c))

print(paste(a,b,c, sep = "-"))

print(paste(a,b,c, sep = "", collapse = ""))
 
#count number of chars 
print(nchar(a))
print(toupper(a))
print(tolower(a))
# sub string fun
print(substring(a,1,3))

v <- c(10,20,88,1,2,6,8,70)
#sort function 
print(sort(v , decreasing = TRUE))



