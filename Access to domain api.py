#the normal api key won't work, need to have a OAuth 2.0 Clients key


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
