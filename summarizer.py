import subprocess

def summarize_with_mistral(text):
    # Construct the detailed prompt
    detailed_prompt = (
        "Act as a world-class researcher in every single field. "
        "Take this technical abstract and explain it in a way a layman can understand in 4-5 sentences. "
        "Include any key insights that a technical person would glean from it in order to create something applicable in the real world: "
        f"{text}"
    )
    
    # Use subprocess to call the Ollama CLI with the Mistral model
    result = subprocess.run(
        ["ollama", "run", "mistral", detailed_prompt],
        text=True,
        capture_output=True
    )
    
    # Get the output
    output = result.stdout.strip()
    error = result.stderr.strip()
    
    if error:
        print(f"Mistral Error: {error}")
        
    return output
