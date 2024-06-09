def fetch_search_results(query: str) -> Union[List[Dict[str, str]], Dict[str, str]]:
    url = 'https://google.serper.dev/search'
    headers = {
        'X-API-KEY': 'your_api_key',
        'Content-Type': 'application/json'
    }
    data = json.dumps({"q": query})
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        results = response.json()
        print(results)
        return results
    else:
        return {'error': f"failed to fetch search results. Status code: {response.status_code}"}

#this tool uses google serper api to fetch relevant searhc results, useful for researcher agent, you would need to register on https://serper.dev/signup   and get a api key that has free tier of 2500 request
# which in my opinion is pretty decent considering that one search querry is considered as 1 request
