def scrape_website(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # attempt to find the main content container
        main_content = soup.find('main') or soup.find('article') or soup.find('div', role='main')
        
        # if a main content container isn't found, fall back to the body of the document
        if not main_content:
            main_content = soup.body
        
        # extracting text from the targeted elements
        titles = [tag.get_text(strip=True) for tag in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])] #you can add more elements in case you need it
        paragraphs = [tag.get_text(strip=True) for tag in main_content.find_all('p')]
        
        content = {
            'title': titles,
            'content': paragraphs
        }
        scraped = json.dumps(content, indent=2)
        content_message = "You are a helpful assistant skilled in text formatting. Please format the following content into structured Markdown, removing any unnecessary elements such as links and html elements and others and making a very good small summery.make sure to remove sources or authors or anything similar , just leave the text "
        formatted_content = format_text_with_ai(scraped,content_message)
        appender("research.md",formatted_content)
        return("data was scraped , formatted and appended succesfully")
    else:
        return json.dumps({'error': f'Failed to retrieve the webpage. Status code: {response.status_code}'})



#this tool scrapes a website on a url and returns scraped data without html elements, it will return a large data so it would be recommended to somehow summerize it using free ai tools so that you dont waste too 
#many tokens of any other paid ai in case you are using one, or rather so that you dont exhoust the token limitations for certain llms
