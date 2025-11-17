"""
Utility functions for managing code snippets in the application.
"""
import streamlit as st
import os
from io import StringIO
import sys
import traceback


def get_code(path):
    """
    Load code content from a file.
    
    Args:
        path: Path to the code file relative to code_snippets directory
        
    Returns:
        str: Content of the code file
    """
    # Get the base directory (project root)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    code_snippets_dir = os.path.join(base_dir, 'code_snippets')
    
    # Construct full path
    full_path = os.path.join(code_snippets_dir, path)
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"# Error: File not found: {path}"
    except Exception as e:
        return f"# Error loading file: {str(e)}"


def run_code(code, language="python"):
    """
    Display a button to run the provided code.
    Shows the output in an expandable section.
    
    Args:
        code: The code content to execute
        language: Programming language (default: python)
    """
    # Only support Python code execution for now
    if language.lower() not in ["python", "py"]:
        st.info(f"Code execution is only supported for Python. Language: {language}")
        return
    
    # Create a unique key for this button based on a hash of the code
    button_key = f"run_code_{hash(code) % 10000}"
    
    if st.button("▶️ Run Code", key=button_key):
        # Create string buffers to capture output
        stdout_buffer = StringIO()
        stderr_buffer = StringIO()
        
        # Save original stdout/stderr
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        
        try:
            # Redirect stdout/stderr
            sys.stdout = stdout_buffer
            sys.stderr = stderr_buffer
            
            # Create a namespace for execution
            namespace = {}
            
            # Execute the code
            exec(code, namespace)
            
            # Get the output
            output = stdout_buffer.getvalue()
            errors = stderr_buffer.getvalue()
            
            # Display results
            if output:
                st.success("✅ Code executed successfully!")
                with st.expander("📤 Output", expanded=True):
                    st.code(output, language="text")
            elif errors:
                st.warning("⚠️ Code executed with warnings")
                with st.expander("⚠️ Warnings", expanded=True):
                    st.code(errors, language="text")
            else:
                st.success("✅ Code executed successfully (no output)")
                
        except Exception as e:
            st.error(f"❌ Error executing code")
            with st.expander("🐛 Error Details", expanded=True):
                error_msg = f"{type(e).__name__}: {str(e)}\n\n"
                error_msg += traceback.format_exc()
                st.code(error_msg, language="text")
        
        finally:
            # Restore original stdout/stderr
            sys.stdout = original_stdout
            sys.stderr = original_stderr
