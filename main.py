import streamlit as st

# HTML and CSS for fading effect
fade_effect = """
<style>
    .fade {
        opacity: 0;
        transition: opacity 1s ease-in-out;
    }
    .fade.show {
        opacity: 1;
    }
</style>
<div id="fade-content" class="fade">
    <h2>This is your fading content!</h2>
    <p>This content will fade in when you click the button.</p>
</div>
<script>
    function fadeIn() {
        const fadeContent = document.getElementById('fade-content');
        fadeContent.classList.add('show');
    }
</script>
"""

# Main Streamlit App
st.title("Fading Effect Demo")

if st.button("Click me to reveal content"):
    # Inject HTML with fading effect
    st.markdown(fade_effect, unsafe_allow_html=True)
    # Use JavaScript to trigger the fade in effect
    st.markdown("<script>fadeIn();</script>", unsafe_allow_html=True)



