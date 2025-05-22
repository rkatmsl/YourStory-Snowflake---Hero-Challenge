import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Explore India's Cultural Heritage",
    # layout="wide"
)

with st.sidebar:    
    pages = ["Art Forms", "Cultural Experiences", "World Heritage Sites", "Tourism Insights", "Responsible Tourism"]
    current_page = st.query_params.get("page", "Art Forms")
    if current_page not in pages:
        current_page = "Art Forms"
    
    selected = option_menu(
        "Explore India's",
        pages,
        icons=["brush", "globe", "brush", "bar-chart", "globe"],
        menu_icon="cast",
        default_index=pages.index(current_page),
        styles={
            "container": {"padding": "0!important", "background-color": "#262730"},
            "icon": {"color": "#4da6ff", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#404040",
                "color": "#FFFFFF",
            },
            "nav-link-selected": {"background-color": "#1f77b4"},
            "menu-title": {"color": "#FFFFFF", "font-weight": "600"},
        }
    )

if selected != current_page:
    st.query_params["page"] = selected
    st.rerun()


def extract_global_data():
    data = {
        "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "World ITAs (Million)": [1087.0, 1137.0, 1195.0, 1241.0, 1333.0, 1413.0, 1465.0, 407.0, 458.0, 975.0, 1300.0],
        "India ITAs (Million)": [6.97, 13.11, 13.77, 15.02, 16.81, 17.42, 17.91, 6.33, 7.00, 14.33, 18.89],
        "India Share (%)": [0.64, 1.15, 1.15, 1.21, 1.26, 1.23, 1.22, 1.56, 1.53, 1.47, 1.45],
        "India Receipts (US$ Billion)": [18.4, 20.2, 21.1, 22.9, 27.3, 28.6, 30.1, 13.1, 8.8, 28.2, 32.2]
    }
    return pd.DataFrame(data)

def extract_inbound_data():
    data = {
        "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "FTAs (Million)": [6.97, 7.68, 8.03, 8.80, 10.04, 10.56, 10.93, 2.74, 1.52, 6.44, 9.52],
        "NRIs (Million)": [None, 5.43, 5.74, 6.22, 6.77, 6.87, 6.98, 3.59, 5.48, 7.89, 9.38],
        "ITAs (Million)": [None, 13.11, 13.76, 15.03, 16.81, 17.42, 17.91, 6.33, 7.00, 14.33, 18.89]
    }
    return pd.DataFrame(data)

def extract_top_countries():
    data = {
        "Country": ["Bangladesh", "United States", "United Kingdom", "Australia", "Canada", "Sri Lanka", "Malaysia", "Germany", "Nepal", "France"],
        "FTAs (Lakhs)": [21.20, 16.91, 9.21, 4.56, 3.86, 2.80, 2.62, 2.24, 1.95, 1.89],
        "Share (%)": [22.26, 17.75, 9.67, 4.79, 4.05, 2.94, 2.75, 2.35, 2.05, 1.98]
    }
    return pd.DataFrame(data)

def extract_monthly_ftas_2023():
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "FTAs (Lakhs)": [8.20, 7.95, 8.50, 7.20, 6.80, 6.50, 7.10, 7.30, 7.60, 9.00, 9.50, 11.00]
    }
    return pd.DataFrame(data)

def extract_outbound_data():
    data = {
        "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "INDs (Million)": [16.63, 18.33, 20.38, 21.87, 24.36, 26.30, 26.92, 7.24, 7.16, 21.13, 27.02]
    }
    return pd.DataFrame(data)

def extract_top_destinations():
    data = {
        "Destination": ["United Arab Emirates", "United States", "Thailand", "Saudi Arabia", "Singapore", "United Kingdom", "Malaysia", "Canada", "Australia", "Germany"],
        "INDs (Lakhs)": [26.50, 15.20, 14.80, 13.50, 12.30, 10.10, 9.80, 8.90, 7.60, 6.50]
    }
    return pd.DataFrame(data)

def extract_domestic_data():
    data = {
        "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "DTVs (Million)": [1145.28, 1282.80, 1431.97, 1615.39, 1657.55, 1854.93, 2321.98, 610.22, 677.63, 1731.01, 2509.63]
    }
    return pd.DataFrame(data)

def extract_top_states():
    data = {
        "State": ["Uttar Pradesh", "Tamil Nadu", "Maharashtra", "Karnataka", "Rajasthan", "Madhya Pradesh", "Andhra Pradesh", "Gujarat", "West Bengal", "Telangana"],
        "DTVs (Million)": [478.53, 399.32, 292.45, 227.81, 188.92, 185.63, 155.47, 138.29, 135.82, 108.74],
        "FTVs (Lakhs)": [25.63, 20.14, 15.82, 12.47, 10.95, 8.76, 7.89, 6.54, 5.92, 4.87]
    }
    return pd.DataFrame(data)

def extract_asi_monuments():
    data = {
        "Monument": ["Taj Mahal", "Sun Temple", "Qutub Minar", "Red Fort", "Ellora Caves", "Golkonda Fort", "Agra Fort", "Bibi ka Maqbara", "Charminar", "Shanwarwada"],
        "Domestic Footfall 2023-24 (Lakhs)": [60.99, 31.97, 31.24, 27.94, 17.41, 16.08, 14.10, 12.95, 12.90, 12.61],
        "Foreign Footfall 2023-24 (Lakhs)": [7.52, 0.95, 1.87, 1.63, 0.82, 0.45, 1.21, 0.33, 0.28, 0.19]
    }
    return pd.DataFrame(data)

def extract_economic_data():
    data = {
        "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "FEEs (US$ Billion)": [18.4, 20.2, 21.1, 22.9, 27.3, 28.6, 30.1, 13.1, 8.8, 28.2, 32.2],
        "GDP Contribution (%)": [6.8, 6.9, 7.0, 7.1, 7.3, 7.4, 7.5, 6.0, 5.8, 7.2, 7.6]
    }
    return pd.DataFrame(data)

def extract_regional_data():
    data = {
        "Bloc": ["ASEAN", "BRICS", "EU", "G20", "APEC", "GCC"],
        "FTAs (Lakhs)": [12.34, 8.76, 15.82, 45.67, 30.12, 9.45],
        "INDs (Lakhs)": [45.20, 10.50, 25.30, 80.15, 60.78, 40.12]
    }
    return pd.DataFrame(data)

def generate_global_visual(data):
    st.subheader("India's Share in Global ITAs and Receipts (2013-2023)")
    fig, ax1 = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="Year", y="World ITAs (Million)", data=data, ax=ax1, color="blue", marker="o", label="World ITAs")
    ax1.set_ylabel("World ITAs (Million)", color="blue")
    ax2 = ax1.twinx()
    sns.lineplot(x="Year", y="India Share (%)", data=data, ax=ax2, color="green", marker="o", label="India Share (%)")
    ax2.set_ylabel("India Share (%)", color="green")
    ax1.set_title("Global ITAs and India's Share (2013-2023)")
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Year", y="India Receipts (US$ Billion)", data=data, ax=ax, palette="Blues")
    ax.set_title("India's Tourism Receipts (2013-2023)")
    st.pyplot(fig)

def generate_global_textual(data):
    return """
    ## Global Tourism Scenario
    - **2023 Global ITAs**: 1,300 million, up 33.33% from 2022.
    - **India's ITAs**: 18.89 million, with a 1.45% global share.
    - **Tourism Receipts**: US$32.2 billion in 2023, contributing 2.14% to global receipts.
    - **Trend**: India's share peaked at 1.56% in 2020 due to a global drop, stabilizing at ~1.45% in 2023.
    """

def generate_inbound_visual(data, top_countries, monthly_data):
    st.subheader("Inbound Tourism Trends (2013-2023)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="Year", y="FTAs (Million)", data=data, ax=ax, color="purple", marker="o", label="FTAs")
    sns.lineplot(x="Year", y="NRIs (Million)", data=data, ax=ax, color="orange", marker="o", label="NRIs")
    ax.set_title("FTAs and NRIs in India (2013-2023)")
    st.pyplot(fig)

    st.subheader("Top 10 Source Countries for FTAs (2023)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Country", y="FTAs (Lakhs)", hue="Share (%)", data=top_countries, ax=ax, palette="viridis")
    ax.set_title("Top 10 Source Countries for FTAs (2023)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Monthly FTAs in 2023")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="Month", y="FTAs (Lakhs)", data=monthly_data, ax=ax, color="red", marker="o")
    ax.set_title("Monthly FTAs in 2023")
    st.pyplot(fig)

def generate_inbound_textual(data, top_countries, monthly_data):
    return """
    ## Inbound Tourism
    - **FTAs 2023**: 9.52 million, up 47.90% from 2022.
    - **NRIs 2023**: 9.38 million, contributing to total ITAs of 18.89 million.
    - **Top Source**: Bangladesh (21.20 lakh FTAs, 22.26% share).
    - **Peak Month**: December with 11.00 lakh FTAs.
    - **Other Key Sources**: US (16.91 lakh), UK (9.21 lakh).
    """

def generate_outbound_visual(data, top_destinations):
    st.subheader("Outbound Tourism Trends (2013-2023)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="Year", y="INDs (Million)", data=data, ax=ax, color="teal", marker="o", label="INDs")
    ax.set_title("Indian Nationals' Departures (INDs) (2013-2023)")
    st.pyplot(fig)

    st.subheader("Top 10 Destinations for INDs (2023)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Destination", y="INDs (Lakhs)", data=top_destinations, ax=ax, palette="cool")
    ax.set_title("Top 10 Destinations for INDs (2023)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

def generate_outbound_textual(data, top_destinations):
    return """
    ## Outbound Tourism
    - **INDs 2023**: 27.02 million, up 27.87% from 2022.
    - **Top Destination**: UAE with 26.50 lakh departures.
    - **Other Key Destinations**: US (15.20 lakh), Thailand (14.80 lakh).
    - **Trend**: Sharp recovery post-2021, surpassing pre-pandemic levels.
    """

def generate_domestic_visual(data, top_states, asi_data):
    st.subheader("Domestic Tourist Visits (DTVs) Trends (2013-2023)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="Year", y="DTVs (Million)", data=data, ax=ax, color="orange", marker="o", label="DTVs")
    ax.set_title("Domestic Tourist Visits (DTVs) in India (2013-2023)")
    st.pyplot(fig)

    st.subheader("Top 10 States by DTVs and FTVs (2023)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="State", y="DTVs (Million)", data=top_states, ax=ax, color="skyblue", label="DTVs")
    ax2 = ax.twinx()
    sns.lineplot(x="State", y="FTVs (Lakhs)", data=top_states, ax=ax2, color="red", marker="o", label="FTVs")
    ax.set_title("Top States by DTVs and FTVs (2023)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Top ASI Monuments by Footfall (2023-24)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Monument", y="Domestic Footfall 2023-24 (Lakhs)", data=asi_data, ax=ax, color="green", label="Domestic")
    sns.barplot(x="Monument", y="Foreign Footfall 2023-24 (Lakhs)", data=asi_data, ax=ax, color="blue", label="Foreign")
    ax.set_title("Top ASI Monuments by Footfall (2023-24)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

def generate_domestic_textual(data, top_states, asi_data):
    return """
    ## Domestic Tourism
    - **DTVs 2023**: 2,509.63 million, up 44.98% from 2022.
    - **Top State**: Uttar Pradesh with 478.53 million DTVs and 25.63 lakh FTVs.
    - **Taj Mahal**: 60.99 lakh domestic and 7.52 lakh foreign visitors in 2023-24.
    - **Other Key States**: Tamil Nadu (399.32M DTVs), Maharashtra (292.45M DTVs).
    """

def generate_economic_visual(data):
    st.subheader("Economic Impact Trends (2013-2023)")
    fig, ax1 = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="Year", y="FEEs (US$ Billion)", data=data, ax=ax1, color="gold", marker="o", label="FEEs")
    ax1.set_ylabel("FEEs (US$ Billion)", color="gold")
    ax2 = ax1.twinx()
    sns.lineplot(x="Year", y="GDP Contribution (%)", data=data, ax=ax2, color="purple", marker="o", label="GDP Contribution")
    ax2.set_ylabel("GDP Contribution (%)", color="purple")
    ax1.set_title("Foreign Exchange Earnings and GDP Contribution (2013-2023)")
    st.pyplot(fig)

def generate_economic_textual(data):
    return """
    ## Economic Impact
    - **FEEs 2023**: US$32.2 billion, up 14.18% from 2022.
    - **GDP Contribution**: 7.6% in 2023, up from 7.2% in 2022.
    - **Trend**: Strong recovery post-2021 (US$8.8B), exceeding pre-pandemic levels (US$30.1B in 2019).
    """

def generate_regional_visual(data):
    st.subheader("FTAs and INDs by Regional Blocs (2023)")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Bloc", y="FTAs (Lakhs)", data=data, ax=ax, color="blue", label="FTAs")
    sns.barplot(x="Bloc", y="INDs (Lakhs)", data=data, ax=ax, color="orange", label="INDs")
    ax.set_title("FTAs and INDs by Regional Blocs (2023)")
    st.pyplot(fig)

def generate_regional_textual(data):
    return """
    ## Regional Blocs
    - **G20**: 45.67 lakh FTAs, 80.15 lakh INDs.
    - **APEC**: 30.12 lakh FTAs, 60.78 lakh INDs.
    - **ASEAN**: 12.34 lakh FTAs, 45.20 lakh INDs.
    - **GCC**: 9.45 lakh FTAs, 40.12 lakh INDs.
    """

global_data = extract_global_data()
inbound_data = extract_inbound_data()
top_countries = extract_top_countries()
monthly_ftas = extract_monthly_ftas_2023()
outbound_data = extract_outbound_data()
top_destinations = extract_top_destinations()
domestic_data = extract_domestic_data()
top_states = extract_top_states()
asi_data = extract_asi_monuments()
economic_data = extract_economic_data()
regional_data = extract_regional_data()

# st.title("Explore India's Cultural Heritage")

# page = st.sidebar.selectbox("Choose a Section", ["Art Forms", "Cultural Experiences", "World Heritage Sites", "Tourism Insights", "Responsible Tourism"])

if selected == "Art Forms":
    st.markdown("""
    <style>
    /* Overall page styling */
    .main {
        background-color: #f8f5f0;
        padding: 10px;
    }
    
    /* Header styling */
    .art-header {
        text-align: center;
        margin-bottom: 25px;
        color: #fff;
        border-bottom: 2px solid #8D6E63;
        padding-bottom: 15px;
    }
    
    /* Card styling */
    .art-card {
        border: none;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        background: black;
    }
    
    .art-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    .art-image {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 12px 12px 0 0;
    }
    
    .art-content {
        padding: 20px;
    }
    
    .art-title {
        font-size: 22px;
        font-weight: 600;
        color: #4E342E;
        margin-bottom: 8px;
    }
    
    .art-state {
        display: inline-block;
        background-color: #8D6E63;
        color: #fff;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 14px;
        margin-bottom: 12px;
    }
    
    .art-description {
        color: #fff;
        font-size: 15px;
        line-height: 1.5;
    }
    
    /* Filter styling */
    .filter-container {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }
    
    .filter-title {
        font-weight: 600;
        color: #fff;
        margin-bottom: 0px;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #8D6E63;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #6D4C41;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("Traditional Art Forms of India", divider="rainbow")

    with st.container(border=True):
        st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h3>Explore Traditional Art Forms of India</h3>
            <p>Discover diverse Art Forms across India's states</p>
        </div>
        """, unsafe_allow_html=True)

    art_data = pd.DataFrame({
        'Name': [
            'Phad Painting', 'Punjabi Kissa Art', 'Pahari Painting', 'Mughal Miniature Painting',
            'Mandala Art', 'Mural Painting', 'Tanjore Painting', 'Kalamkari', 'Mysore Painting',
            'Patachitra', 'Pattachitra', 'Madhubani Painting', 'Assamese Scroll Painting',
            'Warli Painting', 'Worli Painting', 'Miniature Painting', 'Christian Art of Goa',
            'Gond Painting', 'Bastar Tribal Art', 'Sohrai Art', 'Naga Tribal Art', 'Manipuri Painting'
        ],
        'State': [
            'Rajasthan', 'Punjab', 'Himachal Pradesh', 'Uttar Pradesh', 'Rajasthan', 'Kerala', 'Tamil Nadu',
            'Andhra Pradesh', 'Karnataka', 'West Bengal', 'Odisha', 'Bihar', 'Assam', 'Gujarat', 'Maharashtra',
            'Rajasthan', 'Goa', 'Madhya Pradesh', 'Chhattisgarh', 'Jharkhand', 'Meghalaya', 'Manipur'
        ],
        'Description': [
            'Epic tales with bold colours and patterns',
            'Folk tales and cultural heritage from Punjab',
            'Delicate brushwork of Himalayan themes',
            'Royal court scenes in Persian style',
            'Spiritual geometric patterns representing the universe',
            'Temple wall art with spiritual themes',
            'Gold-embellished religious paintings',
            'Mythological narratives in natural dyes',
            'Bright paintings with religious themes',
            'Bengali scroll art with elaborate narratives',
            'Odisha’s cloth paintings with myths',
            'Vivid rural and spiritual paintings from Bihar',
            'Tribal scrolls with religious themes',
            'Tribal art of nature in geometric forms',
            'Geometric folk art by Worli tribe',
            'Detailed royal heritage art of Rajasthan',
            'Christian art influenced by Portuguese style',
            'Nature-inspired tribal art with fine detail',
            'Bold tribal expressions of Bastar culture',
            'Harvest-themed tribal wall art',
            'Textiles and carvings with tribal motifs',
            'Spiritual themes in vibrant hues'
        ],
        'Image_URL': [
            'https://cdn.shopify.com/s/files/1/0849/4704/files/Phad_Facebook_Image.jpg',
            'https://upload.wikimedia.org/wikipedia/en/5/52/Punjabi_Shahmukhi_Qissay.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Krishna_and_Radha_looking_into_a_mirror._-_Google_Art_Project.jpg/1280px-Krishna_and_Radha_looking_into_a_mirror._-_Google_Art_Project.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/1/16/Govardhan._Jahangir_Visiting_the_Ascetic_Jadrup._ca._1616-20%2C_Musee_Guimet%2C_Paris.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/9a/Manjuvajramandala_con_43_divinit%C3%A0_-_Unknown_-_Google_Cultural_Institute.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d3/Meister_des_Mah%C3%A2janaka_J%C3%A2taka_001.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/de/Sikh_Gurus_with_Bhai_Bala_and_Bhai_Mardana.jpg',
            'https://upload.wikimedia.org/wikipedia/en/0/0b/Kalamkari_painting_of_Lord_Vishnu.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/5/5d/Mysore_Painting.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/92/Extrait_de_Chandi_Mangal_de_Hazra_Chitrakar_%28Naya_Bengale%29_%281439702942%29.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/7/7d/Odisha_Pattachitara_Depicting_Unconditional_Love_between_Radha_Krushna.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/6/67/Madhubani_Mahavidyas.jpg',
            'https://cdn.shopify.com/s/files/1/1194/1498/files/Interiro_scene__Chitra_Bhagavata__Narowa_Bali_Satra_480x480.png',
            'https://upload.wikimedia.org/wikipedia/commons/9/94/Painted_prayers%2C_Warli_paintings%2C_at_Sanskriti_Kendra%2C_Anandagram%2C_New_Delhi.jpg',
            'https://rukminim1.flixcart.com/image/416/416/jl41nrk0/painting/g/y/e/mm-2192-mad-masters-original-imaf8arxxzbfbuen.jpeg',
            'https://indianfolkart.org/wp-content/uploads/2021/04/rajasthani-painting-Dharmendrayati-88.jpeg',
            'https://upload.wikimedia.org/wikipedia/commons/4/4a/Poster-museumofchristianart.jpg',
            'https://gondart-india.com/wp-content/uploads/2021/04/jangarh_singh_shyam_01-1.png',
            'https://theindiacrafthouse.com/cdn/shop/products/Bastar_20Tribal_20Art_20Tealight_20Holder_20-_20Musicians_20-_20SSB01A_1024x1024@2x.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/9e/Tribal_Art_Gallery.jpg',
            'https://oddessemania.in/wp-content/uploads/2024/07/Art-of-nagaland.jpg',
            'https://dailydesignist.com/cdn/shop/products/17112020012300.png',
        ]
    })

    with st.container():
        st.markdown('<div class="">', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        
        with col1:
            state_filter = st.selectbox(
                "📅 Filter by State", 
                ['All'] + sorted(list(art_data['State'].unique())),
                help="Select a specific state to see festivals during that time"
            )                    

        with col2:
            search_term = st.text_input(
                placeholder="Type to search...", 
                label="🔎 Search by Art Form Name"
            )

        st.markdown('</div>', unsafe_allow_html=True)
    
    if state_filter != 'All':
        filtered_data = art_data[art_data['State'] == state_filter]
    else:
        filtered_data = art_data
    
    if search_term:
        filtered_data = filtered_data[filtered_data['Name'].str.lower().str.contains(search_term.lower())]
    
    # st.markdown(f"<p style='color: #fff; margin-bottom: 20px;'>Showing {len(filtered_data)} art forms</p>", unsafe_allow_html=True)
    st.info(f"📊 Showing {len(filtered_data)} Art Forms.")

    if len(filtered_data) > 0:
        cols = st.columns(2)
        
        for i, (index, row) in enumerate(filtered_data.iterrows()):
            col = cols[i % 2]
            
            with col:
                st.markdown(f"""
                <div class="art-card">
                    <img src="{row['Image_URL']}" class="art-image" alt="{row['Name']}">
                    <div class="art-content">
                        <h3 class="art-title">{row['Name']}</h3>
                        <div class="art-state">{row['State']}</div>
                        <p class="art-description">{row['Description']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 50px; color: #fff;">
            <h3>No art forms found matching your criteria</h3>
            <p>Try adjusting your filters or search term</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add footer
    st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 20px; border-top: 1px solid #D7CCC8; color: #fff;">
        <p>Explore the rich cultural heritage of traditional Indian art forms</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Cultural Experiences":
    st.header("Cultural Experiences", divider="rainbow")

    festival_data = pd.DataFrame({
        'Name': ['Pitr-Paksha- Mahalaya Amavasya', 'Noopuraraavam', 'All India Industrial Exhibition', 'Bhishma Ekadasi', 'Deccan Festival', 'Telugu New Year', 'Ugadi', 'Sri Rama Navami Festival', 'Vinayaka Chaturthi', 'Durga Festival', 'Nagula Chavithi', 'Magh or Bhogali Bihu', 'Dehing Patkai Festival', 'Elephant Festival', 'Pragjyothi International Dance Festival', 'Bohag Bihu', 'Bihu', 'Island Tourism Festival', 'Swami Vivekananda Jayanti', 'Boori Boot', 'Hill Miris Festival', 'Losar', 'Tamladu', 'Oriah', 'Ali-Aye Ligang', 'Nyokum', 'Mopin', 'Pongtu', 'Sanken', 'Moh or Mol', 'Dree', 'Solung', 'Chalo Loku', 'Chhath Puja', 'Rajgir Dance Festival', 'Sonepur Cattle Fair', 'National Tribal art & Food Festival', 'Monsoon Magic Festival', 'Heritage Festival', 'Nariyela Poornima', 'Holika Dahan', 'Delhi Book Fair', 'Taj Mahotsav', 'Garden Tourism Festival', 'Mango Festival', 'Kutch Festival', 'Paragliding Festival', 'Saptak Music Festival', 'Pravasi Bharatiya Divas', 'Vibrant Gujarat Global Summit', 'Uttarayan Kite Festival', 'Modhera Dance Festival', 'Vad Fest', 'Global Bird Watchers Conference', 'Bhavnath Fair', 'Great Indian Heritage Fest', 'Dangs Darbar', 'Kavant Fair', 'Chaitra Navratri', 'Chitra Vichitra Fair', 'Mango Festival', 'Monsoon Festival', 'Tarnetar Fair', 'Bhadrapada Purnima', 'Beach Festival', 'Shamlaji Fair', 'Vautha Fair', 'Sunburn Festival', 'Zatra at Cansaulin', 'Goa Carnival', 'Feast of Sacred Heart of Jesus', 'Sao Joao', 'Feast of Assumption of our Lady', 'Feast of Three Kings', 'Gokulashtami', 'Chovoth', 'Ladainha or Ladin', 'Feast of St Francis Xavier', 'Feast of Immaculate Conception', 'Goa Liberation Day', 'Surajkund Craft Mela', 'Guru Ravidas’s Birthday', 'Shaheedi Diwas of Bhagat Singh, Rajguru & Sukhedev', 'Baisakhi Festival', 'Maharana Pratap Jayanthi', 'Sant Kabir Jayanthi', 'Haryana Heroes Martyrdom Day', 'Maharaja Agrasen Jayanti', 'Haryana Day', 'Shaheed Udham Singh’s Birthday', 'Losar', 'Himachal Day', 'Rakhadumni – Rakhi', 'Leh Sindhu Darshan', 'Kashmir Lavender Festival', '33rd Kalachakra', 'Guru Tse-Chu', 'Vikram Samvat', 'Wanchuk', 'Galdan Namchot', 'Lohri', 'Spitok Gustor Zanskar', 'Spituk Gustor', 'Basant Panchmi', 'Dosmochey Festival', 'Yargon Tungshak', 'Guru Tse-Chu', 'Stok Guru Tsechu', 'Matho Nagrang', 'Nagrang', 'Shab-e-Miraj', 'Yuru Kabgyat', 'Hemis Festival', 'Shachukul Gustor', 'Zanskar Karsha Gustor', 'Phyang Tsedup', 'Korzok Gustor', 'Dak-Thok Tse-Chu', 'Sakti Tse-Chu', 'Naszal', 'Ladakh Festival', 'Navratri', 'Thiksay Gustor', 'Chemrey Angchok', 'Galdan Namchot', 'Losar', 'Makar Sankramana', 'Pattadakal Dance Festival', 'Gudi Padva or Ugadi', 'Naga Panchami', 'Arthunkal Perunnal', 'Sabarimala Makaravilakku', 'Kanjiramattom Nercha', 'Thaipooyam', 'Thaipooya Mahotsavam', 'Machattu Mamangam', 'Adoor Gajamela', 'Kuttikkol Thampuratty Theyyam', 'Uthralikavu Pooram', 'Chettikulangara Bharani', 'Guruvayoor Utsavam', 'Attukal Pongala', 'Parippally Gajamela', 'Thirunakkara Arattu', 'Attuvela Mahotsavam', 'Kodungalloor Bharani', 'Malanada Kettukazhcha', 'Arattupuzha Pooram', 'Nenmara Vallangi Vela', 'Kottiyoor Utsavam', 'Vallarpadam Thirunal', 'Sree Narayana Guru Samadhi', 'Sree Narayana Guru Jayanthi', 'Perumthitta Tharavad Kottamkuzhy', 'Feast at Manarcad', 'Feast at Edathua Church', 'Feast Malayattoor Church', 'Mannarasala Ayilyam', 'Swathi Sangeethotsavam', 'Nishagandhi Festival', 'Ernakulathappan Utsavam', 'Pattambi Nercha', 'Maramon Convention', 'Pariyanampetta Pooram', 'Chittur Kongan Pada', 'Chinakkathoor Pooram', 'Soorya Music Festival', 'Soorya Dance Festival', 'Chembai Sangeetholsavam', 'Kochi Biennale', 'Onam', 'Vishu', 'Thrissur Pooram', 'Nehru Trophy Boat Race', 'Champakulam Boat Race', 'Aranmula Boat Race', 'Payippad Boat Race', 'Neelamperoor Padayani', 'Thripunithura Athachamayam', 'Kalpathi Ratholsavam', 'Vaikathashtami Festival', 'Cochin Carnival', 'Amrithanandamayi Birthday', 'Khajuraho Dance Festival', 'Tejaji Fair', 'Ganesh Chaturthi', 'Nag Panchami', 'Kalidas Festival', 'Chikoo Utsav', 'Bird fest', 'Bob Dylan Festival', 'Ahaia Festival', 'Chavang Kut', 'Chapchar Kut', 'Hornbill Festival', 'Moatsu Festival', 'Savitri Amavasya', 'Mukteswar Dance Festival', 'Sattila Ekadasi', 'Rajarani Music Festival', 'Bhaimi Ekadasi', 'Magha Purnima', 'Puri Beach Festival', 'Kumbha Sankranti', 'Pankoddhar Ekadasi', 'Konark Dance Festival', 'Phagu Dasami', 'Papanasini Ekadasi', 'Dola Purnima', 'Meena Sankranti', 'Papamochani Ekadasi', 'Chaitra Amavasya', 'Rama Navami', 'Kamada Ekadasi', 'Pana Sankranti', 'Baruthini Ekadasi', 'Chandan Yatra', 'Akshaya Tritiya', 'Mohini Ekadasi', 'Jala Krida Ekadasi', 'Brusha Sankranti', 'Sudasha Brata', 'Raja Sankranti', 'Rath Yatra', 'Bada Ekadasi', 'Bahuda Yatra', 'Singha Sankranti', 'Khudurukuni Osha', 'Gamha Purnima', 'Bali Trutiya', 'Kanya Sankranti', 'Rushi Panchami', 'Saraswati Puja', 'Garbhana Sankranti', 'Mahastami', 'Kumarotstaba Purnima', 'Kartik Purnima', 'Bichha Sankranti', 'Awala Navami', 'Konark Festival', 'International Sand Art Festival', 'Prathamastami', 'Manabasa – Gurubar Osha', 'Dhanu Sankranti', 'Muktsar Fair', 'Lohri', 'Pracheen Kala Kendra Nritya and Sangeet Sammelan', 'Baisakhi', 'Guru Parab- Guru Nanak’s Birthday', 'International Yoga Festival', 'Bikaner Camel Festival', 'Jaipur Literature Festival', 'Nagaur Fair', 'Beneshwar Fair', 'Desert Festival', 'Braj Festival', 'Shekhawati Festival', 'Jambheshwar Fair', 'Elephant Festival', 'Gangaur Festival', 'Mewar Spring Festival', 'Rajasthan Day Celebration', 'Mahaveerji Fair', 'Jodhpur Flamenco and Gypsy Festival', 'Summer Festival', 'Urs Fair', 'Teej Festival', 'Kajli Teej Festival', 'Kota Dussehra', 'Marwar Festival', 'Galiyakot Urs', 'Pushkar Camel Fair', 'Kolayat Fair', 'Chandrabhaga Fair', 'Matasya Festival', 'Bundi Utsav', 'Winter Festival', 'Saga Dawa', 'Drupka Tseshi', 'Lakshmi Puja', 'Lhabab Duechen', 'Kagyat Dance', 'Losoong Sikkimese', 'Maghe Sankranti Sanhamole', 'Losar Tibetan', 'International Flower Festival', 'Guru Rimpoche’s Birthday', 'Pang Lhabsol', 'Kambam Festival', 'Chennai Dance Festival', 'Chennai Music Festival', 'Arudra Darisanam', 'Thyagaraja Aradhana', 'Bhogi Pongal', 'Surya Pongal', 'Mattu Pongal', 'Jallikattu Festival', 'Thiruvalluvar day', 'India International Leather Fair', 'Thaipusam', 'Natyanjali Festival', 'Tamil New Year', 'Velankanni Church Festival', 'Mamallapuram Dance Festival', 'Rabindra', 'Kharchi Puja', 'Ker Puja', 'Diwali Festival', 'Magh Mela', 'Uttarayani Mela', 'International Yoga Week', 'Ayurveda Jhansi Mahotsav', 'Kailash Fair', 'Ayudha Puja', 'Nag Nathaiya', 'Deva Mela Ramayan Mela Ayodhya', 'Kumbh Mela', 'Magh Mela', 'Dhrupad Mela', 'Lathmar Holi', 'Sheetala Ashtami', 'Sankat Mochan Music Festival', 'Ganga Dussehras', 'Sri Krishna Janmashtami', 'Ram Leela', 'Matki Leela', 'Ganga Mahotsav', 'Dev Deepavali', 'Kenduli Mela', 'Gangasagar Mela', 'Dover Lane Music Conference', 'Birthday of Netaji Subhash Chandra Bose', 'Vasant Panchami', 'Birthday of Sri Ramakrishna Paramahamsa', 'Bengali Nava Barsha', 'Rabindra Jayanti', 'Durga Puja', 'Nandikar National Theatre Festival', 'Bishnupur'],
        'State': ['Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Assam', 'Assam', 'Assam', 'Assam', 'Assam', 'Assam', 'Andaman and Nicobar', 'Andaman and Nicobar', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Arunachal Pradesh', 'Bihar', 'Bihar', 'Bihar', 'Daman and Diu', 'Daman and Diu', 'Daman and Diu', 'Daman and Diu', 'Dadra and Nagar Haveli', 'Delhi', 'Delhi', 'Delhi', 'Delhi', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Gujarat', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Goa', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Himachal Pradesh', 'Himachal Pradesh', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Jammu and Kashmir', 'Karnataka', 'Karnataka', 'Karnataka', 'Karnataka', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Kerala', 'Madhya Pradesh', 'Madhya Pradesh', 'Maharashtra', 'Maharashtra', 'Maharashtra', 'Maharashtra', 'Maharashtra', 'Meghalaya', 'Meghalaya', 'Manipur', 'Mizoram', 'Nagaland', 'Nagaland', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Odisha', 'Punjab', 'Punjab', 'Punjab', 'Punjab', 'Punjab', 'Puducherry', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Rajasthan', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Sikkim', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tamil Nadu', 'Tripura', 'Tripura', 'Tripura', 'Tripura', 'Uttaranchal', 'Uttaranchal', 'Uttaranchal', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'West Bengal', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown'],
        'Month': ['September/October', 'Varies', 'January/February', 'January/February', 'February/March', 'March/April', 'March/April', 'March/April', 'August/September', 'September/October', 'October/November', 'January', 'January', 'February', 'Varies (Often February)', 'April', 'Varies (Jan, Apr, Oct/Nov)', 'January', 'January', 'February', 'Varies', 'February/March', 'February', 'February/March', 'February/March', 'February', 'April', 'April', 'April', 'Varies', 'July', 'September', 'October/November', 'October/November', 'October', 'November/December', 'Varies', 'August', 'Varies', 'August', 'March', 'August/September or January', 'February', 'February', 'July', 'December-February', 'December/January', 'January', 'January (biennial)', 'January (biennial)', 'January', 'January', 'January (Varies)', 'Varies', 'February/March (Maha Shivaratri)', 'Varies', 'March', 'March (After Holi)', 'March/April', 'March/April', 'June/July', 'July/August', 'August/September', 'September', 'Varies', 'November (Kartik Purnima)', 'November (Kartik Purnima)', 'December', 'January (Epiphany)', 'February/March', 'June', 'June', 'August', 'January', 'August/September', 'August/September', 'Varies', 'December', 'December', 'December', 'February', 'January/February', 'March', 'April', 'May/June', 'June', 'September', 'September/October', 'November', 'December', 'February/March', 'April', 'August', 'June', 'May/June', 'Varies (Past event)', 'Varies (Different Monasteries)', 'March/April', 'Varies', 'December/January', 'January', 'January/February', 'January', 'January/February', 'February', 'Varies', 'Varies (Different Monasteries)', 'February/March', 'February/March', 'February/March', 'Varies (Islamic Calendar)', 'June/July', 'June/July', 'July/August', 'July', 'July/August', 'July/August', 'July/August', 'Varies', 'Varies', 'September', 'September/October', 'October/November', 'November', 'December/January', 'February/March', 'January', 'January/February', 'March/April', 'July/August', 'January', 'January', 'January', 'January/February', 'January/February', 'February/March', 'January/February', 'February/March', 'February/March', 'February/March', 'February/March', 'February/March', 'February/March', 'March/April', 'March/April', 'March/April', 'March/April', 'March/April', 'April', 'May/June', 'September/October', 'September', 'August/September', 'December/January', 'September', 'April/May', 'April (Sunday after Easter)', 'October/November', 'January', 'January', 'January/February', 'February', 'February', 'February/March', 'February/March', 'February/March', 'October (Annual, long running)', 'October (Annual, long running)', 'November (Part of Guruvayur Ekadasi)', 'December-April (Biennial)', 'August/September', 'April', 'April/May', 'August (Second Saturday)', 'June/July', 'August/September (During Onam)', 'August/September (During Onam)', 'August/September', 'August/September (Starts Onam celebrations)', 'November', 'November/December', 'December (Last week)', 'September', 'February', 'August/September', 'August/September', 'July/August', 'November', 'January/February', 'Varies', 'May', 'November (Post-harvest)', 'November', 'March', 'December (1-10)', 'May (First week)', 'May/June', 'January', 'January/February', 'January', 'January/February', 'January/February', 'November', 'February', 'February/March', 'December (1-5)', 'February/March', 'March', 'March', 'March', 'March/April', 'March/April', 'March/April', 'April', 'April', 'April/May', 'April/May', 'May', 'May/June', 'May', 'Varies', 'June', 'June/July', 'July', 'July', 'August', 'August/September', 'August', 'August/September', 'September', 'September', 'January/February (Vasant Panchami)', 'October', 'September/October', 'October', 'November', 'November', 'November', 'December (1-5)', 'December (1-5)', 'November/December', 'November/December (Thursdays in Margasira)', 'December', 'January (Maghi)', 'January', 'Varies (Often March)', 'April', 'October/November (Kartik Purnima)', 'January', 'January', 'January', 'January/February', 'January/February (Magh Purnima)', 'January/February', 'February/March (Before Holi)', 'February', 'Varies (Twice a year)', 'March (Holi)', 'March/April', 'March/April (Coincides with Gangaur)', 'March', 'March/April', 'March (Varies)', 'May/June', 'Varies (Islamic Calendar, Rajab month)', 'July/August', 'August/September', 'September/October', 'October', 'Varies (Islamic Calendar)', 'October/November (Kartik Purnima)', 'November (Kartik Purnima)', 'October/November (Kartik Purnima)', 'November/December', 'November/December', 'December', 'May/June (Tibetan Calendar)', 'July/August (Tibetan Calendar)', 'October/November (Diwali)', 'October/November (Tibetan Calendar)', 'December (Tibetan Calendar)', 'December', 'January', 'February/March', 'May', 'June/July (Tibetan Calendar)', 'August/September', 'May', 'December/January', 'December/January', 'December/January', 'January/February', 'January', 'January', 'January', 'January (During Pongal)', 'January (During Pongal)', 'January/February', 'January/February', 'February/March (Maha Shivaratri)', 'April (Mid-April)', 'August/September', 'December/January', 'May/August', 'July', 'July/August (After Kharchi Puja)', 'October/November', 'January/February', 'January (Makar Sankranti)', 'March (1-7)', 'Varies', 'August/September', 'September/October (Navaratri)', 'October/November', 'October/November (Deva Sharif); Varies (Ramayan Mela)', 'Varies (every 3-12 years)', 'January/February', 'February/March', 'March', 'March/April (After Holi)', 'April', 'May/June', 'August/September', 'September/October', 'August/September', 'October/November', 'October/November (Kartik Purnima)', 'January (Makar Sankranti)', 'January (Makar Sankranti)', 'January', 'January', 'January/February', 'February/March', 'April (Mid-April)', 'May', 'September/October', 'December/January', 'December (Last week)', 'Unknown'],
        'Description': ["Fortnight dedicated to ancestral worship, culminating in Mahalaya Amavasya.", "A classical dance festival.", "Large annual consumer exhibition in Hyderabad.", "Hindu holy day dedicated to Bhishma Pitamaha.", "Showcases arts, crafts, culture, and cuisine of the Deccan region, held in Hyderabad.", "Known as Ugadi, marking the beginning of a new Hindu lunar calendar year for Telugu people.", "Telugu and Kannada New Year.", "Celebrates the birth of Lord Rama.", "Hindu festival celebrating the birth of Lord Ganesha.", "Part of Navaratri/Dussehra, celebrating Goddess Durga.", "Festival dedicated to serpent Gods, observed after Diwali.", "Harvest festival (Bhogali Bihu) with community feasts and bonfires.", "Showcases indigenous culture, adventure sports, and traditions of Assam.", "Celebrates elephants (Kaziranga Elephant Festival promotes conservation).", "A festival showcasing various classical dance forms from India.", "Assamese New Year and spring festival (Rongali Bihu), marked by dance and music.", "General term for three important Assamese festivals: Bohag, Kati, and Magh Bihu.", "A 10-day festival showcasing the culture and traditions of the islands.", "Birth anniversary of Swami Vivekananda, observed as National Youth Day.", "Festival of the Nyishi tribe for a successful harvest and prosperity.", "Cultural festival of the Hill Miri tribe.", "Tibetan New Year, celebrated by Monpa and other Buddhist communities.", "Festival of the Idu-Mishmi tribe, seeking protection from natural calamities.", "Agricultural festival of the Wancho tribe.", "Spring festival of the Mishing tribe, marking the beginning of Ahu paddy cultivation.", "Main festival of the Nishi (Nyishi) tribe, for prosperity and communal harmony.", "Agricultural festival of the Adi (specifically Galo) tribe to drive away evil spirits and ensure prosperity.", "Agricultural festival of the Tutsa tribe.", "Traditional New Year festival of the Khampti and Singhpo tribes, similar to Songkran in Thailand.", "Festival of the Tangsa tribe.", "Agricultural festival of the Apatani tribe, for a bountiful harvest.", "Main socio-religious festival of the Adi tribe, celebrating harvest and prosperity.", "Agricultural festival of the Nocte tribe.", "Ancient Hindu Vedic festival dedicated to the Sun God (Surya) and Chhathi Maiya.", "Classical dance and music festival held in Rajgir.", "Asia's largest cattle fair, held on Kartik Purnima.", "Showcases tribal art, culture, and cuisine.", "Celebrates the monsoon season with cultural events.", "Festival celebrating the rich heritage of Daman and Diu.", "Coconut festival marking the end of monsoon and start of fishing season, similar to Raksha Bandhan Purnima.", "Ritual bonfire on the eve of Holi, symbolizing the victory of good over evil.", "Annual book fair organized by ITPO and FIP.", "A 10-day cultural festival in Agra (near Delhi), showcasing arts, crafts, and culture.", "Showcases a variety of flowers and plants, promoting horticulture.", "Celebrates the king of fruits with numerous varieties on display and sale.", "Rann Utsav, a carnival of music, dance, and natural beauty in the Kutch desert.", "Adventure sports festival, often held in Saputara.", "Annual Indian classical music festival in Ahmedabad.", "Celebrates the contribution of the overseas Indian community.", "Biennial investors' summit held by the Government of Gujarat.", "International Kite Festival marking Makar Sankranti.", "Classical dance festival at the Modhera Sun Temple (Uttarardh Mahotsav).", "Vadodara International Art and Culture Festival.", "Conference for ornithologists and bird enthusiasts.", "Religious fair at the Bhavnath Mahadev temple near Girnar.", "Festival celebrating Indian heritage.", "Annual tribal fair held in the Dangs district before Holi.", "Tribal fair of the Rathva community in Kavant village.", "Nine-day festival dedicated to Goddess Durga, celebrated in spring.", "Tribal fair held near the Sabarmati river, largely by Garasia and Bhil tribes.", "Celebration of the mango season with exhibitions and sales of various mango varieties in Gujarat.", "Celebrations to welcome the monsoon, often in Saputara.", "Major fair known for matchmaking, folk dances, and rural Olympics.", "Large fair at the Ambaji temple during the full moon of Bhadrapada month.", "Cultural and recreational festival held on Gujarat's beaches (e.g., Tithal).", "Religious fair at the Shamlaji temple.", "Animal trading fair, especially for donkeys and camels.", "Large electronic dance music (EDM) festival.", "Three Kings Feast at Cansaulim, a major Christian festival.", "Vibrant pre-Lenten carnival with parades, music, and dancing.", "Christian religious feast.", "Feast of St. John the Baptist, celebrated by jumping into wells and ponds.", "Christian religious feast.", "Celebrated in Reis Magos, Cansaulim, and Chandor.", "Hindu festival celebrating the birth of Lord Krishna.", "Goan name for Ganesh Chaturthi.", "A Goan Christian litany or thanksgiving prayer service.", "Major Christian feast honoring St. Francis Xavier in Old Goa.", "Christian feast celebrated in Panjim and Margao.", "Commemorates the day Goa was liberated from Portuguese rule in 1961.", "International crafts fair showcasing Indian handicrafts and culture.", "Birth anniversary of Guru Ravidas, a mystic poet-saint.", "Martyrdom day of the three freedom fighters.", "Harvest festival, Sikh New Year, and marking the Khalsa's formation.", "Birth anniversary of Maharana Pratap, a Rajput king.", "Birth anniversary of Sant Kabir, a mystic poet and saint.", "Commemorates heroes who sacrificed their lives for the state/country.", "Birth anniversary of Maharaja Agrasen, a legendary king.", "Formation day of Haryana state (November 1, 1966).", "Birth anniversary of Udham Singh, an Indian revolutionary.", "Tibetan New Year, celebrated with traditional music, dance, and rituals.", "Commemorates the creation of Himachal Pradesh as a province (April 15, 1948).", "Raksha Bandhan, a festival celebrating the bond between brothers and sisters.", "Festival promoting national integration and celebrating the Indus River.", "Showcases lavender cultivation and products in Kashmir.", "Major Buddhist initiation ceremony. Specific year's event.", "Buddhist festival in Ladakh dedicated to Guru Padmasambhava, with mask dances.", "Start of the Hindu Vikram Samvat calendar year.", "A Ladakhi festival or personal name, context unclear from list.", "Ladakhi festival commemorating the birth and parinirvana of Je Tsongkhapa.", "Winter harvest festival celebrated with bonfires, marking the end of peak winter.", "Monastic festival at Spituk Monastery, Zanskar, with masked dances.", "Annual monastic festival at Spituk Monastery near Leh, with masked dances.", "Hindu festival dedicated to Goddess Saraswati.", "Ladakhi New Year festival celebrated in Leh, Likir, and Diskit monasteries.", "A local festival in Nubra Valley, Ladakh.", "Buddhist festival in Ladakh dedicated to Guru Padmasambhava, with mask dances.", "Monastic festival at Stok Monastery with masked dances by monks.", "Festival at Matho Monastery, known for oracles and masked dances.", "Part of Matho Nagrang festival.", "Islamic observance of Prophet Muhammad's night journey.", "Monastic festival at Lamayuru Monastery with masked dances.", "Major Buddhist festival in Ladakh at Hemis Monastery, celebrating Guru Padmasambhava.", "Monastic festival at Shachukul Monastery.", "Monastic festival at Karsha Monastery in Zanskar.", "Monastic festival at Phyang Monastery.", "Monastic festival at Korzok Monastery by Tso Moriri lake.", "Monastic festival at Dakthok Monastery.", "Monastic festival in Sakti village.", "Local festival or event in Ladakh.", "Annual festival showcasing Ladakhi culture, folk dances, and traditions.", "Nine-night festival worshipping Goddess Durga.", "Monastic festival at Thiksey Monastery.", "Monastic festival at Chemrey Monastery.", "Ladakhi festival commemorating the birth and parinirvana of Je Tsongkhapa.", "Tibetan New Year, celebrated by Monpa and other Buddhist communities.", "Harvest festival marking the sun's transit into Makara rashi.", "Classical dance festival at the UNESCO World Heritage site of Pattadakal.", "Kannada and Marathi New Year (Ugadi for Kannada).", "Hindu festival dedicated to the worship of snakes.", "Feast of St. Sebastian at Arthunkal Church.", "Annual festival at Sabarimala temple, culminating with Makaravilakku.", "Festival at Kanjiramattom Mosque, commemorating Sheikh Fariduddin.", "Hindu festival dedicated to Lord Murugan.", "Grand celebration of Thaipooyam.", "Horse effigy festival at Machattu Thiruvanikavu Temple.", "Elephant pageant at Adoor Parthasarathy Temple.", "Theyyam festival at Kuttikkol Thampuratty Bhagavathy Temple.", "Temple festival in Wadakkancherry known for its elephant processions.", "Major temple festival at Chettikulangara Devi Temple, known for Kettukazhcha.", "Annual 10-day festival at Guruvayoor Sree Krishna Temple.", "Largest gathering of women for a religious activity, preparing Pongala for Attukal Devi.", "Elephant pageant at Parippally Kodimootil Sree Bhadrakali Temple.", "Temple festival at Thirunakkara Mahadeva Temple, Kottayam.", "Water carnival at Elankavu Sree Bhagavathy Temple, Vaikom.", "Festival at Kodungalloor Bhagavathy Temple, known for unique rituals.", "Temple festival at Poruvazhy Malanada Duryodhana Temple with giant effigies.", "Ancient temple festival, considered the 'mother of all poorams'.", "Spectacular annual festival of Nellikulangara Bhagavathy Temple in Nenmara and Vallangi villages.", "28-day long temple festival at Kottiyoor, in two temples Akkare and Ikkare Kottiyoor.", "Feast at the Basilica of Our Lady of Ransom, Vallarpadam.", "Commemoration of the Samadhi (death anniversary) of Sree Narayana Guru.", "Birth anniversary of Sree Narayana Guru.", "Theyyam festival in Kasaragod district.", "Ettu Nombu Perunnal (8-Day Lent) at St. Mary's Jacobite Syrian Cathedral, Manarcad.", "Feast of St. George at Edathua Church.", "Malayattoor Perunnal, feast at St. Thomas Syro-Malabar Church, Malayattoor.", "Main festival at Mannarasala Sree Nagaraja Temple, dedicated to serpent gods.", "Music festival in Thiruvananthapuram, dedicated to Swathi Thirunal.", "Annual dance and music festival organized by Kerala Tourism in Thiruvananthapuram.", "Annual festival at Ernakulam Shiva Temple.", "Festival at Pattambi Mosque in Palakkad district.", "Largest Christian convention in Asia, held on the banks of Pamba River.", "Temple festival known for Kalamezhuthu Pattu and Pooram.", "Historical festival in Chittur, Palakkad, commemorating a victory.", "Temple festival at Chinakkathoor Bhagavathy Temple, known for its elephant pageant and folk arts.", "Part of the long Soorya Festival, showcasing music performances.", "Part of the Soorya Festival, showcasing dance performances.", "Annual Carnatic music festival in Guruvayur, in honor of Chembai Vaidyanatha Bhagavathar.", "Kochi-Muziris Biennale, an international exhibition of contemporary art.", "Harvest festival of Kerala, state festival, with Pookalam, Onasadya, and Vallamkali.", "Malayalam New Year, celebrated with Vishukkani and fireworks.", "Grand temple festival in Thrissur, known for elephants, percussion, and fireworks.", "Premier snake boat race held in Punnamada Lake, Alappuzha.", "Oldest snake boat race in Kerala, held on Pamba River.", "Traditional snake boat race (Uthrattathi Vallamkali) on Pamba River.", "Three-day water festival and boat race at Payippad lake.", "Ancient ritual art form performed at Neelamperoor Palli Bhagavathy Temple.", "Cultural procession marking the beginning of Onam festivities.", "Chariot festival at Sri Visalakshi Sametha Sri Viswanatha Swamy temple, Kalpathy, Palakkad.", "Major festival at Vaikom Mahadeva Temple.", "New Year celebration in Fort Kochi, ending on Jan 1st.", "Celebration of the birth anniversary of Mata Amrithanandamayi Devi.", "Week-long classical dance festival against the backdrop of Khajuraho temples.", "Fair honoring the folk hero Tejaji, especially in Guna district.", "Grand festival celebrating the birth of Lord Ganesha.", "Festival dedicated to serpent worship.", "Celebrates the poet Kalidas with music, dance, and drama in Nagpur.", "Festival promoting chikoo fruit and local culture in Dahanu-Gholvad.", "Bird watching festival, often in winter months at various sanctuaries.", "Music festival in Shillong celebrating Bob Dylan's birthday.", "Post-harvest festival of the Garo tribe, also part of Wangala.", "Post-harvest festival of Kuki-Chin-Mizo communities.", "Spring festival of Mizoram, after completion of jungle clearing for cultivation.", "Showcases the culture and traditions of all Naga tribes at Kisama Heritage Village.", "Post-sowing festival of the Ao tribe.", "Festival where married women pray for their husbands' long life.", "Classical Odissi dance festival at Mukteswar Temple, Bhubaneswar.", "Hindu holy day, an Ekadashi.", "Classical music festival at Rajarani Temple, Bhubaneswar.", "Hindu holy day, an Ekadashi.", "Full moon day in the month of Magha, considered auspicious.", "Cultural and crafts festival on Puri beach.", "Sun's transition into Aquarius zodiac sign.", "Hindu holy day, an Ekadashi.", "Classical dance festival with the Konark Sun Temple as backdrop.", "Tenth day of the bright fortnight in Phalguna, part of Holi celebrations.", "Hindu holy day, an Ekadashi.", "Full moon day in Phalguna, main day of Holi festival in Odisha.", "Sun's transition into Pisces zodiac sign.", "Hindu holy day, an Ekadashi.", "New moon day in the month of Chaitra.", "Celebrates the birth of Lord Rama.", "Hindu holy day, an Ekadashi.", "Odia New Year, also known as Maha Vishuva Sankranti.", "Hindu holy day, an Ekadashi.", "Sandalwood paste festival for deities, especially Lord Jagannath.", "Auspicious day, marks beginning of Chandan Yatra and Rath Yatra chariot construction.", "Hindu holy day, an Ekadashi.", "Hindu holy day, an Ekadashi.", "Sun's transition into Taurus zodiac sign.", "Ritual observed by Odia women for family well-being when a specific astrological combination occurs.", "Raja Parba, a 3-day festival celebrating womanhood and mother earth.", "Grand chariot festival of Lord Jagannath in Puri.", "Also known as Shayani Ekadasi, marks the beginning of Chaturmas.", "Return journey of the deities during Rath Yatra.", "Sun's transition into Leo zodiac sign.", "Festival where unmarried girls worship Goddess Mangala for their brothers' well-being.", "Full moon day in Shravana, also Raksha Bandhan and Baladeva's birthday.", "Festival observed by women, part of Teej celebrations.", "Sun's transition into Virgo zodiac sign, Vishwakarma Puja observed.", "Day to honor ancient sages, observed after Ganesh Chaturthi.", "Worship of Goddess Saraswati.", "Marks a phase in paddy cultivation, Tula Sankranti.", "Eighth day of Navaratri, a key day of Durga Puja.", "Kumara Purnima, festival where unmarried girls pray for a good husband.", "Full moon in Kartik month, auspicious day, Boita Bandana observed.", "Sun's transition into Scorpio zodiac sign.", "Ninth day of Shukla Paksha in Kartik month, worship of Amla tree.", "Classical dance festival, also refers to the Dance Festival.", "Held alongside Konark Dance Festival at Chandrabhaga beach.", "Festival for the well-being of the firstborn child.", "Worship of Goddess Lakshmi on Thursdays in Margasira month.", "Sun's transition into Sagittarius zodiac sign, start of Dhanu Yatra in Bargarh.", "Maghi Mela in Muktsar, commemorating the 40 Sikh martyrs.", "Winter harvest festival celebrated with bonfires, marking the end of peak winter.", "Classical dance and music conference.", "Harvest festival, Sikh New Year, and marking Khalsa's foundation.", "Celebrates birth anniversary of Guru Nanak Dev Ji.", "Promotes yoga with workshops and demonstrations by experts.", "Festival dedicated to camels, with races, dances, and cultural performances.", "World's largest free literary festival.", "Large annual cattle fair in Nagaur.", "Tribal fair at the confluence of Som, Mahi, and Jakham rivers.", "Held in Jaisalmer, showcasing Rajasthani folk culture and traditions.", "Celebrates Lord Krishna's association with Braj region, in Bharatpur.", "Showcases the art, culture, and heritage of the Shekhawati region.", "Fair of the Bishnoi community, honoring Guru Jambheshwar.", "Celebrates elephants with processions and events in Jaipur.", "Important festival dedicated to Goddess Gauri, celebrated by women.", "Welcomes spring, part of Gangaur celebrations in Udaipur.", "Commemorates the formation of Rajasthan state (March 30).", "Jain fair at Shri Mahaveerji temple.", "Music and dance festival celebrating Rajasthani, Flamenco, and Gypsy traditions.", "Held in Mount Abu, with folk dances, music, and boat races.", "Commemorates death anniversary of Sufi saint Khwaja Moinuddin Chishti in Ajmer.", "Monsoon festival celebrated by women, dedicated to Goddess Parvati.", "Grand Teej celebrations, especially in Bundi.", "Elaborate Dussehra celebrations in Kota.", "Celebrates heroes of Rajasthan through folk music and dance in Jodhpur.", "Urs of Syed Fakhruddin Shaheed in Galiyakot (Dungarpur).", "World-renowned camel and livestock fair with cultural events.", "Religious fair at Kolayat near Bikaner, dedicated to sage Kapil Muni.", "Cattle fair and religious gathering on banks of Chandrabhaga river in Jhalrapatan.", "Celebrates culture and heritage of Alwar region.", "Showcases cultural richness, arts, and crafts of Bundi.", "Held in Mount Abu, featuring cultural programs and traditional sports.", "Most important Buddhist festival, marking Buddha's birth, enlightenment, and parinirvana.", "Celebrates Buddha's first sermon.", "Worship of Goddess Lakshmi during Diwali.", "Marks Buddha's descent from heaven after preaching to his mother.", "Monastic masked dance performed before Losoong.", "Sikkimese New Year (for Bhutias), marking end of harvest season, with Chaam dances.", "Maghe Sankranti, first day of Magh month, celebrated by Nepali Sikkimese.", "Tibetan New Year, celebrated by Tibetan Buddhist communities.", "Showcases diverse flora of Sikkim, especially orchids and rhododendrons.", "Birth anniversary of Guru Padmasambhava (Guru Rimpoche).", "Unique Sikkimese festival worshipping Mount Khangchendzonga.", "Festival at Mariamman temples, especially in Coimbatore region, to appease the goddess for rain.", "Major classical dance festival, part of the Margazhi season.", "World's largest cultural event, featuring Carnatic music, part of Margazhi.", "Hindu festival celebrating cosmic dance of Lord Shiva (Nataraja).", "Annual Carnatic music festival commemorating composer Thyagaraja in Thiruvaiyaru.", "First day of Pongal festival, involves discarding old items.", "Second day of Pongal, dedicated to Sun God, involves cooking Pongal rice.", "Third day of Pongal, dedicated to cattle worship.", "Traditional bull-taming sport.", "Celebrates Tamil poet and philosopher Thiruvalluvar.", "Major trade fair for leather industry in Chennai.", "Hindu festival dedicated to Lord Murugan, involving penance and Kavadi.", "Dance festival dedicated to Lord Nataraja in Chidambaram and other temples.", "Puthandu, the first day of the Tamil traditional calendar.", "Annual feast of Our Lady of Good Health at Velankanni Basilica.", "Classical dance festival against backdrop of ancient Pallava rock sculptures.", "Birth anniversaries of Rabindranath Tagore (May) and Kazi Nazrul Islam (May/August).", "Week-long festival worshipping the fourteen deities of Tripura.", "Traditional tribal festival for community welfare and protection.", "Festival of lights, widely celebrated.", "Annual religious fair during Hindu month of Magh, especially at confluences.", "Fair held on Makar Sankranti, especially in Bageshwar.", "Held in Rishikesh, attracting global yoga enthusiasts.", "Festival promoting Ayurveda, often in Jhansi.", "Fair held at Kailash temple near Agra, dedicated to Lord Shiva.", "Worship of weapons and tools, part of Dussehra.", "Re-enactment of Lord Krishna subduing Kaliya Naag, in Varanasi.", "Deva Mela at shrine of Haji Waris Ali Shah; Ramayan Mela in Ayodhya.", "Largest Hindu pilgrimage, held in rotation at Prayagraj, Haridwar, Ujjain, Nashik.", "Annual religious fair during Hindu month of Magh, especially at confluences.", "Annual music festival dedicated to Dhrupad style, in Varanasi.", "Unique Holi celebration in Barsana and Nandgaon.", "Worship of Goddess Sheetala for protection from diseases.", "Annual classical music and dance festival at Sankat Mochan Temple, Varanasi.", "Celebrates descent of River Ganga to Earth.", "Celebrates birth of Lord Krishna, especially in Mathura-Vrindavan.", "Dramatic enactment of Ramayana, especially famous in Ramnagar (Varanasi).", "Part of Janmashtami celebrations, re-enacting Krishna's childhood pranks.", "Festival in Varanasi celebrating River Ganga, with cultural events.", "Festival of lights of the Gods in Varanasi, 15 days after Diwali.", "Fair in Kenduli (Birbhum), associated with poet Jayadeva and Baul music.", "Large pilgrimage fair at Sagar Island.", "Major Indian classical music festival in Kolkata.", "Parakram Divas, birth anniversary of the freedom fighter.", "Saraswati Puja, worship of Goddess Saraswati.", "Birth anniversary of the 19th-century mystic.", "Poila Boishakh, the Bengali New Year.", "Birth anniversary of Rabindranath Tagore.", "Most important festival, celebrating Goddess Durga's victory.", "Major theatre festival organized by Nandikar group in Kolkata.", "Showcases music, dance, and terracotta crafts of Bishnupur."]
    })

    with st.container(border=True):
        st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h3>Explore India's Rich Cultural Festivals</h3>
            <p>Discover diverse festivals across India's states and throughout the year</p>
        </div>
        """, unsafe_allow_html=True)
    
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        month_filter = st.selectbox(
            "📅 Filter by Month", 
            ['All'] + sorted(list(festival_data['Month'].unique())),
            help="Select a specific month to see festivals during that time"
        )
    
    with filter_col2:
        state_filter = st.selectbox(
            "🗺️ Filter by State", 
            ['All'] + sorted(list(festival_data['State'].unique())),
            help="Select a specific state to see local festivals"
        )
    
    filtered_data = festival_data.copy()
    
    if month_filter != 'All':
        filtered_data = filtered_data[filtered_data['Month'] == month_filter]
    
    if state_filter != 'All':
        filtered_data = filtered_data[filtered_data['State'] == state_filter]
    
    if len(filtered_data) == 1:
        st.info(f"📊 Showing {len(filtered_data)} Festival.")
    else:
        st.info(f"📊 Showing {len(filtered_data)} Festivals.")
    
    # with button_col:
    #     if month_filter != 'All' or state_filter != 'All':
    #         if st.button("Reset Filters", type="primary", use_container_width=True):
    #             month_filter = 'All'
    #             state_filter = 'All'
    #             filtered_data = festival_data.copy()
    
    st.write("")
    
    if not filtered_data.empty:
        st.dataframe(
            filtered_data,
            column_config={
                "Name": st.column_config.TextColumn("Festival Name"),
                "State": st.column_config.TextColumn("State/UT"),
                "Month": st.column_config.TextColumn("Month of Celebration"),
                "Description": st.column_config.TextColumn("About the Festival")
            },
            use_container_width=True,
            hide_index=True,
            height=450
        )
        
        st.write("")
        with st.expander("📊 Festival Distribution Visualization"):
            viz_tab1, viz_tab2 = st.tabs(["By State", "By Month"])
            
            with viz_tab1:
                state_counts = filtered_data['State'].value_counts().reset_index()
                state_counts.columns = ['State', 'Count']
                
                if len(state_counts) > 0:
                    st.bar_chart(state_counts, x='State', y='Count', use_container_width=True)
                else:
                    st.write("No data available for visualization")
            
            with viz_tab2:
                def month_sort_key(month_name):
                    month_order = {
                        'January': 1, 'February': 2, 'March': 3, 'April': 4,
                        'May': 5, 'June': 6, 'July': 7, 'August': 8,
                        'September': 9, 'October': 10, 'November': 11, 'December': 12
                    }
                    
                    if '/' in month_name:
                        first_month = month_name.split('/')[0]
                        if first_month in month_order:
                            return month_order[first_month]
                    
                    if month_name in month_order:
                        return month_order[month_name]
                    
                    for key in month_order:
                        if month_name.startswith(key):
                            return month_order[key]
                    
                    return 13
                
                month_data = filtered_data['Month'].copy()
                month_counts = month_data.value_counts().reset_index()
                month_counts.columns = ['Month', 'Count']
                
                month_counts['Sort_Key'] = month_counts['Month'].apply(month_sort_key)
                month_counts = month_counts.sort_values('Sort_Key').drop('Sort_Key', axis=1)
                
                if len(month_counts) > 0:
                    st.bar_chart(month_counts, x='Month', y='Count', use_container_width=True)
                else:
                    st.write("No data available for visualization")
    else:
        st.warning("No festivals match your selected filters. Try different criteria.")
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; font-size: 0.85rem; color: #888;">
        <p>💡 <b>Tip:</b> You can sort the table by clicking on column headers or use the search box to find specific festivals.</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "World Heritage Sites":
    st.markdown("""
    <style>
    /* Overall page styling */
    .main {
        background-color: #f8f5f0;
        padding: 10px;
    }
    
    /* Header styling */
    .art-header {
        text-align: center;
        margin-bottom: 25px;
        color: #fff;
        border-bottom: 2px solid #8D6E63;
        padding-bottom: 15px;
    }
    
    /* Card styling */
    .art-card {
        border: none;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        background: black;
    }
    
    .art-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    .art-image {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 12px 12px 0 0;
    }
    
    .art-content {
        padding: 20px;
    }
    
    .art-title {
        font-size: 22px;
        font-weight: 600;
        color: #4E342E;
        margin-bottom: 8px;
    }
    
    .art-state {
        display: inline-block;
        background-color: #8D6E63;
        color: #fff;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 14px;
        margin-bottom: 12px;
    }
    
    .art-description {
        color: #fff;
        font-size: 15px;
        line-height: 1.5;
    }
    
    /* Filter styling */
    .filter-container {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }
    
    .filter-title {
        font-weight: 600;
        color: #fff;
        margin-bottom: 0px;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #8D6E63;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #6D4C41;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header("UNESCO listed World Heritage sites of India", divider="rainbow")

    with st.container(border=True):
        st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h3>Explore UNESCO listed World Heritage sites of India</h3>
            <p>Discover diverse sites India's states</p>
        </div>
        """, unsafe_allow_html=True)

    heritage_data = pd.DataFrame({
        'Name': [
            'Ajanta Caves', 'Ellora Caves', 'Agra Fort', 'Taj Mahal', 'Sun Temple, Konark', 
            'Group of Monuments at Mahabalipuram', 'Kaziranga National Park', 'Manas Wildlife Sanctuary', 
            'Keoladeo National Park', 'Churches and Convents of Goa', 'Khajuraho Group of Monuments', 
            'Group of Monuments at Hampi', 'Fatehpur Sikri', 'Group of Monuments at Pattadakal', 
            'Elephanta Caves', 'Great Living Chola Temples', 'Sundarbans National Park', 
            'Nanda Devi and Valley of Flowers National Parks', 'Buddhist Monuments at Sanchi', 
            'Humayun\'s Tomb, Delhi', 'Qutb Minar and its Monuments, Delhi', 'Mountain Railways of India', 
            'Mahabodhi Temple Complex at Bodh Gaya', 'Rock Shelters of Bhimbetka', 
            'Chhatrapati Shivaji Terminus', 'Champaner-Pavagadh Archaeological Park', 'Red Fort Complex', 
            'The Jantar Mantar, Jaipur', 'Western Ghats', 'Hill Forts of Rajasthan', 
            'Rani-ki-Vav (the Queen\'s Stepwell) at Patan, Gujarat', 
            'Great Himalayan National Park Conservation Area', 
            'Archaeological Site of Nalanda Mahavihara at Nalanda, Bihar', 'Khangchendzonga National Park', 
            'The Architectural Work of Le Corbusier', 'Historic City of Ahmadabad', 
            'Victorian Gothic and Art Deco Ensembles of Mumbai', 'Jaipur City, Rajasthan', 
            'Kakatiya Rudreshwara (Ramappa) Temple, Telangana', 'Dholavira: a Harappan City', 
            'Santiniketan', 'Sacred Ensembles of the Hoysalas', 'Moidams – the Mound-Burial system of the Ahom Dynasty', 
            'Temples at Bishnupur, West Bengal', 'Mattancherry Palace, Ernakulam, Kerala', 
            'Group of Monuments at Mandu, Madhya Pradesh', 'Ancient Buddhist Site, Sarnath, Varanasi, Uttar Pradesh', 
            'Sri Harimandir Sahib, Amritsar, Punjab', 'River Island of Majuli in midstream of Brahmaputra River in Assam', 
            'Namdapha National Park', 'Wild Ass Sanctuary, Little Rann of Kutch', 'Neora Valley National Park', 
            'Desert National Park', 'Silk Road Sites in India', 
            'The Qutb Shahi Monuments of Hyderabad Golconda Fort, Qutb Shahi Tombs, Charminar', 
            'Mughal Gardens in Kashmir', 'Delhi - A Heritage City', 'Monuments and Forts of the Deccan Sultanate', 
            'Cellular Jail, Andaman Islands', 'Iconic Saree Weaving Clusters of India', 
            'Apatani Cultural Landscape', 'Sri Ranganathaswamy Temple, Srirangam', 
            'Monuments of Srirangapatna Island Town', 'Chilika Lake', 'Padmanabhapuram Palace', 
            'Sites of Satyagrah, India\'s non-violent freedom movement', 'Thembang Fortified Village', 
            'Narcondam Island', 'Ekamra Kshetra – The Temple City, Bhubaneswar', 
            'The Neolithic Settlement of Burzahom', 'Archaeological remains of a Harappa Port-Town, Lothal', 
            'Mountain Railways of India (Extension)', 'Chettinad, Village Clusters of the Tamil Merchants', 
            'Bahá\'í House of Worship at New Delhi', 
            'Evolution of Temple Architecture – Aihole-Badami-Pattadakal', 
            'Cold Desert Cultural Landscape of India', 
            'Sites along the Uttarapath, Badshahi Sadak, Sadak-e-Azam, Grand Trunk Road', 
            'Keibul Lamjao Conservation Area', 'Garo Hills Conservation Area (GHCA)', 
            'The historic ensemble of Orchha', 'Iconic Riverfront of the Historic City of Varanasi', 
            'Temples of Kanchipuram', 'Hire Benakal, Megalithic Site', 
            'Bhedaghat-Lametaghat in Narmada Valley', 'Satpura Tiger Reserve', 
            'Serial Nomination of Maratha Military Architecture in Maharashtra', 
            'Geoglyphs of Konkan Region of India', 
            'Jingkieng jri: Living Root Bridge Cultural Landscapes', 
            'Sri Veerabhadra Temple and Monolithic Bull (Nandi), Lepakshi', 
            'Sun Temple, Modhera and its adjoining monuments', 
            'Rock-cut Sculptures and Reliefs of the Unakoti, Unakoti Range, Unakoti District', 
            'Vadnagar – A multi-layered Historic town, Gujarat', 
            'Serial nomination of Coastal Fortifications along the Konkan Coast, Maharashtra', 
            'The Gond monuments of Ramnagar, Mandla', 'The Bhojeshwar Mahadev Temple, Bhojpur', 
            'Rock Art Sites of the Chambal Valley', 'Khooni Bhandara, Burhanpur', 'Gwalior Fort, Madhya Pradesh', 
            'The historic ensemble of Dhamnar', 'Kanger Valley National Park', 'Mudumal Megalithic Menhirs', 
            'Serial nomination for Ashokan Edict sites along the Mauryan Routes', 
            'Serial nomination of Chausath Yogini Temples', 'Serial nomination of Gupta Temples in North India', 
            'The Palace-Fortresses of the Bundelas'
        ],
        'State': [
            'Maharashtra', 'Maharashtra', 'Uttar Pradesh', 'Uttar Pradesh', 'Odisha', 'Tamil Nadu', 'Assam', 
            'Assam', 'Rajasthan', 'Goa', 'Madhya Pradesh', 'Karnataka', 'Uttar Pradesh', 'Karnataka', 
            'Maharashtra', 'Tamil Nadu', 'West Bengal', 'Uttarakhand', 'Madhya Pradesh', 'Delhi', 'Delhi', 
            'West Bengal, Tamil Nadu, Himachal Pradesh', 'Bihar', 'Madhya Pradesh', 'Maharashtra', 'Gujarat', 
            'Delhi', 'Rajasthan', 'Maharashtra, Karnataka, Kerala, Tamil Nadu', 'Rajasthan', 'Gujarat', 
            'Himachal Pradesh', 'Bihar', 'Sikkim', 'Chandigarh', 'Gujarat', 'Maharashtra', 'Rajasthan', 
            'Telangana', 'Gujarat', 'West Bengal', 'Karnataka', 'Assam', 'West Bengal', 'Kerala', 
            'Madhya Pradesh', 'Uttar Pradesh', 'Punjab', 'Assam', 'Arunachal Pradesh', 'Gujarat', 
            'West Bengal', 'Rajasthan', 'Bihar, Jammu and Kashmir, Maharashtra, Puducherry, Punjab, Tamil Nadu, Uttar Pradesh', 
            'Telangana', 'Jammu and Kashmir', 'Delhi', 'Karnataka, Telangana', 'Andaman and Nicobar Islands', 
            'Madhya Pradesh, Uttar Pradesh, Maharashtra, Andhra Pradesh, Assam', 'Arunachal Pradesh', 
            'Tamil Nadu', 'Karnataka', 'Odisha', 'Tamil Nadu', 'several sites', 'Arunachal Pradesh', 
            'Andaman and Nicobar Islands', 'Odisha', 'Jammu and Kashmir', 'Gujarat', 'Maharashtra, Himachal Pradesh', 
            'Tamil Nadu', 'Delhi', 'Karnataka', 'Ladakh, Himachal Pradesh', 'several sites', 'Manipur', 
            'Meghalaya', 'Madhya Pradesh', 'Uttar Pradesh', 'Tamil Nadu', 'Karnataka', 'Madhya Pradesh', 
            'Madhya Pradesh', 'Maharashtra', 'Maharashtra, Goa', 'Meghalaya', 'Andhra Pradesh', 'Gujarat', 
            'Tripura', 'Gujarat', 'Maharashtra', 'Madhya Pradesh', 'Madhya Pradesh', 'Madhya Pradesh', 
            'Madhya Pradesh', 'Madhya Pradesh', 'Madhya Pradesh', 'Chhattisgarh', 'Telangana', 
            'Andhra Pradesh, Bihar, Delhi, Gujarat, Karnataka, Madhya Pradesh, Uttar Pradesh', 
            'Madhya Pradesh, Odisha, Tamil Nadu, Uttar Pradesh', 'Dashavatara Temple, Deogarh', 
            'Madhya Pradesh and Uttar Pradesh'
        ],
        'Description': [
            'Buddhist caves with 2nd-6th century art, influencing India and Java.',
            '34 temples and monasteries from 7th-11th centuries, showing religious tolerance.',
            '16th-century Mughal fortress with Indo-Islamic architecture.',
            'Indo-Islamic mausoleum built 1631-1648 for Mumtaz Mahal.',
            '13th-century Hindu temple in Kalinga style, depicting Surya’s chariot.',
            '7th-8th century Pallava monuments, influential in Southeast Asia.',
            'Wildlife sanctuary with Indian rhinoceros, tigers, and migratory birds.',
            'Biodiversity hotspot with endangered species, listed as endangered 1992-2011.',
            'Man-made wetland for migratory and resident birds, including Siberian crane.',
            '16th-17th century churches in Gothic and Baroque styles, influencing Asia.',
            '10th-11th century Hindu and Jain temples with Nagara-style carvings.',
            'Vijayanagara Empire capital with Dravidian and Indo-Islamic monuments.',
            'Mughal capital under Akbar with Jama Masjid and Buland Darwaza.',
            '7th-8th century Chalukya temples blending northern and southern styles.',
            '5th-6th century Shiva caves with colossal stone carvings.',
            '11th-12th century Chola temples, prime examples of Dravidian architecture.',
            'World’s largest mangrove forest with Bengal tigers and dolphins.',
            'Himalayan parks with high-altitude habitats and endangered species.',
            'Buddhist sanctuary from 3rd century BCE, pivotal in spreading Buddhism.',
            '1560s Mughal garden tomb, a precursor to the Taj Mahal.',
            '13th-14th century Delhi Sultanate monuments, including Qutb Minar.',
            'Late 19th-early 20th century mountain railways, still operational.',
            '5th-6th century Buddhist temple where Buddha attained enlightenment.',
            'Mesolithic to historical rock paintings in Vindhya Range.',
            'Late 19th century Victorian Gothic train station in Mumbai.',
            'Chalcolithic to 16th century remains, including Hindu and Jain temples.',
            'Mid-17th century Mughal fort, zenith of Indo-Persian architecture.',
            'Early 18th century astronomical observatory with 20 instruments.',
            'Biodiversity hotspot with montane forests and endangered species.',
            'Six Rajput forts from 8th-18th centuries, blending styles.',
            '11th century stepwell with seven levels of carvings.',
            'Himalayan park with diverse forests and endangered species.',
            '5th-13th century Buddhist university with influential architecture.',
            'Sacred Tibetan Buddhist mountain with diverse habitats.',
            'Le Corbusier’s Chandigarh Capitol Complex, a Modernist masterpiece.',
            '15th century Gujarat Sultanate capital with unique urban fabric.',
            '19th-20th century Victorian Gothic and Art Deco buildings in Mumbai.',
            '18th century grid-planned city with Hawa Mahal and Jantar Mantar.',
            '13th century Kakatiya temple with intricate stone carvings.',
            'Bronze Age Harappan city with advanced urban planning.',
            '19th century ashram and university town linked to Rabindranath Tagore.',
            '12th-14th century Hoysala temples with detailed stone sculptures.',
            'Ahom dynasty burial mounds reflecting Tai-Ahom spiritual beliefs.',
            '17th century terracotta temples with sloping roofs.',
            '16th century Portuguese-built palace with carved ceilings.',
            '11th-16th century monuments, including rock-cut tombs and palaces.',
            'Buddhist temples and stupas from 3rd century BCE to 12th century CE.',
            'Sikh spiritual center with floral-decorated architecture.',
            'River island with satras, centers for cultural and dispute resolution.',
            'Eastern Himalayan wilderness with diverse forests.',
            'Salt marsh with Indian wild ass and bird nesting areas.',
            'Virgin forest biodiversity hotspot with red panda.',
            'Thar Desert park with endemic species and Jurassic fossils.',
            '12 Silk Road sites linked to Buddhism and Greco-Buddhist culture.',
            '16th-17th century Qutb Shahi monuments, including Golconda Fort.',
            'Persian-inspired Mughal gardens with Charbagh layout.',
            'Delhi’s historic cities from 1060, including Shahjahanabad.',
            '14th-17th century Deccan sultanate monuments blending styles.',
            '1906 British-built panopticon jail for political prisoners.',
            'Eight sari weaving clusters with unique vernacular architecture.',
            'Apatani cultural landscape with sustainable wet rice cultivation.',
            'World’s largest Hindu temple town with 21 gopurams.',
            '12th-19th century monuments blending Hindu, Islamic, and British styles.',
            'Brackish lagoon with Irrawaddy dolphins and rich fish species.',
            '16th-19th century timber palace with murals and carvings.',
            '22 sites linked to Gandhi’s nonviolent independence movement.',
            'Pre-12th century Monpa dzong village in the Eastern Himalayas.',
            'Volcanic island with Narcondam hornbill and endemic species.',
            'Temple city with 700 temples from 3rd century BCE to 15th century CE.',
            'Neolithic site showing societal evolution from 4th-2nd millennium BCE.',
            'Bronze Age Harappan port-town with trade links to Mesopotamia.',
            'Extension of mountain railways, including Matheran Hill Railway.',
            '19th-20th century Tamil merchant villages with Art Deco houses.',
            '1986 Lotus Temple, a Baháʼí worship site with lotus-shaped design.',
            '6th-8th century Chalukya temples showing temple architecture evolution.',
            'Himalayan cultural landscape with Buddhist monasteries.',
            'Ancient trade road with historical sites from Maurya Empire.',
            'Loktak Lake with phumdi ecosystems and endangered sangai deer.',
            'Garo Hills with sustainable agriculture and diverse wildlife.',
            '16th-17th century Bundela fort and palaces with mixed styles.',
            'Holy city with over 80 ghats along the Ganges for rituals.',
            '6th-9th century Pallava temples marking architectural shift.',
            'Iron Age megalithic dolmens with Mesolithic rock paintings.',
            'Marble canyon with dinosaur fossils in Narmada Valley.',
            'Tiger habitat with endangered plants, linking Western Ghats and Himalayas.',
            '14 Maratha forts from 17th century, built for defense.',
            'Mesolithic to 2nd millennium BCE geoglyphs on Konkan coast.',
            'Khasi living root bridges reflecting harmony with nature.',
            'Vijayanagara temple with 14th-16th century frescoes and monolithic bull.',
            '11th century Māru-Gurjara Sun temple with shrine and reservoir.',
            '8th-9th century Shaivite rock-cut sculptures with folk influences.',
            'Town occupied since 750 BCE with Indo-Greek trade links.',
            'Nine coastal forts along the Konkan coast.',
            'Gond dynasty forts, palaces, and temples with local styles.',
            '11th century unfinished Shiva temple with massive lingam.',
            'Mesolithic rock art depicting prehistoric life and rituals.',
            '16th century Mughal underground water management system.',
            '8th century fort with palaces, temples, and blue ceramic tiles.',
            '5th-7th century Buddhist rock-cut caves and Hindu temple.',
            'Untouched forest with diverse wildlife and geological features.',
            '3500–4000-year-old menhirs aligned with celestial events.',
            '35 Mauryan rock and pillar edicts from Ashoka’s reign.',
            '13 temples with 64 yogini statues, dedicated to female yoga practitioners.',
            '20 Gupta dynasty temples from North India.',
            'Six Bundelkhand fortresses with Rajput and Mughal styles.'
        ],
        'Image_URL': [
            'https://upload.wikimedia.org/wikipedia/commons/a/a4/Cave_26%2C_Ajanta.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/8/88/Kailasa_temple_overview%2C_Ellora.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/7/71/Uttar-Pradesh-Agra-Agra-Fort-Jahangiri-mahal-Apr-2004-00.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/6/60/The_Taj_Mahal_main_building.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/4/47/Konarka_Temple.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/7/74/Shore_Temple_-Mamallapuram_-Tamil_Nadu_-N-TN-C55.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/fe/Beauty_of_Kaziranga_National_Park.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/8/81/Herd_of_Elephant_in_Manas.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/95/Bar-headed_Geese-_Bharatpur_I_IMG_8335.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/1/1b/Basilika_Bom_Jesus.jpeg',
            'https://upload.wikimedia.org/wikipedia/commons/9/92/Lakshmana_Temple_24.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/b2/The_elegant_stone_chariot.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/b5/Fatehput_Sikiri_Buland_Darwaza_gate_2010.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/03/Pattadakal_000.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/9/96/Trimurti%2C_Cave_No._1%2C_Elephanta_Caves_-_1.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/7/77/Le_temple_de_Brihadishwara_%28Tanjore%2C_Inde%29_%2814354574611%29.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/23/Sundarban_Tiger.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/21/%28A%29_Valley_of_flowers%2C_Garhwal_Uttarakhand_India.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/b0/Sanchi1_N-MP-220.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/6/6d/Humayun%27s_tomb_by_Shagil_Kannur_4.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d9/Qutab_Minar_mausoleum.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d8/KSR_Train_on_a_big_bridge_05-02-12_71.jpeg',
            'https://upload.wikimedia.org/wikipedia/commons/4/4e/Mahabodhitemple.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/91/Rock_Shelter_8%2C_Bhimbetka_02.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/4/4d/Chhatrapati_shivaji_terminus%2C_esterno_01.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/20/Jama_masjid_in_Champaner.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/2/2a/Delhi_fort.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/2a/Yantramandir01.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/8/8e/Pampadumshola.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/1/1b/Amber_Fort_%28%E0%A4%86%E0%A4%AE%E0%A5%87%E0%A4%B0_%E0%A4%95%E0%A4%BE_%E0%A4%95%E0%A4%BF%E0%A4%B2%E0%A4%BE_%29.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/a/a5/Rani_ki_vav_02.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/dd/Himalayn_National_Park_01.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/dd/Temple_No.-_3%2C_Nalanda_Archaeological_Site.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/fb/Abhishek532_SamitiReflections.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/1/1a/Palace_of_Assembly_Chandigarh_2006.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/93/Teen_Darwaza.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/5/54/Mumbai_03-2016_40_Bombay_High_Court.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/b4/20191218_Pa%C5%82ac_Wiatr%C3%B3w_w_Jaipurze_1129_9124.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/8/84/Ramappa_Temple_02.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/5/53/Dholavira-1.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/09/Santiniketan_Prayer_Hall.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/bd/Le_temple_de_Chennakesava_%28Somanathapura%2C_Inde%29_%2814465165685%29.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d9/Charaideo_Maidam_of_Ahom_Kings_at_Charaideo_in_Sivasagar%2C_Assam_4.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/0c/Jor_Bangla_Temple_Arnab_Dutta_2011.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/2/2b/Kerala_Dutch_Palace1.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/8/89/Jahaz_Mahal_10.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d9/Ancient_Buddhist_monasteries_near_Dhamekh_Stupa_Monument_Site%2C_Sarnath.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/9f/Amritsar_Golden_Temple_3.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/6/68/Majuli_Island.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/23/Forest_snow_Namdapha_IMG_3373_04.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/e/e5/Wild_ass_india.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/4/41/The_mystic_forest.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/3/3a/A_view_on_Sams_sand_dunes.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/b/b3/VikramshilaRuins.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/08/Qutb_Shahi_Tomb_5.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d6/Shalimar_Bagh_1.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/f2/Jama_Masjid%2CDelhi%2CIndia_05.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/b6/Gateway_to_Bidar_fort.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d0/Cellular_Jail%2C_Andaman_and_Nicobar.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/d/df/Styles_of_Sari.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/1/1e/A_cross_section_of_luch_green_valley_of_Ziro.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/99/Ranganathaswamy_temple_tiruchirappalli.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/8/8c/Gumbaz-_Srirangapatna-Karnataka-DSC_1533.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/90/Chilika_Bhubaneswar.me.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/de/Padmanabhapuram_Palace_1.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/9a/GANDHI_ASHRAM_03.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/b0/Northern_gate_of_Thembang_fort.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/ff/Narcondam_Hornbill_DSCN1242_15.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/0b/Lingaraj_Temple_Complex.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/f6/Horned_figure_on_pottery._Pr%C3%A9-Indus_civilization._Kashmir.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/0b/Lingaraj_Temple_Complex.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/f6/Horned_figure_on_pottery._Pr%C3%A9-Indus_civilization._Kashmir.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/6/63/Chettinad_palatial_house.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/fc/LotusDelhi.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/2d/Durga_Temple.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/f5/Kee_monastery_Spiti_Valley_%28edited%29.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/7/74/Ambala-Kos_Minar.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/0a/Loktak_Lake%2CManipur%2CIndia_01.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/3/38/GARO_TRADITIONAL_DRESS-9.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/5/5b/OrchhaPalace.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/04/Ahilya_Ghat_by_the_Ganges%2C_Varanasi.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/c/c2/Parameswara_Vinnagaram.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/e/e5/Pre-historic_tombs-1.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/6/62/Marble_Rocks_-_Jabalpur.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/4/4e/Amazing_Landscape_%40Satpura_Tiger_Reserve.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/b9/Raigad_fort_towers.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/3/3d/Usgalimal.PNG',
            'https://upload.wikimedia.org/wikipedia/commons/5/51/Living_root_bridges%2C_Nongriat_village%2C_Meghalaya2.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/0/0a/Front_side_of_Veerabhadra_Temple%2C_Lepakshi.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/7/73/Surya_mandhir.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/b/be/Unakotiswara_Kal_Bhairava%2CUnakoti_%28_%E0%A6%8A%E0%A6%A8%E0%A6%95%E0%A7%8B%E0%A6%9F%E0%A6%BF%29.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/9/98/Vadnagar%27s_Kirti_Toran_full_shot_with_beautiful_clouds.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/9/9f/Bastions_of_vijaydurg.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/27/Moti_Mahal_Mandla.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d7/Shiva_Temple%2C_Bhojpur_01.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/9/9c/Rock_Art_Sites_of_the_Chambal_Valley.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/8/82/Khooni_bhandara.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/1/15/Gwalior_Fort_front.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/c/c5/Buddist_sculpture_caves.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/c/c0/Kanger_valley11.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/3/3d/Usgalimal.PNG',
            'https://upload.wikimedia.org/wikipedia/commons/4/4d/Ashoka_Lauriya_Areraj_inscription.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/c/ce/Chausath_Yogini_Temple%2C_Mitaoli%2C_Morena_006.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/6/65/Deogarh01.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/e/ef/View_of_Raja_Mahal_from_Jahangir_Mahal_with_Ram_Raja_Temple_and_Chaturbhuj_Temple_in_the_background%2C_Tikamgarh.jpg'
        ]
    })

    with st.container():
        st.markdown('<div class="">', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 3])
        
        with col1:
            state_filter = st.selectbox(
                "📅 Filter by State", 
                ['All'] + sorted(list(heritage_data['State'].unique())),
                help="Select a specific state to see sites of that state."
            )                    

        with col2:
            search_term = st.text_input(
                placeholder="Type to search...", 
                label="🔎 Search by Site Name"
            )

        st.markdown('</div>', unsafe_allow_html=True)
    
    if state_filter != 'All':
        filtered_data = heritage_data[heritage_data['State'] == state_filter]
    else:
        filtered_data = heritage_data
    
    if search_term:
        filtered_data = filtered_data[filtered_data['Name'].str.lower().str.contains(search_term.lower())]
    
    st.info(f"📊 Showing {len(filtered_data)} Heritage Sites.")

    if len(filtered_data) > 0:
        cols = st.columns(2)
        
        for i, (index, row) in enumerate(filtered_data.iterrows()):
            col = cols[i % 2]
            
            with col:
                st.markdown(f"""
                <div class="art-card">
                    <img src="{row['Image_URL']}" class="art-image" alt="{row['Name']}">
                    <div class="art-content">
                        <h3 class="art-title">{row['Name']}</h3>
                        <div class="art-state">{row['State']}</div>
                        <p class="art-description">{row['Description']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 50px; color: #fff;">
            <h3>No heritage sites found matching your criteria</h3>
            <p>Try adjusting your filters or search term</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add footer
    st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 20px; border-top: 1px solid #D7CCC8; color: #fff;">
        <p>Explore the UNESCO listed World Heritage Sites</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Tourism Insights":
    st.header("Tourism Insights", divider="rainbow")

    section = st.selectbox("", [
        "Global Tourism Scenario",
        "Inbound Tourism",
        "Outbound Tourism",
        "Domestic Tourism",
        "Economic Impact",
        "Regional Blocs"
    ])
    st.write(f"Explore {section} through visuals or text:")
    option = st.radio("Select an option:", ("Visual Insights (Graphs & Charts)", "Textual Insights"))

    if section == "Global Tourism Scenario":
        if option == "Visual Insights (Graphs & Charts)":
            generate_global_visual(global_data)
        else:
            st.markdown(generate_global_textual(global_data))
    elif section == "Inbound Tourism":
        if option == "Visual Insights (Graphs & Charts)":
            generate_inbound_visual(inbound_data, top_countries, monthly_ftas)
        else:
            st.markdown(generate_inbound_textual(inbound_data, top_countries, monthly_ftas))
    elif section == "Outbound Tourism":
        if option == "Visual Insights (Graphs & Charts)":
            generate_outbound_visual(outbound_data, top_destinations)
        else:
            st.markdown(generate_outbound_textual(outbound_data, top_destinations))
    elif section == "Domestic Tourism":
        if option == "Visual Insights (Graphs & Charts)":
            generate_domestic_visual(domestic_data, top_states, asi_data)
        else:
            st.markdown(generate_domestic_textual(domestic_data, top_states, asi_data))
    elif section == "Economic Impact":
        if option == "Visual Insights (Graphs & Charts)":
            generate_economic_visual(economic_data)
        else:
            st.markdown(generate_economic_textual(economic_data))
    elif section == "Regional Blocs":
        if option == "Visual Insights (Graphs & Charts)":
            generate_regional_visual(regional_data)
        else:
            st.markdown(generate_regional_textual(regional_data))

elif selected == "Responsible Tourism":
    st.header("Responsible Tourism", divider="rainbow")

    st.write("""
    Responsible tourism is about making better places for people to live in and better places for people 
    to visit. By following these guidelines, you can ensure your travels have a positive impact on local 
    communities and environments.
    """)
    
    # Create tabs for different categories
    tab1, tab2, tab3 = st.tabs(["Economic Impact", "Environmental Awareness", "Socio-cultural Respect"])
    
    with tab1:
        st.subheader("Supporting Local Economies")
        
        economic_guidelines = [
            {"Title": "Support Local Businesses", "Description": "Buy handicrafts and products from local artisans and markets to support community livelihoods."},
            {"Title": "Fair Prices", "Description": "Pay fair prices for goods and services rather than aggressively bargaining for the lowest price possible."},
            {"Title": "Local Accommodations", "Description": "Stay in locally-owned hotels, guesthouses or homestays rather than international chains when possible."},
            {"Title": "Local Guides", "Description": "Hire local guides who know the area best and help distribute tourism income to local communities."},
            {"Title": "Avoid All-Inclusive Packages", "Description": "Choose tourism options that allow spending to reach local businesses instead of being captured by international companies."}
        ]
        
        for guideline in economic_guidelines:
            st.markdown(f"**{guideline['Title']}**")
            st.write(guideline['Description'])
            st.divider()
    
    with tab2:
        st.subheader("Environmental Responsibility")
        
        environmental_guidelines = [
            {"Title": "Minimize Waste", "Description": "Avoid single-use plastics and carry reusable items such as water bottles, bags, and utensils."},
            {"Title": "Conserve Water", "Description": "Take shorter showers, reuse towels, and be mindful of water usage in water-scarce destinations."},
            {"Title": "Reduce Carbon Footprint", "Description": "Use public transportation, walk, cycle, or share rides when possible. Consider carbon offsetting for flights."},
            {"Title": "Wildlife Protection", "Description": "Never purchase products made from endangered species or participate in activities that exploit animals."},
            {"Title": "Stay on Trails", "Description": "When hiking, stick to marked paths to minimize erosion and impact on natural habitats."},
            {"Title": "Leave No Trace", "Description": "Pack out all trash and leave natural areas as you found them or better."}
        ]
        
        for guideline in environmental_guidelines:
            st.markdown(f"**{guideline['Title']}**")
            st.write(guideline['Description'])
            st.divider()
    
    with tab3:
        st.subheader("Cultural Awareness")
        
        cultural_guidelines = [
            {"Title": "Research Local Customs", "Description": "Learn about local traditions, taboos, and appropriate behavior before your trip."},
            {"Title": "Dress Respectfully", "Description": "Follow local dress codes, especially when visiting religious or cultural sites."},
            {"Title": "Ask Before Photographing", "Description": "Always get permission before taking photos of people, especially in indigenous communities."},
            {"Title": "Learn Basic Phrases", "Description": "Learn a few words in the local language - even simple greetings are appreciated."},
            {"Title": "Respect Sacred Sites", "Description": "Follow all rules at religious and cultural monuments and sacred natural areas."},
            {"Title": "Be Mindful of Your Impact", "Description": "Consider how your presence affects everyday life for local residents."}
        ]
        
        for guideline in cultural_guidelines:
            st.markdown(f"**{guideline['Title']}**")
            st.write(guideline['Description'])
            st.divider()
    
    # Add a personal pledge section
    st.subheader("Make Your Commitment")
    st.write("Select the responsible tourism practices you commit to following:")
    
    # Create columns for checkboxes
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Economic Commitments:**")
        ec1 = st.checkbox("I will buy locally-made products")
        ec2 = st.checkbox("I will use local guides and services")
        ec3 = st.checkbox("I will pay fair prices")
        
        st.write("**Environmental Commitments:**")
        en1 = st.checkbox("I will minimize my waste")
        en2 = st.checkbox("I will conserve water and energy")
        en3 = st.checkbox("I will respect wildlife and natural areas")
    
    with col2:
        st.write("**Cultural Commitments:**")
        cc1 = st.checkbox("I will learn about local customs")
        cc2 = st.checkbox("I will dress appropriately")
        cc3 = st.checkbox("I will ask before taking photographs")
        
        st.write("**General Commitments:**")
        gc1 = st.checkbox("I will share my responsible tourism knowledge")
        gc2 = st.checkbox("I will leave places better than I found them")
    
    # Calculate commitment score
    commitments = [ec1, ec2, ec3, en1, en2, en3, cc1, cc2, cc3, gc1, gc2]
    commitment_count = sum(commitments)
    
    if commitment_count > 0:
        st.progress(commitment_count/len(commitments))
        if commitment_count == len(commitments):
            st.success("You're a Responsible Tourism Champion! Thank you for your complete commitment.")
        elif commitment_count > len(commitments)/2:
            st.info(f"Great start! You've committed to {commitment_count} out of {len(commitments)} practices.")
        else:
            st.warning(f"You've committed to {commitment_count} practices. Can you add a few more?")
    
