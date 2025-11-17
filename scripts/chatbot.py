"""
Chatbot functionality.
Extracted from pages/ollama_miniapps.py
"""


def generate_chat_response(model, messages, temperature=0.7, stream=False):
    """
    Generate a chat response using Ollama.
    
    Args:
        model (str): Model name (e.g., 'llama2', 'mistral')
        messages (list): List of message dictionaries with 'role' and 'content'
        temperature (float): Creativity level (0.0-2.0)
        stream (bool): Whether to stream the response
    
    Returns:
        If stream=False, returns dict with 'status', 'message', 'response'
        If stream=True, returns generator for streaming chunks
    """
    try:
        import ollama
        
        response = ollama.chat(
            model=model,
            messages=messages,
            stream=stream,
            options={'temperature': temperature}
        )
        
        if stream:
            return response
        else:
            return {
                'status': 'success',
                'message': 'Response generated!',
                'response': response['message']['content']
            }
        
    except ImportError:
        if stream:
            def error_gen():
                yield {
                    'message': {
                        'content': '❌ Ollama Python SDK not installed. Run: pip install ollama'
                    }
                }
            return error_gen()
        else:
            return {
                'status': 'error',
                'message': 'Ollama Python SDK not installed. Run: pip install ollama',
                'response': ''
            }
    except Exception as e:
        if stream:
            def error_gen():
                yield {
                    'message': {
                        'content': f'❌ Error: {str(e)}\n\nMake sure Ollama is running and the model is installed.'
                    }
                }
            return error_gen()
        else:
            return {
                'status': 'error',
                'message': f'Error: {str(e)}',
                'response': ''
            }


def prepare_chat_messages(user_messages, system_prompt="You are a helpful AI assistant."):
    """
    Prepare messages for chat API by adding system prompt.
    
    Args:
        user_messages (list): List of user/assistant message dictionaries
        system_prompt (str): System prompt to set behavior
    
    Returns:
        list: Complete messages list with system prompt
    """
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(user_messages)
    return messages
