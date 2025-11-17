"""
Text Analyzer functionality.
Extracted from pages/ollama_miniapps.py
"""


# Analysis prompts for different types
ANALYSIS_PROMPTS = {
    "Summarize": "Summarize the following text concisely:\n\n{text}",
    "Extract Key Points": "Extract the key points from the following text as a bulleted list:\n\n{text}",
    "Sentiment Analysis": "Analyze the sentiment of the following text (positive, negative, or neutral) and explain why:\n\n{text}",
    "Find Main Topics": "Identify the main topics discussed in the following text:\n\n{text}",
    "Translate to Simple Language": "Rewrite the following text in simple, easy-to-understand language:\n\n{text}",
    "Grammar Check": "Check the following text for grammar errors and suggest corrections:\n\n{text}"
}


# Sample texts for testing
SAMPLE_TEXTS = {
    "News Article": "Scientists have discovered a new species of butterfly in the Amazon rainforest. The butterfly, named Morpho amazonicus, has distinctive blue and green wings that shimmer in the sunlight. Researchers believe this discovery could provide insights into the region's biodiversity.",
    "Product Review": "I recently purchased this laptop and I'm extremely impressed. The build quality is excellent, the screen is vibrant, and the battery life exceeds expectations. However, the keyboard could be better and it's a bit pricey.",
    "Technical Text": "The algorithm utilizes a recursive approach to traverse the binary tree in depth-first manner. By implementing memoization, we can optimize the time complexity from O(2^n) to O(n), significantly improving performance for large datasets."
}


def get_analysis_prompt(analysis_type, text):
    """
    Get the appropriate prompt for the analysis type.
    
    Args:
        analysis_type (str): Type of analysis to perform
        text (str): Text to analyze
    
    Returns:
        str: Formatted prompt
    """
    template = ANALYSIS_PROMPTS.get(analysis_type, ANALYSIS_PROMPTS["Summarize"])
    return template.format(text=text)


def analyze_text(model, text, analysis_type):
    """
    Analyze text using Ollama.
    
    Args:
        model (str): Model name (e.g., 'llama2', 'mistral')
        text (str): Text to analyze
        analysis_type (str): Type of analysis to perform
    
    Returns:
        dict: Response with keys 'status', 'message', 'response', and 'stats'
    """
    try:
        import ollama
        
        prompt = get_analysis_prompt(analysis_type, text)
        
        response = ollama.generate(
            model=model,
            prompt=prompt,
            options={'temperature': 0.3}  # Lower temperature for analytical tasks
        )
        
        stats = {
            'analysis_type': analysis_type,
            'model': model,
            'input_length': len(text)
        }
        
        if 'total_duration' in response:
            duration_sec = response['total_duration'] / 1e9
            stats['duration'] = f"{duration_sec:.2f}s"
        
        return {
            'status': 'success',
            'message': 'Analysis complete!',
            'response': response['response'],
            'stats': stats
        }
        
    except ImportError:
        return {
            'status': 'error',
            'message': 'Ollama Python SDK not installed. Run: pip install ollama',
            'response': '',
            'stats': {}
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Error: {str(e)}. Make sure Ollama is running and the model is installed.',
            'response': '',
            'stats': {}
        }


def get_sample_text(sample_name):
    """
    Get a sample text by name.
    
    Args:
        sample_name (str): Name of the sample text
    
    Returns:
        str: Sample text, or empty string if not found
    """
    return SAMPLE_TEXTS.get(sample_name, "")
