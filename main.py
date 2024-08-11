from fetch_paper import fetch_ai_papers
from summarizer import summarize_with_mistral
from startup_generator import generate_ideas

def process_papers(papers):
    summaries = []
    for paper in papers:
        print(f"Processing paper: {paper.get('title', 'No title')}")
        
        summary = paper.get('summary')
        link = paper.get('link')
        
        if not summary:
            print(f"No summary found for paper: {paper.get('title', 'No title')}")
            continue
        if not link:
            print(f"No link found for paper: {paper.get('title', 'No title')}")
            continue
        
        try:
            summarized_text = summarize_with_mistral(summary)
            summaries.append({
                'title': paper['title'],
                'summary': summarized_text,
                'link': link
            })
        except Exception as e:
            print(f"Failed to process paper: {paper.get('title', 'No title')}. Error: {str(e)}")
    return summaries

def main():
    papers = fetch_ai_papers()
    if not papers:
        print("No papers were fetched from the ArXiv API.")
        return

    processed_papers = process_papers(papers)
    startup_ideas = generate_ideas(processed_papers)
    
    for paper in startup_ideas:
        print(f"Title: {paper.get('title', 'No title')}")
        print(f"Summary: {paper.get('summary', 'No summary available')}")
        print(f"Link: {paper.get('link', 'No link available')}")
        print("Startup Ideas:")
        print(f"1. {paper.get('idea1', 'No idea available')}")
        print(f"2. {paper.get('idea2', 'No idea available')}")
        print(f"3. {paper.get('idea3', 'No idea available')}")
        print("-" * 50)

if __name__ == "__main__":
    main()
