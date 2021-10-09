# st2915_assignment_2

install.packages("rvest")
library(rvest)

#extract content from wiki
wiki_url <- "https://en.wikipedia.org/wiki/Comma-separated_values#Example"
html <- read_html(wiki_url)

# extract wikitable content into html_table
content <- html_node(html,".wikitable") %>%
  html_table() 
content # test to see if html_table works

# write dataframe to csv, without row names.
write.csv(content,"/Users/roylee/repositories/st2915/st2195_assignment_2/r_csv/R_wikitable.csv", row.names = FALSE)

# read csv to dataframe
content_df <- read.csv("/Users/roylee/repositories/st2915/st2195_assignment_2/r_csv/R_wikitable.csv")
print(content_df) #  print to see if its working