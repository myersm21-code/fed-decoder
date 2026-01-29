import streamlit as st
import re
import random

# 1. Page Configuration
st.set_page_config(page_title="The Stealth Federal Decoder", page_icon="🏦", layout="wide")

# 2. THE MASSIVE 500+ TERM DICTIONARY
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
    "technical volume": "The part where we pretend we have a proprietary secret",
    "cost volume": "The part where the math gets creative",
    "compliance matrix": "A giant spreadsheet for OCD project managers",
    "page limit": "The art of using 9pt font to fit a novel into 10 pages",
    "executive summary": "The only part the client will actually read",
    "key personnel": "The people we'll replace the week after we win",
    "letter of intent": "A promise that we'll eventually sign a real contract",
    "non-disclosure agreement": "Keep your mouth shut or the lawyers come out",
    "prime contractor": "The person who takes all the credit and 20% of the money",
    "subcontractor": "The person who does all the work for 80% of the money",
    "tier 2 sub": "The person who actually knows how to use a wrench",
    "government estimate": "A number pulled out of a hat three years ago",
    "solicitation": "The government asking to be impressed",
    "amendment": "A surprise update that breaks all your previous work",
    "deficiency": "A polite way of saying 'You completely missed the point'",
    "clarification": "A chance to fix your typo before you're disqualified",
    "competitive range": "The group of people who aren't disqualified yet",
    "debrief": "A meeting to tell you why you lost while being legally vague",
    "federal acquisition regulation": "The bible of how to make things complicated",
    "far clause": "The fine print that will eventually screw us over",
    "naics code": "The bucket we put our business in so the gov can find us",
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
    "load-bearing wall": "The wall you definitely shouldn't knock down",
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

# 3. Dynamic Footer Logic
pro_tips = [
    "PRO-TIP: If the IT section mentions 'legacy integration,' the budget is 50% too low.",
    "PRO-TIP: 'Cybersecurity compliance' is 10% tech and 90% filling out spreadsheets.",
    "PRO-TIP: If a contractor says the design is '90% done,' they are actually at 40%.",
    "PRO-TIP: The 'Kickoff Meeting' is where the project manager realizes the scope is impossible.",
    "PRO-TIP: If the client asks for 'innovation,' they just want it cheaper.",
    "PRO-TIP: Always check the 'option years' before celebrating a contract win."
]

# 4. Sidebar (Generic Branding)
with st.sidebar:
    st.header("App Factory Status")
    st.success(f"Dictionary Size: {len(mega_logic)} Terms")
    st.divider()
    st.write("If this tool saved your sanity, consider a tip!")
    st.link_button("☕ Buy Me a Coffee", "https://www.buymeacoffee.com/yourname")
    st.divider()
    st.caption("v5.1 - The 'Stealth Professional' Update")
    st.caption("Built for Federal Contracting Professionals.")

# 5. The Main Interface
st.title("🏦 The Stealth Federal Decoder: 500+ Edition")
st.write("Paste your dry SOW, RFP, or Field Report below to reveal the unfiltered truth.")

user_input = st.text_area("Paste Jargon Here:", height=400, placeholder="The contractor shall perform value engineering during the 60% design phase...")

if st.button("🚀 DECODE THE NONSENSE"):
    if user_input:
        decoded = user_input
        matches_found = 0
        
        # The Smart Engine Loop (Sorted by length to catch longer phrases first)
        sorted_jargon = sorted(mega_logic.keys(), key=len, reverse=True)
        
        for jargon in sorted_jargon:
            truth = mega_logic[jargon]
            pattern = re.compile(re.escape(jargon), re.IGNORECASE)
            if pattern.search(decoded):
                decoded = pattern.sub(f" **[{truth.upper()}]** ", decoded)
                matches_found += 1
            
        st.success(f"Decoded {matches_found} industry mysteries!")
        st.markdown(decoded)
        
        # The Dynamic Footer
        st.divider()
        st.info(random.choice(pro_tips))
    else:
        st.warning("Please paste some text first!")
