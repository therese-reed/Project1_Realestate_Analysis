# Project1_Realestate_Analysis
Property price analysis for Melbourne


Everytime when you start to work on our project:

1. cd your terminal to your local repo file
2. git pull the change from that other team members (let your local repo has the latest version)
3. update your work log in the readme file if you want to 




# Material

Price Factor influencing property development and purchases (real estate) - melbourne
 
Questions
1.Have developments/purchases increased/decreased between 2019 - 2021? 
2.What has caused the increase or decrease?
3.What is the relationship between development and purchase?
4.What is the most popular suburb or type of dwelling?
5.Purchased or leased highest
 
Hypothesis


Datasets

https://data.melbourne.vic.gov.au/Property/Development-Activity-Monitor/gh7s-qda8
(Can only get the data of longitude, latitude and address)

https://data.melbourne.vic.gov.au/browse?category=Property&sortBy=most_accessed&src=fpc&tags=property
https://partner.realestate.com.au/documentation/api/
https://data.melbourne.vic.gov.au/Property/Properties-leased-by-City-of-Melbourne/3v7r-q3ds
https://developer.domain.com.au
https://onproperty.com.au/free-sites-for-property-research/


Australian census
Reserve bank - interest rate?
Location of schools -
 post code map
 heat map /highest prices -flag top high school/ list school
Highest lowest areas with schools median house price
Compare property price with development
Investigate influence of covid which increased purchase or rental rate
Compare house sale time overtime vs interest rates offered
Compare house types
Purchase vs rental
Purchase purchase vs ranking


# current dataset Echo find
By using the GET /v1/addressLocators and GET /v1/suburbPerformanceStatistics/ from Domain, we will be able to find the price as follow:

MedianSoldPrice, AuctionNumberAuctioned, AuctionNumberSold, AuctionNumberWithdrawn, NumberSold, LowestSoldPrice, HighestSoldPrice, 5thPercentileSoldPrice, 25thPercentileSoldPrice, 75thPercentileSoldPrice, 95thPercentileSoldPrice, DaysOnMarket, DiscountPercentage, MedianRentListingPrice, NumberRentListing, HighestRentListingPrice, LowestRentListingPrice, MedianSaleListingPrice, NumberSaleListing, HighestSaleListingPrice, LowestSaleListingPrice

![Screen Shot 2021-06-20 at 3 37 42 pm](https://user-images.githubusercontent.com/75764401/122663398-838d8680-d1dd-11eb-944a-75ec6944c2be.png)


