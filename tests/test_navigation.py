from pathlib import Path

from app_navigation import build_navigation


def test_build_navigation_groups_by_topic(tmp_path: Path):
    pages = tmp_path / "pages"
    pages.mkdir()

    # create sample page files
    (pages / "200_Streamlit_Basics_Text_Elements.py").write_text("# text elements")
    (pages / "201_Streamlit_Basics_Forms.py").write_text("# forms")
    (pages / "1_Python_Basics.py").write_text("# python basics")
    (pages / "__init__.py").write_text("")

    nav = build_navigation(pages_dir=pages)

    # Topics should include 'Streamlit Basics' and 'Python Basics'
    assert any("streamlit basics" == t.lower() for t in nav.keys())
    assert any("python basics" == t.lower() for t in nav.keys())

    # Check pages under Streamlit Basics
    streamlit_topic = next(t for t in nav.keys() if t.lower() == "streamlit basics")
    titles = [p.title for p in nav[streamlit_topic]]
    assert "Text Elements" in titles
    assert "Forms" in titles

    # Check Python Basics contains a page titled 'Python Basics' (fallback case)
    python_topic = next(t for t in nav.keys() if t.lower() == "python basics")
    titles = [p.title for p in nav[python_topic]]
    assert "Python Basics" in titles
