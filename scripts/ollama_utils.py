"""
Ollama utilities and helper functions.
Extracted from pages/ollama_basics.py and pages/ollama_miniapps.py
"""


def check_ollama_status():
    """
    Check if Ollama is running and return status information.
    
    Returns:
        dict: Status information with keys 'status', 'message', and 'models'
    """
    try:
        import ollama
        
        models = ollama.list()
        
        return {
            'status': 'success',
            'message': 'Ollama is running!',
            'models': models.get('models', [])
        }
        
    except ImportError:
        return {
            'status': 'error',
            'message': 'Ollama Python SDK not installed. Run: pip install ollama',
            'models': []
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Cannot connect to Ollama: {str(e)}',
            'models': []
        }


def get_available_models():
    """
    Get list of available Ollama models.
    
    Returns:
        list: List of model names, or empty list if error
    """
    try:
        import ollama
        models = ollama.list()
        return [model['name'] for model in models.get('models', [])]
    except:
        return []
