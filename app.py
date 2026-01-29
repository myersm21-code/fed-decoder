import streamlit as st
import re
import random

# 1. Page Configuration
st.set_page_config(page_title="The Fed-Speak Ultra-Decoder", page_icon="🕵️‍♂️")

# 2. THE MASSIVE DICTIONARY
# I've added 15+ new common federal jargon terms here.
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
    "stakeholder engagement": "A meeting that could have been an email",
    "subject to availability of funds": "We'll pay you... maybe. Someday.",
    "firm-fixed-price": "We're going to lose money on this, aren't we?",
    "time and materials": "A license to print money very slowly",
    "performance-based": "We'll move the goalposts once you start running",
    "government-furnished equipment": "A 10-year-old laptop with a broken 'Enter' key",
    "technical acceptable": "It's the cheapest thing that isn't literally on fire",
    "past performance": "The art of making a disaster look like a triumph",
    "cure notice": "The 'we're breaking up' text of the contracting world",
    "de-scope": "We ran out of money so we're pretending we didn't want this anyway"
}

# 3. Random Contractor Pro-Tips
pro_tips = [
    "PRO-TIP: If the SOW is over 100 pages, the Contracting Officer hasn't read it either.",
    "PRO-TIP: 'Urgent Requirement' usually means someone forgot to file paperwork three months ago.",
    "PRO-TIP: The 'Kickoff Meeting' is just where everyone agrees on who to blame later.",
    "PRO-TIP: A 'Modified' requirement is just a new way for the client to be unhappy."
]

# 4. Sidebar Tip Jar
with st.sidebar:
    st.header("Support the Dev")
    st.write("Helping you survive the RFP process without losing your mind.")
    st.link_button("☕ Buy Me a Coffee", "https://www.buymeacoffee.com/yourname")
    st.divider()
    st.info(f"Decoding {len(fed_logic)} federal traps and counting!")

# 5. The Main Interface
st.title("🕵️‍♂️ The Fed-Speak Ultra-Decoder")
st.write("Paste your dry SOW or RFP text below to reveal the hidden truth.")

user_input = st.text_area("Paste Jargon Here:", height=300)

if st.button("Decode the Truth"):
    if user_input:
        decoded = user_input
        matches_found = 0
        
        # The Smart Engine Loop
        for jargon, truth in fed_logic.items():
            pattern = re.compile(re.escape(jargon), re.IGNORECASE)
            if pattern.search(decoded):
                decoded = pattern.sub(f" **[{truth.upper()}]** ", decoded)
                matches_found += 1
            
        st.success(f"Successfully decoded {matches_found} federal mysteries!")
        st.markdown(decoded)
        
        # The "Value Add" at the bottom
        st.divider()
        st.info(random.choice(pro_tips))
    else:
        st.warning("Please paste some text first!")
