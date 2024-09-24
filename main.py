import streamlit as st

# HTML and CSS for fading effect
fade_effect = """
<style>
    .fade {
        opacity: 0;
        transition: opacity 1s ease-in-out;
        margin: 50px;
        padding: 20px;
        background: #fff;
        border: 1px solid #ccc;
    }
    .fade.show {
        opacity: 1;
    }
</style>
<div id="fade-content" class="fade {show_class}">
    <h2>This is your fading content!</h2>
    <p>This content will fade in when you click the button.</p>
</div>
"""

# Main Streamlit App
st.title("Fading Effect Demo")

# Initialize session state for content visibility
if "content_visible" not in st.session_state:
    st.session_state.content_visible = False

# Button to reveal content
if st.button("Click me to reveal content"):
    st.session_state.content_visible = True

# Show fading content with updated class
show_class = "show" 

if st.session_state.content_visible:
    st.markdown(fade_effect.format(show_class=show_class), unsafe_allow_html=True)
    
else:
    print ""





