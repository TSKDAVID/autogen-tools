# autogen-tools
these are some tools you may find useful for your autogen project, including simple and advanced tools as well

## how to register tools

in case you dont know you can register tools for agents like this:


start by defining the tool 
```python
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
```
then you would define the agent
```python
manager = UserProxyAgent(
    name="manager",
    system_message="You are a manager",
    llm_config=llm_config,
    human_input_mode=NEVER,
    code_execution_config={"executor": code_executor},
    is_termination_msg=lambda msg: "TERMINATE" == (msg.get("content") or "").strip()
)

researcher = AssistantAgent(
    name="researcher",
    system_message="You are a researcher",
    llm_config=llm_config,
    is_termination_msg=lambda msg: "TERMINATE" == (msg.get("content") or "").strip()
)
```
then you should register it in this format
```python
register_function(fetch_search_results, caller=researcher, executor=manager, name="fetch_search_results", description="Fetches the most relevant websites for a given search query. It takes a single argument 'query'.")
```
These are example agents of researcher and manager, and the tool that is being assigned is fetch_search_results. Then you specify the caller who will be using the tool and the executor who will be executing this tool. It can be the same agent, but in that case, the agent needs to be UserProxyAgent and needs to be able to execute codes:

```python

code_execution_config={"executor": code_executor}
```
