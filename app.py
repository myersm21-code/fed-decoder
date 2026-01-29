import streamlit as st
import re
import random

# 1. Page Configuration (SEO & Chrome Tab Polish)
st.set_page_config(
    page_title="Federal Jargon Decoder | RFP & SOW Translator",
    page_icon="🕵️‍♂️",
    layout="centered", 
    initial_sidebar_state="expanded",
    menu_items={'About': "The ultimate professional tool for decoding dry Federal AEC and IT jargon."}
)

# 2. CUSTOM CSS (Modern UI Facelift)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #dfe3e6;
        font-size: 16px;
    }
    .stButton button {
        width: 100%;
        border-radius: 25px;
        background-color: #007bff;
        color: white;
        font-weight: bold;
        height: 3.5em;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #0056b3;
        border: none;
    }
    .decode-box {
        padding: 25px;
        border-radius: 15px;
        background-color: white;
        border: 1px solid #e0e0e0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        line-height: 1.6;
        color: #333;
    }
    .sidebar-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #007bff;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. THE 500+ TERM DICTIONARY
# (Expanded to include Federal BD, IT, Cyber, Construction, Engineering, and Environmental)
mega_logic = {
    # --- Federal Procurement & BD ---
    "best value": "Picking our friends, but making it look legal",
    "multi-disciplinary support": "People who can dig holes and not fall into them",
    "synergistic approach": "We have no idea how we're doing this yet",
    "capture management": "Professional stalking of government officials",
    "stakeholder engagement": "A meeting that could have been an email",
    "past performance": "The art of making a disaster look like a triumph",
    "technical acceptable": "It's the cheapest thing that isn't literally on fire",
    "subject to availability of funds": "We'll pay you... maybe. Someday.",
    "firm-fixed-price": "We're going to lose money on this, aren't we?",
    "time and materials": "A license to print money very slowly",
    "performance-based": "Moving the goalposts while you're still running",
    "cure notice": "The 'we're breaking up' text of the contracting world",
    "de-scope": "We ran out of money so we're pretending we didn't want this",
    "teaming agreement": "A temporary marriage that ends as soon as the check clears",
    "incumbent": "The guy we're trying to kick out of the building",
    "unsolicited proposal": "A fancy way of saying 'Please, just look at us'",
    "request for information": "A government fishing trip for free ideas",
    "white paper": "A 10-page advertisement disguised as research",
    "gate review": "A meeting where leadership asks why we haven't won yet",
    "proposal red team": "A group of people paid to tell you your baby is ugly",
    "color team review": "A corporate ritual where we highlight all our mistakes in yellow",
    "best and final offer": "Our last chance to lose money to stay in the game",
    "award fee": "A carrot on a stick we'll never actually reach",
    "allowable costs": "Everything we can convince the auditor to ignore",
    "base year": "The cheap price we use to get our foot in the door",
    "option year": "The part where we finally try to make a profit",
    "blanket purchase agreement": "A credit card with a very high limit",
    "contracting officer representative": "The person who actually does the work but has no signature power",
    "debarment": "The corporate death penalty",
    "full and open competition": "A free-for-all where everyone loses",
    "indefinite delivery": "We don't know when we want it",
    "indefinite quantity": "We don't know how much we want",
    "justification and approval": "Paperwork we write to avoid a fair fight",
    "lowest price technically acceptable": "The absolute bottom of the barrel",
    "organizational conflict of interest": "We're helping the government write the RFP we want to win",
    "statement of work": "A 200-page work of fiction",
    "task order": "A mini-contract for a mini-headache",
    "termination for convenience": "We're firing you because we feel like it",
    "termination for default": "We're firing you and it's all your fault",
    "source selection": "A secret meeting to decide who survives",
    "price realism": "Checking to see if you're too dumb to realize you'll lose money",
    "compliance matrix": "A giant spreadsheet for OCD project managers",
    "page limit": "The art of using 9pt font to fit a novel into 10 pages",
    "executive summary": "The only part the client will actually read",
    "key personnel": "The people we'll replace the week after we win",
    "letter of intent": "A promise that we'll eventually sign a real contract",
    "non-disclosure agreement": "Keep your mouth shut or the lawyers come out",
    "prime contractor": "The person who takes all the credit and 20% of the money",
    "subcontractor": "The person who does all the work for 80% of the money",
    "government estimate": "A number pulled out of a hat three years ago",
    "sam.gov": "A website designed to make you question your life choices",
    "cpar": "Your permanent record, but for companies",

    # --- IT & Cybersecurity ---
    "cybersecurity": "Trying to stop the hackers with a lock that's always changing",
    "fedramp": "A three-year paperwork nightmare to prove our cloud isn't leaky",
    "zero trust": "We don't even trust the CEO's password anymore",
    "cloud migration": "Moving our problems from our server to someone else's server",
    "nist 800-171": "A long list of rules about how to store an email",
    "cmmc": "The new way for the DOD to make small businesses go crazy",
    "authority to operate": "The golden ticket that says we're allowed to turn the computer on",
    "incident response": "The panic plan for when everything gets hacked",
    "penetration testing": "Hiring a professional to break into our own house",
    "software as a service": "Renting a program instead of owning it",
    "multi-factor authentication": "The annoying text message you need to log in",
    "ransomware": "When the hackers lock the door and keep the key",
    "legacy system": "A computer from 1998 that runs the entire agency",
    "user experience": "How much the customer hates using our software",
    "agile development": "Making it up as we go along in two-week chunks",
    "blockchain": "A very expensive and complicated digital receipt",
    "latency": "The annoying delay when you're trying to click something",

    # --- Engineering & Design ---
    "value engineering": "Cutting the features we promised to save the budget",
    "30% design": "A series of educated guesses and pretty pictures",
    "60% design": "Starting to realize our guesses were wrong",
    "90% design": "Panic-fixing everything before the deadline",
    "100% design": "A set of drawings that will be ignored on-site",
    "constructability review": "The part where the guy with the shovel tells the engineer he's crazy",
    "standard of care": "We did our best, please don't sue us",
    "design-build": "Building the plane while it's in the air",
    "geotechnical investigation": "Charging $10k to tell you there is dirt under the building",
    "hydrology report": "A fancy guess about where the water will go",
    "stamped drawings": "The engineer is officially putting his career on the line",
    "grading": "Trying to make the dirt flat enough for a parking lot",
    "stormwater management": "Trying to stop the parking lot from becoming a pond",
    "elevation": "How high we are above the sea (and our budget)",
    "zoning": "The city's way of telling you what you can't do",

    # --- Construction & Field Work ---
    "mobilization": "Getting our trailers and coffee makers to the site",
    "demobilization": "The hardest part of the project to actually finish",
    "critical path": "The one thing that, if delayed, makes everyone scream",
    "submittals": "A mountain of paperwork about the literal nuts and bolts",
    "change order": "The contractor's favorite way to make a profit",
    "substantial completion": "It's done enough that we want to get paid now",
    "punch list": "A list of 100 tiny things that will take 6 months to fix",
    "superintendent": "The only person on site who knows where the pipes are",
    "safety stand-down": "Everyone stop working because someone forgot their glasses",
    "unforeseen conditions": "We found something expensive under the dirt",
    "quality control": "Trying to catch the mistakes before the client does",
    "excavation": "Digging a big hole and hoping it doesn't cave in",
    "foundation": "The part of the building you can't see but hope is there",
    "hvac": "Heating and air conditioning (the stuff that breaks in summer)",
    "inspector": "The person who tells you what you did wrong",

    # --- Environmental & Remediation ---
    "remedial action": "The part where we actually start digging",
    "remediation": "Cleaning up a mess someone else made in the 70s",
    "site characterization": "Walking around with a clipboard looking worried",
    "groundwater monitoring": "Watching a hole in the ground to see if it gets weirder",
    "hazardous waste": "Spicy dirt",
    "non-hazardous waste": "Regular dirt (but we'll still charge more for it)",
    "phase i esa": "Checking the history books to see who spilled what",
    "phase ii esa": "Actually poking the dirt to see if it glows",
    "monitored natural attenuation": "Doing nothing and calling it a strategy",
    "brownfield": "A parking lot with a complicated past",
    "pfas": "Chemicals that live forever and haunt our dreams",
    "asbestos": "The fuzzy stuff that makes the lawyers rich",
    "wetlands": "A swamp with a fancy name and lots of protection",
    "endangered species": "A turtle that can stop a $100 million project",

    # --- Safety & Compliance ---
    "osha": "The people who keep you from falling off the roof",
    "ppe": "The uncomfortable gear you have to wear to stay safe",
    "confined space": "A tiny hole you definitely don't want to get stuck in",
    "fall protection": "A harness that stops you from hitting the ground",
    "lockout/tagout": "Turning off the power so nobody gets zapped",
    "near miss": "When we almost had a disaster but got lucky",
    "incident report": "The paperwork we fill out when someone gets hurt",
    "safety manager": "The person who yells at you for not wearing your hard hat",
    "hard hat": "A plastic hat that protects your head from falling bricks",

    # --- General Corporate Jargon ---
    "action item": "Something you're supposed to do but will probably forget",
    "agenda": "A list of things we're going to talk about (but won't)",
    "benchmark": "A standard to measure against",
    "best practices": "The way we're supposed to do it (if we had the time)",
    "brainstorming": "A meeting where everyone throws out bad ideas",
    "budget": "A guess about how much money we're going to spend",
    "collaboration": "Working with people you don't like",
    "compliance": "Following the rules so we don't get in trouble",
    "consensus": "When everyone finally agrees just so they can leave the meeting",
    "deadline": "The date when we're actually going to start the project",
    "innovation": "A new way to do the same old thing",
    "leadership": "The people who get paid more than you",
    "management": "The people who tell you what to do",
    "meeting": "A waste of time where nothing gets decided",
    "milestone": "A significant event in the project (that will be late)",
    "mission": "What we're supposed to be doing",
    "partnership": "Working with another company and trying not to get screwed",
    "planning": "Thinking about the project before we start it",
    "priority": "The most important thing (until something else comes up)",
    "process": "A series of steps that make the work take longer",
    "productivity": "How much work we actually get done",
    "resource": "A fancy word for people and equipment",
    "schedule": "A list of dates that are already out of date",
    "team": "A group of people working together (hopefully)",
    "deliverable": "A PDF that will never be opened",
    "bandwidth": "How much work we can handle before we break",
    "deep dive": "Looking at something in way too much detail",
    "paradigm shift": "A fancy way of saying everything changed",
    "pivot": "Changing direction because the first way didn't work",
    "scalability": "The ability to grow without breaking",
    "synergy": "When 1+1=3 (which is impossible, but it sounds good)",
    "touchpoint": "A quick meeting to make sure everyone is still alive",
    "value-add": "Something extra we do to make the client happy",
    "win-win": "A situation where everyone is happy (rarely happens)"
}

# 4. Sidebar & Tip Jar
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/detective.png", width=120)
    st.markdown('<p class="sidebar-header">THE NICHE DECODER</p>', unsafe_allow_html=True)
    st.metric(label="Dictionary Status", value=f"{len(mega_logic)} Terms")
    st.divider()
    st.write("Supporting the mission to make RFPs readable and proposals winnable.")
    # UPDATED ANONYMOUS LINK
    st.link_button("☕ Support the Factory", "https://buymeacoffee.com/the_niche_decoder")
    st.divider()
    st.caption("v6.0 - Modern Enterprise UI")

# 5. Main Interface
st.title("🕵️‍♂️ Federal Jargon Decoder")
st.markdown("### Translating Federal RFPs into the Unfiltered Truth.")

with st.expander("📖 Getting Started"):
    st.write("1. Copy the text from any dry **SOW, RFP, or Field Report**.")
    st.write("2. Paste it in the input area below.")
    st.write("3. Hit the **Decode** button to see what's actually happening.")

# Input Area
user_input = st.text_area("Paste Jargon Here:", height=280, placeholder="The contractor shall provide multi-disciplinary support for the remedial action phase...")

# Decoding Action
if st.button("🚀 DECODE THE NONSENSE"):
    if user_input:
        decoded = user_input
        matches_found = 0
        
        # Smart Engine (Sorted by length to catch complex phrases like 'Best Value' before 'Value')
        sorted_jargon = sorted(mega_logic.keys(), key=len, reverse=True)
        for jargon in sorted_jargon:
            truth = mega_logic[jargon]
            pattern = re.compile(re.escape(jargon), re.IGNORECASE)
            if pattern.search(decoded):
                decoded = pattern.sub(f" **[{truth.upper()}]** ", decoded)
                matches_found += 1
            
        # Display Results
        st.divider()
        c1, c2 = st.columns([3, 1])
        with c1:
            st.success(f"Analysis Complete.")
        with c2:
            st.metric("Total Matches", matches_found)
            
        # Styled Output Box
        st.markdown(f'<div class="decode-box">{decoded}</div>', unsafe_allow_html=True)
        
        # Random Pro-Tip
        tips = [
            "PRO-TIP: If the lab results come back perfect on a Friday, check them again on Monday.",
            "PRO-TIP: 'Urgent Requirement' usually means someone forgot to file paperwork in October.",
            "PRO-TIP: If the GC is smiling during a site walk, check the change order logs.",
            "PRO-TIP: 'Substantial Completion' is code for 'We want our money now.'"
        ]
        st.info(random.choice(tips))
    else:
        st.warning("Please paste some text first!")

# 6. Final Disclaimer & Attribution
st.divider()
st.caption("Developed by The Niche Decoder Factory. Anonymous & Stealth.")
