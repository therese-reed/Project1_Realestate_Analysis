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

#how to access to domain api (the normal api key won't work, need to have a OAuth 2.0 Clients key

client_secret = " " #fill your client_secret and id here
client_id = " "
scopes = ['api_properties_read']
auth_url = 'https://auth.domain.com.au/v1/connect/token'
url_endpoint = 'https://api.domain.com.au/sandbox/v1/properties/'
property_id = 'RF-8884-AK' #fill the id here


def get_property_info():
    response = requests.post(auth_url, data = {
                        'client_id':client_id,
                        'client_secret':client_secret,
                        'grant_type':'client_credentials',
                        'scope':scopes,
                        'Content-Type':'text/json'
                        })
    json_res = response.json()
    access_token=json_res['access_token']
    print(access_token)
    auth = {'Authorization':'Bearer ' + access_token}
    url = url_endpoint + property_id
    res1 = requests.get(url, headers=auth)    
    r = res1.json()
    print(r)


final_details = get_property_info()
print(json.dumps(final_details, indent=4, sort_keys =True))
