# Project1_Realestate_Analysis
Property price analysis for Melbourne


Everytime when you start to work on our project:

1. cd your terminal to your local repo file
2. git pull the change from that other team members (let your local repo has the latest version)
3. update your work log in the readme file if you want to 




# Material

Price Factor influencing property development and purchases (real estate) - melbourne
 
Questions

1.Do purchase price and sell number impact by bank interest rate (quartly , median sell price, listing, sold, line chart)

2.In three different years, compare whole number of list and sold (use sum up value, bar chart)

3.What has caused the increase or decrease? (covid, loan interests, schools)

4.Does the quantity of the schools has anything do with the property price? Or just the quality of the schools? (heatmap of schools and heatmaps of price, heatmps of median price with markers of top ranking schools)

5.Does the median price of the rent has relationships with price of sold?(scatter plot, linear regression)

6.Does the list of rent has relationships with price of sold?(scatter plot, linear regression)

7.What's the sell and list data about each suburb? (bar chart)

8.What is the most popular suburb or type of dwelling? (heatmap-googlemap geo module, marker about school (government, catholic, private)

9.The outliners of 2019-2021 in Highest sell price, median sold price (boxplot, maybe highlight the outliner)

 
# Hypothesis

1. The sold number and the purchase price will go up when the bank interest rate go down.
2. Covid will have negative impact on market, the price and list will drop.
3. 


Datasets

https://data.melbourne.vic.gov.au/Property/Development-Activity-Monitor/gh7s-qda8
(Can only get the data of longitude, latitude and address)

https://data.melbourne.vic.gov.au/browse?category=Property&sortBy=most_accessed&src=fpc&tags=property
https://data.melbourne.vic.gov.au/Property/Properties-leased-by-City-of-Melbourne/3v7r-q3ds
https://developer.domain.com.au
https://onproperty.com.au/free-sites-for-property-research/
https://developers.google.com/chart/interactive/docs/gallery/geochart
https://www.greatschools.org/api/


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

# Rachel's suggestion: 
Can consider this API, we can specify the stats based on quarter or year, and specify the region, it still provide majorities of the stats infor that we requires.
https://developer.domain.com.au/docs/latest/apis/pkg_properties_locations/references/suburbperformancestatistics_get

using python to map geo graph data
https://towardsdatascience.com/mapping-geograph-data-in-python-610a963d2d7f

