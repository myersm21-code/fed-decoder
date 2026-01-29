import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Fed-Speak Decoder", page_icon="🕵️‍♂️")

# 2. The Dictionary (The "New Words" we talked about)
fed_logic = {
    "multi-disciplinary support": "People who can dig holes and not fall into them",
    "synergistic approach": "We have no idea how we're doing this yet",
    "remedial action phase": "The part where we actually start digging",
    "capture management": "Professional stalking of government officials",
    "best value": "We're picking our friends, but legally",
    "stakeholder engagement": "A meeting that could have been an email",
    "period of performance": "The time we have to finish before the money runs out"
}

# 3. The Sidebar Tip Jar
with st.sidebar:
    st.header("Support the Dev")
    st.write("Helping you survive the RFP process.")
    # Replace the link below with your Buy Me a Coffee link later!
    st.link_button("☕ Buy Me a Coffee", "https://www.buymeacoffee.com/yourname")

# 4. The Main App
st.title("🕵️‍♂️ The Fed-Speak Decoder")
st.write("Paste your dry SOW or RFP text below to see the unfiltered truth.")

user_input = st.text_area("Paste Jargon Here:", height=200)

if st.button("Decode Now"):
    if user_input:
        decoded = user_input.lower()
        for jargon, truth in fed_logic.items():
            decoded = decoded.replace(jargon.lower(), f"**[{truth.upper()}]**")
        st.success("Decoded!")
        st.markdown(decoded)
    else:
        st.warning("Please paste some text first!")
