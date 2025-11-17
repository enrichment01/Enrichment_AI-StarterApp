# Progress bar
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.01)

# Spinner
with st.spinner("Loading..."):
    time.sleep(2)
st.success("Done!")
