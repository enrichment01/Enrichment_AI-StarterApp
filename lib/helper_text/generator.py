"""
Text Generator functionality.
Extracted from pages/ollama_miniapps.py
"""


def generate_text(model, prompt, temperature=0.7, max_tokens=200):
    """
    Generate text using Ollama.
    
    Args:
        model (str): Model name (e.g., 'llama2', 'mistral')
        prompt (str): Text prompt for generation
        temperature (float): Creativity level (0.0-2.0)
        max_tokens (int): Maximum length of generated text
    
    Returns:
        dict: Response with keys 'status', 'message', 'response', and 'stats'
    """
    try:
        import ollama
        
        response = ollama.generate(
            model=model,
            prompt=prompt,
            options={
                'temperature': temperature,
                'num_predict': max_tokens,
            }
        )
        
        stats = {
            'model': model,
            'temperature': temperature,
            'max_tokens': max_tokens,
        }
        
        if 'total_duration' in response:
            duration_sec = response['total_duration'] / 1e9
            stats['duration'] = f"{duration_sec:.2f}s"
        
        return {
            'status': 'success',
            'message': 'Generated successfully!',
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
