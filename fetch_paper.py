import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from summarizer import summarize_with_mistral

def fetch_ai_papers():
    print("Starting script...")

    # Calculate the time range for the last 24 hours
    now = datetime.utcnow()
    yesterday = now - timedelta(days=1)
    
    # Define the ArXiv API endpoint and query parameters
    try:
        print("Starting API request...")
        url = 'http://export.arxiv.org/api/query'
        params = {
            'search_query': 'cat:cs.AI',
            'sortBy': 'submittedDate',
            'sortOrder': 'descending',
            'max_results': 1  # Fetch up to 1000 papers
        }

        # Single API request is made here
        response = requests.get(url, params=params, timeout=10)
        print(f"API request completed with status code {response.status_code}")

        if response.status_code != 200:
            print("Failed to fetch data from ArXiv API.")
            return

        # Parse the XML response
        root = ET.fromstring(response.content)
        print("XML parsing completed.")

        # Extract titles and collect them into an array
        titles = []
        papers = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = entry.find("{http://www.w3.org/2005/Atom}title").text
            summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
            link = entry.find("{http://www.w3.org/2005/Atom}id").text
            titles.append(title)
            papers.append({"title": title, "summary": summary, "link": link})

        print(f"Total papers fetched: {len(titles)}")

        if len(titles) == 0:
            print("No papers fetched within the last 24 hours.")
            return []

        # Combine titles into a single string to feed into Mistral
        combined_titles = " | ".join(titles)

        # Use Mistral to determine the top 3 most relevant titles
        top_titles_response = summarize_with_mistral(
            f"Here is a list of AI research paper titles from the last 24 hours: {combined_titles}. "
            "Please return only the top 3 most relevant titles in the following format: 1. Title, 2. Title, 3. Title."
        )

        # Split the Mistral response into the top 3 titles
        top_titles = top_titles_response.strip().split(', ')
        top_titles = [title.split('. ')[1] for title in top_titles if '. ' in title]  # Extract titles after '1. ', '2. ', etc.
        print(f"Top 3 titles determined by Mistral: {top_titles}")

        # Find and return the full details for the top 3 papers
        top_papers = []
        for paper in papers:
            if paper['title'] in top_titles:
                top_papers.append(paper)

        return top_papers

    except requests.exceptions.Timeout:
        print("API request timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the test
papers = fetch_ai_papers()
if papers:
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Summary: {paper['summary']}")
        print(f"Link: {paper['link']}\n")
else:
    print("No papers fetched.")
