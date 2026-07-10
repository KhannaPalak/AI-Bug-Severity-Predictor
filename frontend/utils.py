import streamlit as st


def show_severity(severity):

    if severity == "Blocker":
        st.error("🚨 BLOCKER\n\nCritical system failure requiring immediate attention.")

    elif severity == "Critical":
        st.error("🔴 CRITICAL\n\nImmediate action required.")

    elif severity == "Major":
        st.warning("🟠 MAJOR\n\nHigh priority bug affecting core functionality.")

    elif severity == "Minor":
        st.success("🟢 MINOR\n\nLow priority issue with limited impact.")

    elif severity == "Trivial":
        st.info("🔵 TRIVIAL\n\nCosmetic or very low-impact issue.")

    else:
        st.info(severity)


def get_recommendation(severity):

    recommendations = {
        "Blocker": """🚨 Recommendation

Assign immediately to the development team.

Priority: VERY HIGH

Estimated Response: Immediate
""",
        "Critical": """🔴 Recommendation

Investigate and fix as soon as possible.

Priority: HIGH

Estimated Response: Within 24 Hours
""",
        "Major": """🟠 Recommendation

Schedule for the next development sprint.

Priority: MEDIUM

Estimated Response: 2–3 Days
""",
        "Minor": """🟢 Recommendation

Resolve during routine maintenance.

Priority: LOW

Estimated Response: Next Release
""",
        "Trivial": """🔵 Recommendation

Fix whenever convenient.

Priority: VERY LOW

Estimated Response: Future Update
""",
    }

    return recommendations.get(severity, "No recommendation available.")
