# 🦙 Ollama Helper Test Suite

Comprehensive test suite for `lib/helper_ollama/__init__.py`

## 📁 Test Files

### 900_Overview.py

Main overview page that describes the entire test suite and all functions.

### 901_Test_Status_Discovery.py

**Functions Tested:**

- `check_ollama_status()` - Check if Ollama is running
- `get_available_models()` - Get list of model names

### 902_Test_Model_Filtering.py

**Functions Tested:**

- `get_local_llms(func=None)` - Get all models or filter by capability
- Tests filtering by: embedding, vision, tools, thinking, chat
- Tests error handling for invalid function types

### 903_Test_Model_Categorization.py

**Functions Tested:**

- `list_models_by_capability()` - Organize models by capability
- Displays summary statistics for each capability type

### 904_Test_Model_Info.py

**Functions Tested:**

- `get_model_info(model_name)` - Get detailed model information
- Shows model details, parameters, templates, system prompts, and modelfile

### 905_Test_Generate.py

**Functions Tested:**

- `generate(model_name, prompt, stream=False, **kwargs)` - Generate text
- Tests various prompts and parameters (temperature, top_p, top_k)
- Shows performance metrics (tokens/sec, duration)

### 906_Test_Chat.py

**Functions Tested:**

- `chat(model_name, messages, stream=False, **kwargs)` - Chat interface
- Tests multi-turn conversations with system prompts
- Includes conversation history management

### 907_Test_Embeddings.py

**Functions Tested:**

- `embeddings(model_name, text, **kwargs)` - Generate embeddings
- Displays embedding statistics and visualization
- Includes similarity comparison feature

## 🚀 Usage

1. **Install Ollama:**

   ```bash
   curl https://ollama.ai/install.sh | sh
   ```

2. **Pull models:**

   ```bash
   ollama pull llama3.2              # Chat model
   ollama pull llama3.2-vision       # Vision model
   ollama pull nomic-embed-text      # Embedding model
   ```

3. **Start Ollama:**

   ```bash
   ollama serve
   ```

4. **Run Streamlit:**

   ```bash
   streamlit run app.py
   ```

5. **Navigate to:** `900_🦙_Tests` section in the sidebar

## 📚 Model Capabilities

| Capability | Description | Example Models |
|------------|-------------|----------------|
| **embedding** | Text embeddings for vector representations | nomic-embed-text, mxbai-embed-large |
| **vision** | Image processing and understanding | llama3.2-vision, llava |
| **tools** | Function/tool calling support | llama3.1, mistral, qwen |
| **thinking** | Reasoning and problem-solving | deepseek-r1, qwen-reasoning |
| **chat** | General conversation | llama3.2, mistral, phi3 |

## 🧪 Test Features

Each test page includes:

- ✅ Interactive UI for testing functions
- ✅ Multiple example inputs
- ✅ Advanced parameter controls
- ✅ Detailed result displays
- ✅ Error handling demonstrations
- ✅ Code preview
- ✅ `show_code(__file__)` at the end for source code viewing

## 📖 Functions Reference

### Status & Discovery

```python
check_ollama_status() -> dict
get_available_models() -> list[str]
```

### Model Filtering

```python
get_local_llms(func=None) -> list[dict]
list_models_by_capability() -> dict
get_model_info(model_name) -> dict
```

### Generation & Chat

```python
generate(model_name, prompt, stream=False, **kwargs) -> Response
chat(model_name, messages, stream=False, **kwargs) -> Response
embeddings(model_name, text, **kwargs) -> Response
```

## 🔍 Example Usage

### Get Chat Models

```python
from lib.helper_ollama import get_local_llms

chat_models = get_local_llms(func="chat")
for model in chat_models:
    print(f"{model['name']}: {model['capabilities']}")
```

### Generate Text

```python
from lib.helper_ollama import generate

result = generate(
    model_name="llama3.2",
    prompt="Write a haiku about coding",
    temperature=0.7
)
print(result.response)
```

### Chat

```python
from lib.helper_ollama import chat

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Python?"}
]

result = chat(model_name="llama3.2", messages=messages)
print(result.message.content)
```

### Generate Embeddings

```python
from lib.helper_ollama import embeddings

result = embeddings(
    model_name="nomic-embed-text",
    text="Hello, world!"
)
print(f"Dimension: {len(result.embedding)}")
```

## 🎯 Test Coverage

- ✅ All 8 functions tested
- ✅ Parameter variations
- ✅ Error handling
- ✅ Edge cases
- ✅ Interactive examples
- ✅ Performance metrics
- ✅ Visual displays

## 📝 Notes

- Each test file is independent and can be run separately
- Tests require Ollama to be running locally
- Some tests require specific model types (e.g., embedding models for embeddings test)
- All tests include `show_code(__file__)` for viewing source code
