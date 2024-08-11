from summarizer import summarize_with_mistral

def generate_ideas(papers):
    ideas = []
    for paper in papers:
        # Debugging statement
        print(f"Brainstorming startup ideas for paper: {paper['title']}")

        # Provide an example in the prompt to guide the model
        full_ideas = summarize_with_mistral(
            f"Generate three Y-Combinator worthy SaaS startup ideas based on this paper: {paper['summary']}. "
            "Each idea should be concise and no more than 3-4 sentences. Number each idea as '1.', '2.', and '3.'. "
            "For example:\n"
            "1. AI-Powered Content Creation: A platform that uses GPT-3 to help marketers generate high-quality content at scale. Users input key topics, and the AI generates tailored content pieces, saving time and resources.\n"
            "2. Automated Code Review: A tool that integrates with existing development environments to automatically review and suggest improvements to code, leveraging AI to catch bugs and ensure best practices.\n"
            "3. Personalized Learning Paths: An AI-driven platform that assesses users' learning styles and objectives to create personalized education paths, optimizing the learning process for better outcomes."
        )

        # Split the output into three parts based on the numbering '1.', '2.', '3.'
        idea_parts = full_ideas.split('1.')
        
        if len(idea_parts) > 1:
            idea_parts = idea_parts[1].split('2.')
            idea1 = idea_parts[0].strip()
            if len(idea_parts) > 1:
                idea_parts = idea_parts[1].split('3.')
                idea2 = idea_parts[0].strip()
                idea3 = idea_parts[1].strip() if len(idea_parts) > 1 else "No idea available"
            else:
                idea2 = "No idea available"
                idea3 = "No idea available"
        else:
            idea1 = "No idea available"
            idea2 = "No idea available"
            idea3 = "No idea available"

        ideas.append({
            'title': paper['title'],
            'idea1': idea1.replace("Summary:", "").strip(),
            'idea2': idea2.replace("Summary:", "").strip(),
            'idea3': idea3.replace("Summary:", "").strip(),
            'summary': paper.get('summary', 'No summary available'),
            'link': paper.get('link', 'No link available')
        })
    return ideas
