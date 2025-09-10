import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Set page configuration
st.set_page_config(
    page_title="महिना कॅल्क्युलेटर",
    page_icon="📅",
    layout="centered"
)

# Title and description
st.title("📅 दिनांक कॅल्क्युलेटर")
st.subheader("महिन्यांच्या आधारे भविष्यातील किंवा मागील तारखा मोजा")

# Create two columns for input
col1, col2 = st.columns(2)

# Get the current date
today = datetime.now().date()

# Column 1: Date selection
with col1:
    st.subheader("प्रारंभ दिनांक निवडा")
    selected_date = st.date_input(
        "वर्तमान दिनांक",
        value=today,
        min_value=datetime(2000, 1, 1).date(),
        max_value=datetime(2050, 12, 31).date()
    )
    
    # Display the selected date in a more readable format
    st.write(f"निवडलेला दिनांक: {selected_date.strftime('%B %d, %Y')}")

# Column 2: Month input
with col2:
    st.subheader("महिने प्रविष्ट करा")
    months_to_add = st.number_input(
        "जोडण्याचे/वजा करण्याचे महिने",
        min_value=-120,
        max_value=120,
        value=0,
        step=1,
        help="महिने जोडण्यासाठी सकारात्मक संख्या किंवा वजा करण्यासाठी नकारात्मक संख्या प्रविष्ट करा"
    )
    
    # Display hint for the user
    if months_to_add > 0:
        st.write(f"{months_to_add} महिने जोडत आहे")
    elif months_to_add < 0:
        st.write(f"{abs(months_to_add)} महिने वजा करत आहे")
    else:
        st.write("गणना करण्यासाठी महिन्यांची संख्या प्रविष्ट करा")

# Calculate button
if st.button("दिनांक मोजा", type="primary"):
    # Calculate the new date by adding/subtracting months
    result_date = selected_date + relativedelta(months=months_to_add)
    
    # Display the result in a highlighted box
    st.success(f"**परिणाम दिनांक:** {result_date.strftime('%B %d, %Y')}")
    
    # Show difference information
    difference_in_days = (result_date - selected_date).days
    
    # Create a detailed result box
    st.info(f"""
    **गणना तपशील:**
    - प्रारंभ दिनांक: {selected_date.strftime('%B %d, %Y')}
    - महिने {' जोडले' if months_to_add >= 0 else ' वजा केले'}: {abs(months_to_add)}
    - परिणाम दिनांक: {result_date.strftime('%B %d, %Y')}
    - एकूण फरक: {abs(difference_in_days)} दिवस
    """)

# Add a separator
st.divider()

# Add some helpful information
with st.expander("ℹ️ हा कॅल्क्युलेटर कसा वापरावा"):
    st.write("""
    1. दिनांक पिकर वापरून आपला प्रारंभ दिनांक निवडा
    2. आपण जोडू इच्छित असलेल्या महिन्यांची संख्या (सकारात्मक संख्या) किंवा वजा करू इच्छित असलेल्या महिन्यांची संख्या (नकारात्मक संख्या) प्रविष्ट करा
    3. परिणाम पाहण्यासाठी 'दिनांक मोजा' बटणावर क्लिक करा
    4. परिणामात मोजलेला दिनांक आणि दिवसांमधील एकूण फरक दाखवला जाईल
    """)

# Footer
st.caption("स्ट्रीमलिट सह तयार केले • दिनांक कॅल्क्युलेटर © 2025")
