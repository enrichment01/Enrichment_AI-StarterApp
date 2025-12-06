"""Reusable Streamlit helpers for interacting with the Ollama API."""

from __future__ import annotations

import json
from typing import Iterable, List

import requests
import streamlit as st

from lib.helper_ollama import OLLAMA

import os
from pathlib import Path
import streamlit as st
from io import StringIO
import sys
import traceback
import re

HERE = Path(__file__).parent.parent.parent


def get_code(path, as_array=True):
    full_path = os.path.join(HERE, path)

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = f.read()

            if as_array:
                data = data.splitlines()
    except FileNotFoundError:
        data = f"# Error: File not found: {path}"
    except Exception as e:
        data = f"# Error loading file: {str(e)}"

    return data


def get_code_and_output(path, filter_code=True):
    CODE = get_code(path, as_array=filter_code)
    CODE_OUTPUT = ""

    if filter_code:
        # Filter code between special markers
        in_code = False
        in_code_output = False

        filtered = []
        filtered_output = []

        for line in CODE:
            if line.strip().startswith("# --- CODE START: OUTPUT"):
                in_code = False
                in_code_output = True
                continue

            if line.strip().startswith("# --- CODE START"):
                in_code = True
                in_code_output = False
                continue

            if line.strip().startswith("# --- CODE END: OUTPUT"):
                in_code = False
                in_code_output = False
                continue

            if line.strip().startswith("# --- CODE END"):
                in_code = False
                in_code_output = False
                continue

            if in_code:
                filtered.append(line)

            if in_code_output:
                filtered_output.append(line)

        CODE = "\n".join(filtered)
        CODE_OUTPUT = "\n".join(filtered_output)

    return CODE, CODE_OUTPUT


def run(code, namespace=None):
    if namespace is None:
        namespace = {}

    namespace.update(
        {
            "st": st,  # inject streamlit
        }
    )

    # Create string buffers to capture output
    try:
        stdout_buffer = StringIO()
        stderr_buffer = StringIO()

        # Save original stdout/stderr
        original_stdout = sys.stdout
        original_stderr = sys.stderr

        sys.stdout = stdout_buffer
        sys.stderr = stderr_buffer

        # Execute the code
        exec(code, namespace)

        # Get the output
        output = stdout_buffer.getvalue()
        errors = stderr_buffer.getvalue()

    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr

    return output, errors


def run_code(code, language="python"):
    # Only support Python code execution for now
    if language.lower() not in ["python", "py"]:
        st.info(f"Code execution is only supported for Python. Language: {language}")
        return

    # Create a unique key for this button based on a hash of the code
    button_key = f"run_code_{hash(code) % 10000}"

    if st.button("▶️ Run Code", key=button_key):
        with st.spinner("Executing code..."):
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
                        st.code(output, language="text", wrap_lines=True)
                elif errors:
                    st.warning("⚠️ Code executed with warnings")
                    with st.expander("⚠️ Warnings", expanded=True):
                        st.code(errors, language="text", wrap_lines=True)
                else:
                    st.success("✅ Code executed successfully (no output)")

            except Exception as e:
                st.error("❌ Error executing code")
                with st.expander("🐛 Error Details", expanded=True):
                    error_msg = f"{type(e).__name__}: {str(e)}\n\n"
                    error_msg += traceback.format_exc()
                    st.code(error_msg, language="text")

            finally:
                # Restore original stdout/stderr
                sys.stdout = original_stdout
                sys.stderr = original_stderr


def show_code(path):
    CODE, CODE_OUTPUT = get_code_and_output(path)

    tab_code, tab_output = st.tabs(["Code", "Output"])

    with tab_output:
        st.code(CODE_OUTPUT, language="python")

    with tab_code:
        st.code(CODE, language="python", wrap_lines=True)


def show_snippet(code, namespace=None):
    """
    Display a two-column snippet: left shows the source code, right provides a run interface and output.
    """
    st.markdown("----")

    # col_code, col_run = st.columns([1, 1])

    # with col_code:
    st.code(code, language="python")

    # with col_run:
    run(code, namespace)


def build_navigation(folder="views"):
    base_dir = HERE / folder

    pages = {}

    if not base_dir.exists() or not base_dir.is_dir():
        return pages

    for subdir in sorted(p for p in base_dir.iterdir() if p.is_dir()):
        page_list = []

        group = re.sub(r"^\d+_", "", subdir.name).replace("_", " ")

        for file in sorted(
            f
            for f in subdir.iterdir()
            if f.is_file() and f.suffix in {".py", ".md", ".txt"}
        ):
            stem = re.sub(r"^\d+_", "", file.stem)

            page_title = stem.replace("_", " ").replace("-", " ").title()
            page_url = f"{subdir.name}_{file.stem}"

            rel_path = str(file.relative_to(HERE))

            page = st.Page(rel_path, title=page_title, url_path=page_url)

            page_list.append(page)

        pages[group] = page_list

    return pages


def _extract_model_names(models_payload: Iterable[dict]) -> List[str]:
    """Return sorted model names from an Ollama tag payload."""

    names = sorted({str(model.get("model", "")).strip() for model in models_payload})
    return [name for name in names if name]

def models() -> List[str]:
    """Fetch available Ollama models with sensible fallbacks.

    When the Ollama server cannot be reached we keep the UX intact by returning a
    set of commonly available models.
    """

    try:
        response = requests.get(f"{OLLAMA}/api/tags", timeout=3)
        response.raise_for_status()
        payload = response.json().get("models", [])
        names = _extract_model_names(payload)
        return names or ["llama3.2", "mistral:7b"]
    except Exception:  # noqa: BLE001 - best effort fallback for UI friendliness
        return ["llama3.2", "mistral:7b"]


def generate(model: str, prompt: str) -> str:
    """Stream responses from Ollama into the UI and return the final text."""

    box, acc = st.empty(), ""

    with requests.post(
        f"{OLLAMA}/api/generate",
        json={"model": model, "prompt": prompt, "stream": True},
        stream=True,
    ) as response:
        for ln in response.iter_lines():
            if not ln:
                continue
            part = json.loads(ln.decode("utf-8"))
            acc += part.get("response", "")
            box.markdown(acc)
    return acc


def add_select_model(label: str = "Modell") -> str:
    """Render a model selectbox with the available Ollama models."""

    return st.selectbox(label, models())
