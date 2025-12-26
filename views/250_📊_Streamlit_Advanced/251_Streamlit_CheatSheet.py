# app.py
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
TILES: List[Tile] = [
    # Masonry #1 (featured)
    Tile(
        section="Getting started",
        title="Install & Import",
        code=(
            "pip install streamlit\n\n"
            "streamlit run first_app.py\n\n"
            "# Import convention\n"
            ">>> import streamlit as st\n"
        ),
        featured=True,
    ),
    Tile(
        section="Getting started",
        title="Pre-release features",
        code="pip uninstall streamlit\npip install streamlit-nightly --upgrade\n",
        body_md="Learn more about experimental features in the Streamlit docs.",
        featured=True,
    ),
    Tile(
        section="Getting started",
        title="Command line",
        code=(
            "streamlit cache clear\n"
            "streamlit config show\n"
            "streamlit docs\n"
            "streamlit hello\n"
            "streamlit help\n"
            "streamlit init\n"
            "streamlit run streamlit_app.py\n"
            "streamlit version\n"
        ),
        featured=True,
    ),
    # Masonry #2
    Tile(
        section="Text",
        title="Magic commands",
        code=(
            "# Magic commands implicitly\n"
            "# call st.write().\n"
            "\"_This_ is some **Markdown**\"\n"
            "my_variable\n"
            "\"dataframe:\", my_data_frame\n"
        ),
    ),
    Tile(
        section="Text",
        title="Display text",
        code=(
            "st.write(\"Most objects\") # df, err, func, keras!\n"
            "st.write([\"st\", \"is <\", 3])\n"
            "st.write_stream(my_generator)\n"
            "st.write_stream(my_llm_stream)\n\n"
            "st.text(\"Fixed width text\")\n"
            "st.markdown(\"_Markdown_\")\n"
            "st.latex(r\"\"\" e^{i\\pi} + 1 = 0 \"\"\")\n"
            "st.title(\"My title\")\n"
            "st.header(\"My header\")\n"
            "st.subheader(\"My sub\")\n"
            "st.code(\"for i in range(8): foo()\")\n"
            "st.badge(\"New\")\n"
            "st.html(\"<p>Hi!</p>\")\n"
        ),
    ),
    Tile(
        section="Data",
        title="Display data",
        code=(
            "st.dataframe(my_dataframe)\n"
            "st.table(data.iloc[0:10])\n"
            "st.json({\"foo\":\"bar\",\"fu\":\"ba\"})\n"
            "st.metric(\"My metric\", 42, 2)\n"
        ),
    ),
    Tile(
        section="Media",
        title="Display media",
        code=(
            "st.image(\"./header.png\")\n"
            "st.logo(\"logo.jpg\")\n"
            "st.pdf(\"my_document.pdf\")\n"
            "st.audio(data)\n"
            "st.video(data)\n"
            "st.video(data, subtitles=\"./subs.vtt\")\n"
        ),
    ),
    Tile(
        section="Charts",
        title="Display charts",
        code=(
            "st.area_chart(df)\n"
            "st.bar_chart(df)\n"
            "st.bar_chart(df, horizontal=True)\n"
            "st.line_chart(df)\n"
            "st.map(df)\n"
            "st.scatter_chart(df)\n\n"
            "st.altair_chart(chart)\n"
            "st.graphviz_chart(fig)\n"
            "st.plotly_chart(fig)\n"
            "st.pydeck_chart(chart)\n"
            "st.pyplot(fig)\n"
            "st.vega_lite_chart(df, spec)\n\n"
            "# Work with user selections\n"
            "event = st.plotly_chart(\n"
            "    df,\n"
            "    on_select=\"rerun\"\n"
            ")\n"
            "event = st.altair_chart(\n"
            "    chart,\n"
            "    on_select=\"rerun\"\n"
            ")\n"
            "event = st.vega_lite_chart(\n"
            "    df,\n"
            "    spec,\n"
            "    on_select=\"rerun\"\n"
            ")\n"
        ),
        body_md="To use Bokeh, see the custom component `streamlit-bokeh`.",
    ),
    Tile(
        section="Layout",
        title="Add elements to sidebar",
        code=(
            "# Just add it after st.sidebar:\n"
            "a = st.sidebar.radio(\"Select one:\", [1, 2])\n\n"
            "# Or use \"with\" notation:\n"
            "with st.sidebar:\n"
            "    st.radio(\"Select one:\", [1, 2])\n"
        ),
    ),
    Tile(
        section="Layout",
        title="Columns",
        code=(
            "# Two equal columns:\n"
            "col1, col2 = st.columns(2)\n"
            "col1.write(\"This is column 1\")\n"
            "col2.write(\"This is column 2\")\n\n"
            "# Three different columns:\n"
            "col1, col2, col3 = st.columns([3, 1, 1])\n"
            "# col1 is larger.\n\n"
            "# Bottom-aligned columns\n"
            "col1, col2 = st.columns(2, vertical_alignment=\"bottom\")\n\n"
            "# You can also use \"with\" notation:\n"
            "with col1:\n"
            "    st.radio(\"Select one:\", [1, 2])\n"
        ),
    ),
    Tile(
        section="Layout",
        title="Tabs",
        code=(
            "# Insert containers separated into tabs:\n"
            "tab1, tab2 = st.tabs([\"Tab 1\", \"Tab2\"])\n"
            "tab1.write(\"this is tab 1\")\n"
            "tab2.write(\"this is tab 2\")\n\n"
            "# You can also use \"with\" notation:\n"
            "with tab1:\n"
            "    st.radio(\"Select one:\", [1, 2])\n"
        ),
    ),
    Tile(
        section="Layout",
        title="Expandable containers",
        code=(
            "expand = st.expander(\"My label\", icon=\":material/info:\")\n"
            "expand.write(\"Inside the expander.\")\n"
            "pop = st.popover(\"Button label\")\n"
            "pop.checkbox(\"Show all\")\n\n"
            "# You can also use \"with\" notation:\n"
            "with expand:\n"
            "    st.radio(\"Select one:\", [1, 2])\n"
        ),
    ),
    Tile(
        section="Control flow",
        title="Control flow",
        code=(
            "# Stop execution immediately:\n"
            "st.stop()\n"
            "# Rerun script immediately:\n"
            "st.rerun()\n"
            "# Navigate to another page:\n"
            "st.switch_page(\"pages/my_page.py\")\n\n"
            "# Define a navigation widget in your entrypoint file\n"
            "pg = st.navigation(\n"
            "    st.Page(\"page1.py\", title=\"Home\", url_path=\"home\", default=True)\n"
            "    st.Page(\"page2.py\", title=\"Preferences\", url_path=\"settings\")\n"
            ")\n"
            "pg.run()\n\n"
            "# Group multiple widgets:\n"
            "with st.form(key=\"my_form\"):\n"
            "    username = st.text_input(\"Username\")\n"
            "    password = st.text_input(\"Password\")\n"
            "    st.form_submit_button(\"Login\")\n\n"
            "# Define a dialog function\n"
            "@st.dialog(\"Welcome!\")\n"
            "def modal_dialog():\n"
            "    st.write(\"Hello\")\n\n"
            "modal_dialog()\n\n"
            "# Define a fragment\n"
            "@st.fragment\n"
            "def fragment_function():\n"
            "    df = get_data()\n"
            "    st.line_chart(df)\n"
            "    st.button(\"Update\")\n\n"
            "fragment_function()\n"
        ),
    ),
    Tile(
        section="Widgets",
        title="Display interactive widgets",
        code=(
            "st.button(\"Click me\")\n"
            "st.download_button(\"Download file\", data)\n"
            "st.link_button(\"Go to gallery\", url)\n"
            "st.page_link(\"app.py\", label=\"Home\")\n"
            "st.data_editor(\"Edit data\", data)\n"
            "st.checkbox(\"I agree\")\n"
            "st.feedback(\"thumbs\")\n"
            "st.pills(\"Tags\", [\"Sports\", \"Politics\"])\n"
            "st.radio(\"Pick one\", [\"cats\", \"dogs\"])\n"
            "st.segmented_control(\"Filter\", [\"Open\", \"Closed\"])\n"
            "st.toggle(\"Enable\")\n"
            "st.selectbox(\"Pick one\", [\"cats\", \"dogs\"])\n"
            "st.multiselect(\"Buy\", [\"milk\", \"apples\", \"potatoes\"])\n"
            "st.slider(\"Pick a number\", 0, 100)\n"
            "st.select_slider(\"Pick a size\", [\"S\", \"M\", \"L\"])\n"
            "st.text_input(\"First name\")\n"
            "st.number_input(\"Pick a number\", 0, 10)\n"
            "st.text_area(\"Text to translate\")\n"
            "st.date_input(\"Your birthday\")\n"
            "st.time_input(\"Meeting time\")\n"
            "st.file_uploader(\"Upload a CSV\")\n"
            "st.audio_input(\"Record a voice message\")\n"
            "st.camera_input(\"Take a picture\")\n"
            "st.color_picker(\"Pick a color\")\n\n"
            "# Use widgets' returned values in variables:\n"
            "for i in range(int(st.number_input(\"Num:\"))):\n"
            "    foo()\n"
            "if st.sidebar.selectbox(\"I:\",[\"f\"]) == \"f\":\n"
            "    b()\n"
            "my_slider_val = st.slider(\"Quinn Mallory\", 1, 88)\n"
            "st.write(slider_val)\n\n"
            "# Disable widgets to remove interactivity:\n"
            "st.slider(\"Pick a number\", 0, 100, disabled=True)\n"
        ),
    ),
    Tile(
        section="Chat",
        title="Build chat-based apps",
        code=(
            "# Insert a chat message container.\n"
            "with st.chat_message(\"user\"):\n"
            "    st.write(\"Hello 👋\")\n"
            "    st.line_chart(np.random.randn(30, 3))\n\n"
            "# Display a chat input widget at the bottom of the app.\n"
            "st.chat_input(\"Say something\")\n\n"
            "# Display a chat input widget inline.\n"
            "with st.container():\n"
            "    st.chat_input(\"Say something\")\n"
        ),
        body_md="Learn how to build a basic LLM chat app in the Streamlit tutorials.",
    ),
    Tile(
        section="Data",
        title="Mutate data",
        code=(
            "# Add rows to a dataframe after\n"
            "# showing it.\n"
            "element = st.dataframe(df1)\n"
            "element.add_rows(df2)\n\n"
            "# Add rows to a chart after\n"
            "# showing it.\n"
            "element = st.line_chart(df1)\n"
            "element.add_rows(df2)\n"
        ),
    ),
    Tile(
        section="Debug",
        title="Display code (echo)",
        code='with st.echo():\n    st.write("Code will be executed and printed")\n',
    ),
    Tile(
        section="Utilities",
        title="Placeholders, help, and options",
        code=(
            "# Replace any single element.\n"
            "element = st.empty()\n"
            "element.line_chart(...)\n"
            "element.text_input(...)  # Replaces previous.\n\n"
            "# Insert out of order.\n"
            "elements = st.container()\n"
            "elements.line_chart(...)\n"
            "st.write(\"Hello\")\n"
            "elements.text_input(...)  # Appears above \"Hello\".\n\n"
            "# Horizontal flex\n"
            "flex = st.container(horizontal=True)\n"
            "flex.button(\"A\")\n"
            "flex.button(\"B\")\n\n"
            "st.help(pandas.DataFrame)\n"
            "st.get_option(key)\n"
            "st.set_option(key, value)\n"
            "st.set_page_config(layout=\"wide\")\n"
            "st.query_params[key]\n"
            "st.query_params.from_dict(params_dict)\n"
            "st.query_params.get_all(key)\n"
            "st.query_params.clear()\n"
            "st.html(\"<p>Hi!</p>\")\n"
        ),
    ),
    Tile(
        section="Data",
        title="Connect to data sources",
        code=(
            "st.connection(\"pets_db\", type=\"sql\")\n"
            "conn = st.connection(\"sql\")\n"
            "conn = st.connection(\"snowflake\")\n\n"
            "class MyConnection(BaseConnection[myconn.MyConnection]):\n"
            "    def _connect(self, **kwargs) -> MyConnection:\n"
            "        return myconn.connect(**self._secrets, **kwargs)\n"
            "    def query(self, query):\n"
            "        return self._instance.query(query)\n"
        ),
    ),
    Tile(
        section="Performance",
        title="Optimize performance (cache)",
        body_md="Includes examples for caching data objects and global resources.",
        code=(
            "###### Cache data objects\n\n"
            "# E.g. Dataframe computation, storing downloaded data, etc.\n"
            "@st.cache_data\n"
            "def foo(bar):\n"
            "    # Do something expensive and return data\n"
            "    return data\n"
            "# Executes foo\n"
            "d1 = foo(ref1)\n"
            "# Does not execute foo\n"
            "# Returns cached item by value, d1 == d2\n"
            "d2 = foo(ref1)\n"
            "# Different arg, so function foo executes\n"
            "d3 = foo(ref2)\n"
            "# Clear the cached value for foo(ref1)\n"
            "foo.clear(ref1)\n"
            "# Clear all cached entries for this function\n"
            "foo.clear()\n"
            "# Clear values from *all* in-memory or on-disk cached functions\n"
            "st.cache_data.clear()\n\n"
            "###### Cache global resources\n\n"
            "# E.g. TensorFlow session, database connection, etc.\n"
            "@st.cache_resource\n"
            "def foo(bar):\n"
            "    # Create and return a non-data object\n"
            "    return session\n"
            "# Executes foo\n"
            "s1 = foo(ref1)\n"
            "# Does not execute foo\n"
            "# Returns cached item by reference, s1 == s2\n"
            "s2 = foo(ref1)\n"
            "# Different arg, so function foo executes\n"
            "s3 = foo(ref2)\n"
            "# Clear the cached value for foo(ref1)\n"
            "foo.clear(ref1)\n"
            "# Clear all cached entries for this function\n"
            "foo.clear()\n"
            "# Clear all global resources from cache\n"
            "st.cache_resource.clear()\n"
        ),
    ),
    Tile(
        section="UX",
        title="Display progress and status",
        code=(
            "# Show a spinner during a process\n"
            "with st.spinner(text=\"In progress\"):\n"
            "    time.sleep(3)\n"
            "    st.success(\"Done\")\n\n"
            "# Show and update progress bar\n"
            "bar = st.progress(50)\n"
            "time.sleep(3)\n"
            "bar.progress(100)\n\n"
            "with st.status(\"Authenticating...\") as s:\n"
            "    time.sleep(2)\n"
            "    st.write(\"Some long response.\")\n"
            "    s.update(label=\"Response\")\n\n"
            "st.balloons()\n"
            "st.snow()\n"
            "st.toast(\"Warming up...\")\n"
            "st.error(\"Error message\")\n"
            "st.warning(\"Warning message\")\n"
            "st.info(\"Info message\")\n"
            "st.success(\"Success message\")\n"
            "st.exception(e)\n"
        ),
    ),
    Tile(
        section="Personalization",
        title="Personalize apps for users",
        code=(
            "# Authenticate users\n"
            "if not st.user.is_logged_in:\n"
            "    st.login(\"my_provider\")\n"
            "f\"Hi, {st.user.name}\"\n"
            "st.logout()\n\n"
            "# Get dictionaries of cookies, headers, locale, and browser data\n"
            "st.context.cookies\n"
            "st.context.headers\n"
            "st.context.ip_address\n"
            "st.context.is_embedded\n"
            "st.context.locale\n"
            "st.context.theme.type\n"
            "st.context.timezone\n"
            "st.context.timezone_offset\n"
            "st.context.url\n"
        ),
    ),
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
st.set_page_config(page_title="Streamlit Cheat Sheet", layout="wide")

st.title("Streamlit Cheat Sheet")

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
