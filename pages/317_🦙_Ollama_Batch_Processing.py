import streamlit as st

st.header("📦 Batch Processing — Ollama Basics")
st.markdown("Efficiently processing multiple requests with Ollama.")

# Overview
st.subheader("What is Batch Processing?")

st.write("""
Batch processing allows you to handle multiple AI requests efficiently, 
which is essential for:
- Processing datasets
- Bulk content generation
- Large-scale analysis
- Background jobs
""")

# Basic batch processing
st.subheader("📝 Basic Batch Processing")

basic_batch = """
import ollama

# List of prompts to process
prompts = [
    "Summarize: The quick brown fox...",
    "Summarize: Python is a programming...",
    "Summarize: Machine learning involves..."
]

# Sequential processing
results = []
for i, prompt in enumerate(prompts):
    print(f"Processing {i+1}/{len(prompts)}...")
    
    response = ollama.generate(
        model='phi4-mini',
        prompt=prompt
    )
    
    results.append({
        'prompt': prompt,
        'response': response['response']
    })

# Show results
for result in results:
    print(f"Prompt: {result['prompt'][:50]}...")
    print(f"Response: {result['response'][:100]}...")
    print()
"""

st.code(basic_batch, language="python")

# Parallel processing
st.subheader("⚡ Parallel Processing")

parallel_code = """
import ollama
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def process_single(prompt, model='phi4-mini'):
    '''Process a single prompt'''
    response = ollama.generate(
        model=model,
        prompt=prompt
    )
    return {
        'prompt': prompt,
        'response': response['response']
    }

# Large batch of prompts
prompts = ["Question {i}" for i in range(100)]

# Method 1: ThreadPoolExecutor (recommended)
print("Processing with threads...")
start = time.time()

with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit all tasks
    futures = [
        executor.submit(process_single, prompt) 
        for prompt in prompts
    ]
    
    # Collect results as they complete
    results = []
    for i, future in enumerate(as_completed(futures), 1):
        result = future.result()
        results.append(result)
        print(f"Completed {i}/{len(prompts)}")

elapsed = time.time() - start
print(f"\\nTotal time: {elapsed:.2f}s")
print(f"Average per request: {elapsed/len(prompts):.2f}s")
"""

st.code(parallel_code, language="python")

# Progress tracking
st.subheader("📊 Progress Tracking")

progress_code = """
import ollama
from tqdm import tqdm

def batch_process_with_progress(prompts, model='phi4-mini'):
    '''Process with progress bar'''
    
    results = []
    
    # Using tqdm for progress bar
    for prompt in tqdm(prompts, desc="Processing"):
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        results.append(response['response'])
    
    return results

# Usage
prompts = ["Question " + str(i) for i in range(50)]
results = batch_process_with_progress(prompts)

# In Streamlit
import streamlit as st

prompts = ["Question " + str(i) for i in range(50)]
progress_bar = st.progress(0)
status_text = st.empty()

results = []
for i, prompt in enumerate(prompts):
    status_text.text(f"Processing {i+1}/{len(prompts)}")
    
    response = ollama.generate(
        model='phi4-mini',
        prompt=prompt
    )
    results.append(response['response'])
    
    progress_bar.progress((i + 1) / len(prompts))

status_text.text("Done!")
"""

st.code(progress_code, language="python")

# Error handling
st.subheader("⚠️ Error Handling")

error_handling = """
import ollama
import time

def robust_batch_process(prompts, model='phi4-mini', max_retries=3):
    '''Process batch with retry logic'''
    
    results = []
    failed = []
    
    for i, prompt in enumerate(prompts):
        success = False
        
        for attempt in range(max_retries):
            try:
                response = ollama.generate(
                    model=model,
                    prompt=prompt,
                    options={'num_predict': 500}
                )
                
                results.append({
                    'index': i,
                    'prompt': prompt,
                    'response': response['response'],
                    'status': 'success'
                })
                success = True
                break
                
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
        
        if not success:
            failed.append({
                'index': i,
                'prompt': prompt,
                'status': 'failed'
            })
    
    return results, failed

# Usage
prompts = ["Question " + str(i) for i in range(100)]
results, failed = robust_batch_process(prompts)

print(f"Successful: {len(results)}")
print(f"Failed: {len(failed)}")
"""

st.code(error_handling, language="python")

# Streaming batch
st.subheader("🌊 Streaming Batch Processing")

streaming_batch = """
import ollama

def stream_batch(prompts, model='phi4-mini'):
    '''Stream results for each prompt in batch'''
    
    for i, prompt in enumerate(prompts):
        print(f"\\n--- Response {i+1}/{len(prompts)} ---")
        
        stream = ollama.generate(
            model=model,
            prompt=prompt,
            stream=True
        )
        
        full_response = ""
        for chunk in stream:
            text = chunk['response']
            print(text, end='', flush=True)
            full_response += text
        
        print()  # New line after each response
        
        yield {
            'prompt': prompt,
            'response': full_response
        }

# Usage
prompts = ["Question 1", "Question 2", "Question 3"]

for result in stream_batch(prompts):
    print(f"\\nCompleted: {result['prompt'][:30]}...")
"""

st.code(streaming_batch, language="python")

# Data processing example
st.subheader("📄 Processing CSV Data")

csv_processing = """
import pandas as pd
import ollama
from tqdm import tqdm

# Load data
df = pd.read_csv('reviews.csv')

def analyze_sentiment(text):
    '''Analyze sentiment of text'''
    prompt = f'''
    Analyze the sentiment of this review.
    Respond with only: Positive, Negative, or Neutral
    
    Review: {text}
    
    Sentiment:
    '''
    
    response = ollama.generate(
        model='phi4-mini',
        prompt=prompt,
        options={'num_predict': 10}
    )
    
    return response['response'].strip()

# Process all reviews
tqdm.pandas(desc="Analyzing sentiment")
df['sentiment'] = df['review_text'].progress_apply(analyze_sentiment)

# Save results
df.to_csv('reviews_with_sentiment.csv', index=False)

print("\\nSentiment distribution:")
print(df['sentiment'].value_counts())
"""

st.code(csv_processing, language="python")

# Optimization strategies
st.subheader("🎯 Batch Optimization Strategies")

st.write("**1. Optimal Batch Size**")
st.code("""
# Find optimal batch size for your system
def find_optimal_batch_size(prompts, sizes=[1, 2, 4, 8, 16]):
    '''Test different batch sizes'''
    
    results = {}
    
    for size in sizes:
        start = time.time()
        
        with ThreadPoolExecutor(max_workers=size) as executor:
            futures = [
                executor.submit(process_single, p) 
                for p in prompts[:20]  # Test with 20 prompts
            ]
            list(as_completed(futures))
        
        elapsed = time.time() - start
        results[size] = elapsed
        print(f"Batch size {size}: {elapsed:.2f}s")
    
    optimal = min(results, key=results.get)
    print(f"\\nOptimal batch size: {optimal}")
    return optimal
""", language="python")

st.write("**2. Chunking Large Batches**")
st.code("""
def process_in_chunks(prompts, chunk_size=50, model='phi4-mini'):
    '''Process large batch in chunks'''
    
    all_results = []
    
    for i in range(0, len(prompts), chunk_size):
        chunk = prompts[i:i + chunk_size]
        print(f"Processing chunk {i//chunk_size + 1}...")
        
        # Process chunk
        chunk_results = []
        for prompt in chunk:
            response = ollama.generate(model=model, prompt=prompt)
            chunk_results.append(response['response'])
        
        all_results.extend(chunk_results)
        
        # Optional: Save checkpoint
        save_checkpoint(all_results, f'checkpoint_{i}.pkl')
    
    return all_results
""", language="python")

st.write("**3. Result Caching**")
st.code("""
import hashlib
import pickle
import os

def cached_batch_process(prompts, cache_dir='cache'):
    '''Cache individual results'''
    
    os.makedirs(cache_dir, exist_ok=True)
    results = []
    
    for prompt in prompts:
        # Create cache key
        key = hashlib.md5(prompt.encode()).hexdigest()
        cache_file = f'{cache_dir}/{key}.pkl'
        
        # Check cache
        if os.path.exists(cache_file):
            with open(cache_file, 'rb') as f:
                result = pickle.load(f)
        else:
            # Generate and cache
            response = ollama.generate(
                model='phi4-mini',
                prompt=prompt
            )
            result = response['response']
            
            with open(cache_file, 'wb') as f:
                pickle.dump(result, f)
        
        results.append(result)
    
    return results
""", language="python")

# Interactive demo
st.subheader("🎮 Interactive Batch Demo")

num_items = st.slider("Number of items to process:", 1, 20, 5)

if st.button("Simulate Batch Processing"):
    progress_bar = st.progress(0)
    status = st.empty()
    
    results_container = st.container()
    
    for i in range(num_items):
        status.text(f"Processing item {i+1}/{num_items}...")
        progress_bar.progress((i + 1) / num_items)
        
        # Simulate processing
        time.sleep(0.2)
        
        with results_container:
            st.write(f"✅ Item {i+1}: Processed successfully")
    
    status.text("✨ All items processed!")

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**Efficiency:**
- Use parallel processing for I/O-bound tasks
- Chunk large batches (50-100 items per chunk)
- Cache results to avoid reprocessing
- Monitor resource usage

**Reliability:**
- Implement retry logic
- Save checkpoints for long batches
- Log failures for debugging
- Validate results after processing

**User Experience:**
- Show progress indicators
- Allow cancellation
- Provide time estimates
- Report errors clearly

**Resource Management:**
- Limit concurrent workers (2-8 typical)
- Adjust based on available RAM
- Use appropriate num_ctx to save memory
- Consider rate limiting if needed
""")

# Complete example
st.subheader("📋 Complete Example")

complete_example = """
import ollama
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from tqdm import tqdm

class BatchProcessor:
    def __init__(self, model='phi4-mini', max_workers=4):
        self.model = model
        self.max_workers = max_workers
    
    def process_item(self, item):
        '''Process single item'''
        try:
            response = ollama.generate(
                model=self.model,
                prompt=item['prompt'],
                options={'num_predict': 200}
            )
            return {
                'id': item['id'],
                'result': response['response'],
                'status': 'success'
            }
        except Exception as e:
            return {
                'id': item['id'],
                'error': str(e),
                'status': 'failed'
            }
    
    def process_batch(self, items):
        '''Process batch with parallel execution'''
        results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self.process_item, item)
                for item in items
            ]
            
            for future in tqdm(futures, desc="Processing"):
                results.append(future.result())
        
        return results

# Usage
processor = BatchProcessor(model='phi4-mini', max_workers=4)

items = [
    {'id': 1, 'prompt': 'Question 1'},
    {'id': 2, 'prompt': 'Question 2'},
    # ... more items
]

results = processor.process_batch(items)

# Convert to DataFrame
df = pd.DataFrame(results)
print(df)
"""

st.code(complete_example, language="python")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **Start small**: Test with small batches first
- **Monitor resources**: Watch RAM/CPU during processing
- **Parallel sweet spot**: Usually 2-8 workers optimal
- **Checkpoints**: Save progress for long batches
- **Error handling**: Always expect and handle failures
- **Testing**: Validate results on a sample first
""")
