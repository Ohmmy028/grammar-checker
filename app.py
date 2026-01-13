import streamlit as st
import language_tool_python

# 1. Set up the page layout
st.set_page_config(page_title="Grade 12 English Checker", page_icon="📝")

# 2. Add a simple title and instructions
st.title("📝 Grade 12 Self-Check Tool")
st.write("Paste your sentences below to check for grammar and structure errors.")

# 3. Create the input box
user_text = st.text_area("Type or paste your text here:", height=200)

# 4. The "Check" Logic
if st.button("Check My Writing"):
    if user_text:
        # Show a loading spinner while it thinks
        with st.spinner("Checking your grammar..."):
            # Load the grammar tool (English - US)
            tool = language_tool_python.LanguageTool('en-US')
            matches = tool.check(user_text)

            # If errors are found
            if len(matches) > 0:
                st.warning(f"I found {len(matches)} things to improve:")
                
                # Loop through each error and display it cleanly
                for match in matches:
                    with st.expander(f"🔴 Issue: {match.context}"):
                        st.write(f"**Explanation:** {match.message}")
                        # Show suggestion if available
                        if match.replacements:
                            st.write(f"**Try this instead:** {match.replacements[0]}")
            else:
                st.balloons()
                st.success("Great job! No grammar errors found.")
    else:
        st.info("Please enter some text above first.")

# 5. Footer
st.markdown("---")
st.caption("Teacher's Tip: If you see a suggestion, write it down in your notebook!")
