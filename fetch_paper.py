import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def fetch_ai_papers():
    print("Starting script...")

    # Get today's date in the format YYYYMMDD
    today = datetime.today().strftime('%Y%m%d')

    # Define the ArXiv API endpoint and query parameters
    try:
        print("Starting API request...")
        url = 'http://export.arxiv.org/api/query'
        params = {
            'search_query': f'cat:cs.AI AND submittedDate:[{today}0000 TO {today}2359]',
            'sortBy': 'submittedDate',
            'sortOrder': 'descending',
            'max_results': 3  # Fetch only 3 papers
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

        # Extract and print relevant information from the XML response
        papers = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            paper = {
                "title": entry.find("{http://www.w3.org/2005/Atom}title").text,
                "summary": entry.find("{http://www.w3.org/2005/Atom}summary").text,
                "link": entry.find("{http://www.w3.org/2005/Atom}id").text
            }
            papers.append(paper)
            # Print the paper details immediately after fetching
            print(f"Fetched Paper - Title: {paper['title']}")
            print(f"Summary: {paper['summary']}")
            print(f"Link: {paper['link']}\n")

        print(f"Total papers fetched: {len(papers)}")

        return papers

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
