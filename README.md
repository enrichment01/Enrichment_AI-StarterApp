# 🤖 Streamlit/Ollama Starter App

An interactive starter application showcasing Python, Streamlit, and Ollama integration with educational examples and mini-applications.

## 📚 Features

This application includes over 50 comprehensive example pages organized into 4 main categories:

1. **🐍 Python Basics** (16 pages) - Core Python programming concepts with interactive examples
2. **📊 Streamlit Basics** (18 pages) - Building interactive web apps with Streamlit
3. **🦙 Ollama Python SDK Basics** (19 pages) - Working with Ollama's Python SDK for local LLMs
4. **🚀 Ollama AI MiniApps** (3 apps) - Complete mini-applications powered by Ollama:
   - 📝 Text Generator
   - 💬 Chatbot
   - 🔍 Text Analyzer

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Ollama installed (for Ollama-related features)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/r14r/Enrichment_AI-StarterApp.git
   cd Enrichment_AI-StarterApp
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama (Optional - for AI features):**
   - Visit [https://ollama.ai](https://ollama.ai) to download and install Ollama
   - Pull a model: `ollama pull llama2`

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### Navigation

Use the sidebar to navigate between different pages:

- **🏠 Home** - Overview and introduction
- **🐍 Python Basics** - Learn Python fundamentals
- **📊 Streamlit Basics** - Explore Streamlit components
- **🦙 Ollama Python SDK Basics** - Understand Ollama integration
- **🚀 Ollama AI MiniApps** - Try complete AI applications

### Python Basics (16 Pages)

Interactive examples covering:
- **Fundamentals**: Data types, lists, loops, functions, classes
- **Advanced Concepts**: Dictionary operations, string manipulation, file handling
- **Error Handling**: Exceptions and try-except blocks
- **Advanced Features**: List comprehensions, lambda functions, decorators
- **Standard Library**: Modules and imports, JSON handling, regular expressions
- **Interactive Tools**: Temperature converter

### Streamlit Basics (18 Pages)

Learn Streamlit through examples:
- **Display Elements**: Text elements, status elements, data display, charts
- **Input Widgets**: Text input, number input, sliders, select boxes, checkboxes, buttons
- **Layout Components**: Columns, tabs, containers, sidebar widgets
- **Advanced Features**: File upload/download, session state, forms, expanders
- **Media**: Images, video, audio, camera input
- **Optimization**: Caching data, performance tips
- **Customization**: Custom HTML/CSS components
- **Navigation**: Multipage app structure
- **Interactive Examples**: Progress indicators, data dashboard

### Ollama Python SDK Basics (19 Pages)

Comprehensive guide to Ollama:
- **Getting Started**: Installation, basic usage, model management
- **Core Features**: Chat completions, streaming, text generation, system messages
- **Advanced Techniques**: Multi-turn conversations, context window management
- **Prompt Engineering**: Prompt templates, response parsing, structured output
- **Embeddings**: Semantic search, similarity matching, vector operations
- **Model Selection**: Model comparison, custom model creation
- **Optimization**: Performance tuning, batch processing
- **Specialized**: Vision models for image understanding
- **Parameters**: Temperature, top-p, top-k, and advanced settings
- **Error Handling**: Connection testing, retry logic, troubleshooting

### Ollama AI MiniApps

Three complete applications:

#### 📝 Text Generator
- Generate creative text with customizable prompts
- Adjustable creativity (temperature)
- Control output length
- Multiple model options

#### 💬 Chatbot
- Interactive conversational AI
- Customizable system prompts
- Real-time streaming responses
- Chat history management
- Multiple model support

#### 🔍 Text Analyzer
- Text summarization
- Key point extraction
- Sentiment analysis
- Topic identification
- Language simplification
- Grammar checking

## 🛠️ Configuration

### Models

The app supports multiple Ollama models:
- **llama2** - General purpose, recommended for beginners
- **mistral** - Fast and efficient
- **codellama** - Specialized for code
- **phi** - Lightweight option

To use a model, first pull it:
```bash
ollama pull llama2
ollama pull mistral
```

### Parameters

Customize AI behavior with these parameters:
- **Temperature** (0.0-2.0): Controls randomness
  - 0.0-0.3: Focused, deterministic
  - 0.4-0.7: Balanced
  - 0.8-2.0: Creative, random
- **Max Tokens**: Maximum length of generated text
- **System Prompt**: Defines AI behavior and personality

## 📁 Project Structure

```
Enrichment_AI-StarterApp/
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── pages/                 # Page modules
    ├── __init__.py
    ├── python_basics.py
    ├── streamlit_basics.py
    ├── ollama_basics.py
    └── ollama_miniapps.py
```

## 🔧 Dependencies

- **streamlit** - Web application framework
- **ollama** - Ollama Python SDK
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **requests** - HTTP library

## 💡 Tips

- Start with Python and Streamlit basics if you're new
- Make sure Ollama is running before using AI features
- Experiment with different models and parameters
- Use lower temperatures for factual tasks, higher for creative ones
- Check the "View Source Code" sections to see implementation details

## 🐛 Troubleshooting

### Ollama connection errors
- Ensure Ollama is installed and running
- Check if the model is pulled: `ollama list`
- Try pulling the model: `ollama pull llama2`

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.8 or higher

### Streamlit issues
- Clear cache: `streamlit cache clear`
- Restart the app

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📧 Support

For questions or issues, please open an issue on GitHub.

---

**Happy Learning! 🎉**
