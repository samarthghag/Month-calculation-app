import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Initialize session state for language preference if it doesn't exist
if 'language' not in st.session_state:
    st.session_state.language = 'marathi'  # Default language

# Language translations dictionary
translations = {
    'english': {
        'page_title': "Month Calculator",
        'title': "📅 Date Calculator",
        'subtitle': "Calculate future or past dates based on months",
        'lang_button': "मराठी भाषेत बदला (Switch to Marathi)",
        'start_date_header': "Select Start Date",
        'current_date_label': "Current date",
        'selected_date_text': "Selected date: ",
        'months_header': "Enter Months",
        'months_input_label': "Number of months to add/subtract",
        'months_help': "Enter a positive number to add months or a negative number to subtract months",
        'adding_months': "Adding {} month(s)",
        'subtracting_months': "Subtracting {} month(s)",
        'enter_months': "Enter the number of months to calculate",
        'calculate_button': "Calculate Date",
        'result_date': "Result Date:",
        'calculation_details': "Calculation Details:",
        'start_date': "Start date:",
        'months_added': "added",
        'months_subtracted': "subtracted",
        'months_text': "Months",
        'result_date_label': "Result date:",
        'total_difference': "Total difference:",
        'days': "days",
        'how_to_use': "ℹ️ How to use this calculator",
        'how_to_use_content': """
    1. Select your starting date using the date picker
    2. Enter the number of months you want to add (positive number) or subtract (negative number)
    3. Click the 'Calculate Date' button to see the result
    4. The result will show the calculated date and the total difference in days
    """,
        'footer': "Created with Streamlit • Date Calculator © 2025"
    },
    'marathi': {
        'page_title': "महिना कॅल्क्युलेटर",
        'title': "📅 दिनांक कॅल्क्युलेटर",
        'subtitle': "महिन्यांच्या आधारे भविष्यातील किंवा मागील तारखा मोजा",
        'lang_button': "Switch to English (इंग्रजी भाषेत बदला)",
        'start_date_header': "प्रारंभ दिनांक निवडा",
        'current_date_label': "वर्तमान दिनांक",
        'selected_date_text': "निवडलेला दिनांक: ",
        'months_header': "महिने प्रविष्ट करा",
        'months_input_label': "जोडण्याचे/वजा करण्याचे महिने",
        'months_help': "महिने जोडण्यासाठी सकारात्मक संख्या किंवा वजा करण्यासाठी नकारात्मक संख्या प्रविष्ट करा",
        'adding_months': "{} महिने जोडत आहे",
        'subtracting_months': "{} महिने वजा करत आहे",
        'enter_months': "गणना करण्यासाठी महिन्यांची संख्या प्रविष्ट करा",
        'calculate_button': "दिनांक मोजा",
        'result_date': "परिणाम दिनांक:",
        'calculation_details': "गणना तपशील:",
        'start_date': "प्रारंभ दिनांक:",
        'months_added': "जोडले",
        'months_subtracted': "वजा केले",
        'months_text': "महिने",
        'result_date_label': "परिणाम दिनांक:",
        'total_difference': "एकूण फरक:",
        'days': "दिवस",
        'how_to_use': "ℹ️ हा कॅल्क्युलेटर कसा वापरावा",
        'how_to_use_content': """
    1. दिनांक पिकर वापरून आपला प्रारंभ दिनांक निवडा
    2. आपण जोडू इच्छित असलेल्या महिन्यांची संख्या (सकारात्मक संख्या) किंवा वजा करू इच्छित असलेल्या महिन्यांची संख्या (नकारात्मक संख्या) प्रविष्ट करा
    3. परिणाम पाहण्यासाठी 'दिनांक मोजा' बटणावर क्लिक करा
    4. परिणामात मोजलेला दिनांक आणि दिवसांमधील एकूण फरक दाखवला जाईल
    """,
        'footer': "स्ट्रीमलिट सह तयार केले • दिनांक कॅल्क्युलेटर © 2025"
    }
}

# Function to toggle language
def toggle_language():
    if st.session_state.language == 'english':
        st.session_state.language = 'marathi'
    else:
        st.session_state.language = 'english'
    
# Get current language settings
current_lang = translations[st.session_state.language]

# Set page configuration
st.set_page_config(
    page_title=current_lang['page_title'],
    page_icon="📅",
    layout="centered"
)

# Add language toggle button in the sidebar
st.sidebar.button(
    current_lang['lang_button'],
    on_click=toggle_language,
    use_container_width=True
)

# Title and description
st.title(current_lang['title'])
st.subheader(current_lang['subtitle'])

# Create two columns for input
col1, col2 = st.columns(2)

# Get the current date
today = datetime.now().date()

# Add custom CSS to format the date input as dd/mm/yyyy
st.markdown("""
<style>
    /* Target the date input */
    .stDateInput input {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Column 1: Date selection
with col1:
    st.subheader(current_lang['start_date_header'])
    selected_date = st.date_input(
        current_lang['current_date_label'],
        value=today,
        min_value=datetime(2000, 1, 1).date(),
        max_value=datetime(2050, 12, 31).date(),
        format="DD/MM/YYYY"  # Set format to dd/mm/yyyy
    )
    
    # Display the selected date in dd/mm/yyyy format
    st.write(f"{current_lang['selected_date_text']} {selected_date.strftime('%d/%m/%Y')}")

# Column 2: Month input
with col2:
    st.subheader(current_lang['months_header'])
    months_to_add = st.number_input(
        current_lang['months_input_label'],
        min_value=-120,
        max_value=120,
        value=0,
        step=1,
        help=current_lang['months_help']
    )
    
    # Display hint for the user
    if months_to_add > 0:
        st.write(current_lang['adding_months'].format(months_to_add))
    elif months_to_add < 0:
        st.write(current_lang['subtracting_months'].format(abs(months_to_add)))
    else:
        st.write(current_lang['enter_months'])

# Calculate button
if st.button(current_lang['calculate_button'], type="primary"):
    # Calculate the new date by adding/subtracting months
    result_date = selected_date + relativedelta(months=months_to_add)
    
    # Display the result in a highlighted box with dd/mm/yyyy format
    st.success(f"**{current_lang['result_date']}** {result_date.strftime('%d/%m/%Y')}")
    
    # Show difference information
    difference_in_days = (result_date - selected_date).days
    
    # Create a detailed result box with dd/mm/yyyy format
    st.info(f"""
    **{current_lang['calculation_details']}**
    - {current_lang['start_date']} {selected_date.strftime('%d/%m/%Y')}
    - {current_lang['months_text']} {' ' + current_lang['months_added'] if months_to_add >= 0 else ' ' + current_lang['months_subtracted']}: {abs(months_to_add)}
    - {current_lang['result_date_label']} {result_date.strftime('%d/%m/%Y')}
    - {current_lang['total_difference']} {abs(difference_in_days)} {current_lang['days']}
    """)

# Add a separator
st.divider()

# Add some helpful information
with st.expander(current_lang['how_to_use']):
    st.write(current_lang['how_to_use_content'])

# Footer
st.caption(current_lang['footer'])
