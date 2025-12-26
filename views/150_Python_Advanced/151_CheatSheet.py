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
    # Getting started
    Tile("Getting started", "Install & Run (venv + pip)", code=
"""python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows (powershell)
.venv\\Scripts\\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
""", featured=True),

    Tile("Getting started", "Project layout (typical)", code=
"""my_project/
  pyproject.toml
  src/my_app/__init__.py
  src/my_app/main.py
  tests/test_main.py
  README.md
""", featured=True),

    Tile("Basics", "Variables, types, f-strings", code=
"""name = "Ralph"
age = 62
pi = 3.14159
active = True

msg = f"{name} is {age} years old. pi≈{pi:.2f}"
print(msg)
"""),

    Tile("Basics", "Lists, dicts, sets", code=
"""nums = [1, 2, 2, 3]
unique = set(nums)          # {1,2,3}
nums.append(4)

person = {"name": "Ada", "role": "engineer"}
person["role"] = "scientist"
"""),

    Tile("Control flow", "if / for / while", code=
"""x = 7
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")

for i in range(3):
    print(i)

n = 3
while n > 0:
    n -= 1
"""),

    Tile("Functions", "Functions + type hints", code=
"""from typing import Iterable

def avg(xs: Iterable[float]) -> float:
    xs = list(xs)
    return sum(xs) / len(xs)

print(avg([1.0, 2.0, 3.0]))
"""),

    Tile("Functions", "Lambda + map/filter (practical)", code=
"""nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
evens = [n for n in nums if n % 2 == 0]
"""),

    Tile("Data classes", "dataclass", code=
"""from dataclasses import dataclass

@dataclass
class User:
    name: str
    admin: bool = False

u = User("Kajal")
print(u)
"""),

    Tile("Errors", "Exceptions", code=
"""try:
    x = int("not-a-number")
except ValueError as e:
    print("bad input:", e)
finally:
    print("done")
"""),

    Tile("Files", "Read / write text and JSON", code=
"""from pathlib import Path
import json

p = Path("data.txt")
p.write_text("hello\\n", encoding="utf-8")
text = p.read_text(encoding="utf-8")

obj = {"a": 1, "b": [2, 3]}
Path("data.json").write_text(json.dumps(obj, indent=2), encoding="utf-8")
loaded = json.loads(Path("data.json").read_text(encoding="utf-8"))
"""),

    Tile("Modules", "Imports + __main__", code=
"""# src/my_app/main.py
def main() -> None:
    print("Hello")

if __name__ == "__main__":
    main()
"""),

    Tile("Testing", "pytest basics", code=
"""# tests/test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
""", body_md="Run: `pip install pytest` then `pytest -q`"),

    Tile("Quality", "ruff formatter + linter", code=
"""pip install ruff
ruff check .
ruff format .
"""),

    Tile("Packaging", "pyproject.toml minimal", code=
"""[project]
name = "my-app"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []

[tool.ruff]
line-length = 100
"""),

    Tile("Async", "async/await + httpx", code=
"""import asyncio
import httpx

async def fetch(url: str) -> str:
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.text

async def main():
    html = await fetch("https://example.com")
    print(len(html))

asyncio.run(main())
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
st.set_page_config(page_title="Python Cheat Sheet", layout="wide")

st.title("Python Cheat Sheet")

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
