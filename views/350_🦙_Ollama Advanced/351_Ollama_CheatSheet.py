from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional

import streamlit as st


# -----------------------------
# Data model
# -----------------------------
@dataclass(frozen=True)
class Tile:
    section: str
    title: str
    code: Optional[str] = None
    body_md: Optional[str] = None
    featured: bool = False
    links_md: Optional[str] = None


# -----------------------------
# Content (converted from your Markdown)
# -----------------------------
TILES = [
    Tile("Getting started", "Install (macOS / Linux)", code=
"""# macOS (Homebrew)
brew install ollama

# Linux (official install script)
curl -fsSL https://ollama.com/install.sh | sh
""", featured=True),

    Tile("Getting started", "Start server", code=
"""ollama serve
# default: http://127.0.0.1:11434
""", featured=True),

    Tile("Models", "Search / pull / list / remove", code=
"""ollama list
ollama pull llama3.2
ollama pull qwen2.5:7b
ollama rm qwen2.5:7b
"""),

    Tile("Chat", "Quick chat in terminal", code=
"""ollama run llama3.2
# then type your prompt
"""),

    Tile("Chat", "One-shot prompt", code=
"""ollama run llama3.2 "Summarize Python in 2 sentences."
"""),

    Tile("Chat", "System prompt (CLI)", code=
"""ollama run llama3.2 --system "You are a strict JSON generator." "Return {\"ok\":true}."
"""),

    Tile("API", "Generate (non-chat) REST", code=
"""curl http://127.0.0.1:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Write 3 bullet points about Streamlit",
  "stream": false
}'
"""),

    Tile("API", "Chat REST", code=
"""curl http://127.0.0.1:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {"role": "system", "content": "Be concise."},
    {"role": "user", "content": "Explain caching in Streamlit."}
  ],
  "stream": false
}'
"""),

    Tile("API", "Streaming (curl)", code=
"""curl -N http://127.0.0.1:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [{"role":"user","content":"Count to 20."}],
  "stream": true
}'
"""),

    Tile("OpenAI compat", "OpenAI-style endpoint", code=
"""# often used when Ollama is behind a proxy/bridge
# base_url: http://127.0.0.1:11434/v1
# model: "llama3.2"

curl http://127.0.0.1:11434/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "llama3.2",
  "messages": [{"role":"user","content":"Hello"}],
  "stream": false
}'
"""),

    Tile("Python", "Python client (httpx) - chat", code=
"""import httpx

def chat(prompt: str, model: str = "llama3.2") -> str:
    url = "http://127.0.0.1:11434/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }
    r = httpx.post(url, json=payload, timeout=60)
    r.raise_for_status()
    data = r.json()
    return data["message"]["content"]

print(chat("Give 3 ideas for a Streamlit app."))
"""),

    Tile("Python", "Python streaming (SSE-like lines)", code=
"""import json
import httpx

url = "http://127.0.0.1:11434/api/chat"
payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Write a short poem."}],
    "stream": True,
}

with httpx.stream("POST", url, json=payload, timeout=None) as r:
    r.raise_for_status()
    for line in r.iter_lines():
        if not line:
            continue
        obj = json.loads(line)
        if "message" in obj and "content" in obj["message"]:
            print(obj["message"]["content"], end="", flush=True)
"""),

    Tile("Options", "Useful generation options", code=
"""# include these keys in /api/chat or /api/generate:
{
  "temperature": 0.2,
  "top_p": 0.9,
  "num_predict": 256,
  "repeat_penalty": 1.1,
  "seed": 42
}
"""),

    Tile("Prompting", "Force JSON safely (pattern)", code=
"""SYSTEM: You must output valid JSON only, no prose.

USER: Return an object with:
- "title" (string)
- "bullets" (array of 3 strings)
Topic: Streamlit
"""),

    Tile("Operations", "Where are models stored (typical)", body_md=
"Depends on OS and configuration; commonly under a user-level Ollama data directory. Use your system’s Ollama docs/settings for the exact path.", code=
"""ollama list
# check your environment/installation notes for storage location
"""),
]


# -----------------------------
# Helpers
# -----------------------------
def _normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def tile_matches(tile: Tile, query: str) -> bool:
    if not query:
        return True
    q = _normalize(query)
    hay = " ".join(
        _normalize(x)
        for x in [
            tile.section,
            tile.title,
            tile.code or "",
            tile.body_md or "",
            tile.links_md or "",
        ]
    )
    return q in hay


def render_tile(tile: Tile) -> None:
    with st.container(border=True):
        # Title row
        left, right = st.columns([8, 2], vertical_alignment="center")
        with left:
            st.markdown(f"### {tile.title}")
            st.caption(tile.section)
        with right:
            if tile.featured:
                st.badge("Featured")

        if tile.body_md:
            st.markdown(tile.body_md)

        if tile.code:
            st.code(tile.code, language="python")

        if tile.links_md:
            st.markdown(tile.links_md)


# -----------------------------
# App
# -----------------------------
st.set_page_config(page_title="Ollama Cheat Sheet", layout="wide")

st.title("Ollama Cheat Sheet")

sections = sorted({t.section for t in TILES})
with st.sidebar:
    st.header("Filter")
    q = st.text_input("Search", placeholder="e.g. cache_data, sidebar, chart…")
    selected_sections = st.multiselect("Sections", sections, default=sections)
    cols = st.slider("Columns", min_value=1, max_value=4, value=3)
    compact = st.toggle("Compact spacing", value=False)

filtered = [
    t
    for t in TILES
    if t.section in selected_sections and tile_matches(t, q)
]

if not filtered:
    st.info("No tiles match your filters.")
else:
    if compact:
        st.markdown(
            "<style>div[data-testid='stVerticalBlock']{gap:0.5rem;}</style>",
            unsafe_allow_html=True,
        )

    # Display each tile in its own expander
    for tile in filtered:
        badge_text = " 🌟" if tile.featured else ""
        with st.expander(f"{tile.title}{badge_text}", expanded=False):
            st.caption(f"**Section:** {tile.section}")
            
            if tile.body_md:
                st.markdown(tile.body_md)
            
            if tile.code:
                st.code(tile.code, language="python")
            
            if tile.links_md:
                st.markdown(tile.links_md)
