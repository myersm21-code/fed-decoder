import streamlit as st
import re

# 1. Page Configuration
st.set_page_config(page_title="Fed-Speak Decoder", page_icon="🕵️‍♂️")

# 2. The Smart Dictionary
# This is where your "New Words" live. 
# The engine will find these even if they are capitalized differently.
fed_logic = {
    "applicable laws and regulations": "The rules we'll follow until they get in the way",
    "work product": "The stuff you paid for but we'll probably reuse for the next guy",
    "recommendation pertaining to this contract": "The advice you'll ignore until something breaks",
    "disclosure of information": "Spilling the tea to the wrong people",
    "immediately notify": "Send a frantic email at 4:59 PM on a Friday",
    "multi-disciplinary support": "People who can dig holes and not fall into them",
    "synergistic approach": "We have no idea how we're doing this yet",
    "best value": "Picking our friends, but legally",
    "period of performance": "The time we have to finish before the money runs out",
    "stakeholder engagement": "A meeting that could have been an email"
}

# 3. The Sidebar Tip Jar
with st.sidebar:
    st.header("Support the Dev")
    st.write("Helping you survive the RFP process one joke at a time.")
    # Once you set up your 'Buy Me a Coffee' account, paste your link below
    st.link_button("☕ Buy Me a Coffee", "https://www.buymeacoffee.com/yourname")
    st.divider()
    st.caption("Built on a Chromebook for BD Managers.")

# 4. The Main Interface
st.title("🕵️‍♂️ The Fed-Speak Decoder")
st.write("Paste your dry SOW or RFP text below to see the unfiltered truth.")

# The box where users paste their jargon
user_input = st.text_area("Paste Jargon Here:", height=250, placeholder="We require multi-disciplinary support for the upcoming remedial action phase...")

if st.button("Decode the Truth"):
    if user_input:
        # We start with the original text
        decoded = user_input
        
        # The Smart Engine Loop
        # It scans the text for every key in our dictionary
        for jargon, truth in fed_logic.items():
            # This 're' part makes it ignore Uppercase/Lowercase
            pattern = re.compile(re.escape(jargon), re.IGNORECASE)
            # It replaces the dry jargon with your funny 'Truth'
            decoded = pattern.sub(f" **[{truth.upper()}]** ", decoded)
            
        st.success("Decoded!")
        st.markdown(decoded)
    else:
        st.warning("Please paste some text first!")
