#CoVID-19 ggplot code

library(ggplot2)
library(reshape2)
library(hrbrthemes)
#library(ggthemr)
library(Hmisc)

#if using ggthemr use this and remove all 'theme_ft_rc()' code
#I found this necessary on some OSs as hrbrthemes has font and plotting issues
# ggthemr('flat dark', type = 'outer')

#setwd("")

#####################
####Data Wrangling###
#####################

co19_df <- read.csv("mn_covid_19.txt", sep ="\t")

#add current infected column
co19_df$Curr_Infected <- (co19_df$T.Pos - co19_df$Recovered_Cases)

#Add new cases column
co19_df$New_Cases <- (co19_df$T.Pos - Lag(co19_df$T.Pos, 1))

#Add Growth Factor column
co19_df$Growth_Factor <- round(co19_df$New_Cases / Lag(co19_df$New_Cases, 1), digits = 3)

#Testing Rate
#co19_df$New_Tests <- co19_df$Tested - lag(co19_df$Tested, 1)
#co19_df$Testing_Rate <- round(co19_df$New_Tests / lag(co19_df$New_Tests, 1), digits = 3)

#Convert to long format data frame
co19_df_long <- melt(co19_df, id.vars=1:1)

#####################
#######Plotting######
#####################

###make a pretty plot###
ggplot(data = co19_df, aes(Date, T.Pos, group = '')) + 
  geom_line() + 
  geom_point(color = ft_cols$red) + 
  labs(y = "Tested Positive", title = "CoVID-19 Cases in MN") + 
  theme_ft_rc() + theme(axis.text.x = element_text(angle = 60, hjust =1))



###Plot all###
ggplot(data = co19_df_long, aes(Date, value, group = variable, color = variable)) + 
  geom_line() + 
  geom_point() + 
  labs(y = "Tested Positive", title = "CoVID-19 Cases in MN") + 
  theme_ft_rc() + theme(axis.text.x = element_text(angle = 60, hjust =1))



###fixing legend###
co <- co19_df_long

levels(co$variable)[levels(co$variable)=="T.Pos"] <- "Tested Positive"
names(co)[names(co) == "variable"] <- "Groups"

ggplot(data = co, aes(Date, value, group = Groups, color = Groups)) + 
  geom_line() + 
  geom_point() + 
  labs(y = "N", title = "CoVID-19 Cases in MN") + 
  theme_ft_rc() + theme(axis.text.x = element_text(angle = 60, hjust =1))



###Plot hospital data w/ infection?
co <- co19_df_long

levels(co$variable)[levels(co$variable)=="T.Pos"] <- "Tested Positive"
names(co)[names(co) == "variable"] <- "Groups"
#Filter as needed
co <- subset(co, Groups != 'Growth_Factor')
co <- subset(co, Groups != 'New_Cases')
co <- subset(co, Groups != 'Tested')


ggplot(data = co, aes(Date, value, group = Groups, color = Groups)) + 
  geom_line() + 
  geom_point() + 
  labs(y = "N", title = "CoVID-19 in MN (Health Data)") + 
  theme_ft_rc() + theme(axis.text.x = element_text(angle = 60, hjust =1))


###Plot infection data
co <- co19_df_long

levels(co$variable)[levels(co$variable)=="T.Pos"] <- "Tested Positive"
names(co)[names(co) == "variable"] <- "Groups"
#Filter as needed
co <- subset(co, Groups != 'Deaths')
co <- subset(co, Groups != 'Tot_Req_Hosp')
co <- subset(co, Groups != 'Curr_Hosp')
co <- subset(co, Groups != 'Growth_Factor')
co <- subset(co, Groups != 'New_Cases')
co <- subset(co, Groups != 'Tested')

ggplot(data = co, aes(Date, value, group = Groups, color = Groups)) + 
  geom_line() + 
  geom_point() + 
  labs(y = "N", title = "CoVID-19 Cases in MN") + 
  theme_ft_rc() + theme(axis.text.x = element_text(angle = 60, hjust =1))



#Plot ratio Pos/Total
ggplot(data = co19_df, aes(Date, T.Pos/Tested, group = '')) + 
  geom_line() + 
  geom_point(color = ft_cols$red) + 
  labs(y = "Tested Positive/Total", title = "CoVID-19 Cases in MN") + 
  theme_ft_rc() + theme(axis.text.x = element_text(angle = 60, hjust =1))


#Use log sclae to predict disease curve
ggplot(data = co19_df, aes(log(T.Pos), log(New_Cases), group = '')) + 
  geom_line() + 
  geom_point(color = ft_cols$red) + 
  labs(y = "Log(New Cases)", y = "log(Total Cases)", title = "CoVID-19 in MN (Disease Curve Projection)") + 
  theme_ft_rc() + theme(axis.text.x = element_text(angle = 60, hjust =1))

