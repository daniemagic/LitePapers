from summarizer import summarize_with_mistral

def generate_ideas(papers):
    ideas = []
    for paper in papers:
        idea1 = summarize_with_mistral(f"Generate a Y-Combinator worthy, concise SaaS startup idea based on this paper: {paper['summary']} Keep it 3-4 sentences maximum")
        idea2 = summarize_with_mistral(f"Generate a different Y-Combinator worthy, SaaS startup idea based on this paper: {paper['summary']} Keep it 3-4 sentences maximum")
        idea3 = summarize_with_mistral(f"Generate yet another Y-Combinator worthyaaS startup idea based on this paper: {paper['summary']}. Keep it 3-4 sentences maximum")
        
        ideas.append({
            'title': paper['title'],
            'idea1': idea1,
            'idea2': idea2,
            'idea3': idea3,
            'summary': paper.get('summary', 'No summary available'),
            'one_liner': paper.get('one_liner', 'No one-liner available'),
            'link': paper.get('link', 'No link available')
        })
    return ideas
