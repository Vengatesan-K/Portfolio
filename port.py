import streamlit as st
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.keyboard_text import key
from streamlit_extras.add_vertical_space import add_vertical_space
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from streamlit_extras.mention import mention
from streamlit_extras.colored_header import colored_header

st.set_page_config(page_title='portfolio',
                   page_icon = "💼", 
                   layout="wide")
def style_metric_cards(
    background_color: str = "#FFF",
    border_size_px: int = 1,
    border_color: str = "#CCC",
    border_radius_px: int = 5,
    border_left_color: str = "#9AD8E1",
    box_shadow: bool = True,
):

    box_shadow_str = (
        "box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;"
        if box_shadow
        else "box-shadow: none !important;"
    )
    st.markdown(
        f"""
        <style>
            div[data-testid="metric-container"] {{
                background-color: {background_color};
                border: {border_size_px}px solid {border_color};
                padding: 5% 5% 5% 10%;
                border-radius: {border_radius_px}px;
                border-left: 0.5rem solid {border_left_color} !important;
                {box_shadow_str}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


col1,col2 = st.columns([3,7])
with col1:
#####################
# Header 
 st.write('''
    # Vengatesan K
    ##### *Enthusiastic Data Scientist* 
    ''')
 col3,col4 = st.columns([7,3])

 with col3:
  image = Image.open('fc.png')
  st.image(image, width=150)
 

 add_vertical_space(1)
 from streamlit_extras.word_importances import format_word_importances

 text = (
    "Location  Chennai, Tamilnadu"
 )
 html = format_word_importances(
    words=text.split(),
    importances=(0.7, 0.2, 0.2),  # fmt: skip
 )
 st.write(html, unsafe_allow_html=True)
 add_vertical_space(2)

 text = (
    "Phone  +919488311463, 9790596563"
 )

 html = format_word_importances(
    words=text.split(),
    importances=(0.70, 0.2, 0.3),  # fmt: skip
 )
 st.write(html, unsafe_allow_html=True)
 add_vertical_space(2)
 
 text = (
    "📧 kannanvenkatesh772@gmail.com"
 )

 html = format_word_importances(
    words=text.split(),
    importances=(0.7, 0.3),  # fmt: skip
 )
 st.write(html, unsafe_allow_html=True)

 headerColor = 'green'
 rowEvenColor = 'lightgrey'
 rowOddColor = 'white'

 fig = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>Skills</b>','<b>Languages/Libraries</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=[
      ['Programming','Data Processing','Data Visualization', 'Machine learning','Model deployment'],
      ['Python , R','SQL, Pandas & Numpy','Matplotlib, Plotly','Sci-kit learn & Keras','Streamlit']],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
    align = ['left', 'center'],
    font = dict(color = 'black', size = 10)
    ))
])
 fig.update_layout(width=300, height=400)
 st.plotly_chart(fig)
 
 data = {'Position': ['Site engineer', 'Junior Site engineer'],
        'Start Year': [2019, 2018],
        'End Year': [2022, 2019]}
 df = pd.DataFrame(data)

 df['Years'] = df['End Year'] - df['Start Year']
 colors = px.colors.qualitative.Plotly[:len(df)]

 fig1 = px.bar(df, x='Position', y='Years', title='Work Experience in Years',color='Position', color_discrete_sequence=colors)
 fig1.update_layout(showlegend=False)
 st.plotly_chart(fig1,use_container_width=True) 
 add_vertical_space(15)
 custom_colors = px.colors.sequential.Jet
 data1 = {'Labels': ['Python', 'SQL', 'MongoDB', 'Plotly','Streamlit'],
        'Keys': [4, 3, 2, 3,2]}
 df1 = pd.DataFrame(data1)
 fig2 = px.pie(df1, values='Keys', names='Labels', title='Tools and Libraries Used for this project :',color_discrete_sequence=custom_colors)
 fig2.update_traces(textinfo='none')
 fig2.update_layout(width=300, height=300)
 st.plotly_chart(fig2,use_container_width=True) 
 
 add_vertical_space(20)
 
 data2 = {'Labels': ['Python', 'SQL', 'Plotly','Matplotlib','Streamlit'],
        'Keys': [4, 4, 2, 3,2]}
 df2 = pd.DataFrame(data2)
 fig3 = px.pie(df2, values='Keys', names='Labels', title='Tools and Libraries Used for this project :',color_discrete_sequence=custom_colors)
 fig3.update_traces(textinfo='none')
 fig3.update_traces(hole=0.4)
 fig3.update_layout(width=300, height=300)
 st.plotly_chart(fig3,use_container_width=True)
 
 add_vertical_space(15)
 
 data3 = {'Labels': ['Python','Yfinance', 'Plotly','Streamlit'],
        'Keys': [4, 4, 3, 3]}
 df3 = pd.DataFrame(data3)
 fig4 = px.pie(df3, values='Keys', names='Labels', title='Tools and Libraries Used for this project :',color_discrete_sequence=custom_colors)
 fig4.update_traces(textinfo='none')
 fig4.update_layout(width=300, height=300)
 st.plotly_chart(fig4,use_container_width=True)
 
 add_vertical_space(15)
 
 data4 = {'Labels': ['Python','Streamlit','Pandas','Numpy'],
        'Keys': [4, 4, 3, 3]}
 df4 = pd.DataFrame(data4)
 fig5 = px.pie(df4, values='Keys', names='Labels', title='Tools and Libraries Used for this project :',color_discrete_sequence=custom_colors)
 fig5.update_traces(textinfo='none')
 fig5.update_traces(hole=0.4)
 fig5.update_layout(width=300, height=300)
 st.plotly_chart(fig5,use_container_width=True)
 
 add_vertical_space(15)
 
 data5 = {'Labels': ['PowerBI','Excel'],
        'Keys': [4, 3]}
 df5 = pd.DataFrame(data5)
 fig6 = px.pie(df5, values='Keys', names='Labels', title='Tools and Libraries Used for this project :',color_discrete_sequence=custom_colors)
 fig6.update_traces(textinfo='none')
 fig6.update_layout(width=300, height=300)
 st.plotly_chart(fig6,use_container_width=True)
 



with col2: 
 st.markdown('## Summary', unsafe_allow_html=True)
 st.info('''
-  Results-driven Civil Engineer with 3.5 years of experience in building analytics and project management, seeking to transition into the dynamic field of data science. 
-  Leveraging a strong foundation in engineering principles, I am committed to applying my problem-solving skills and quantitative mindset to solve real-world challenges in data-driven environments.
-  Eager to further develop my expertise in data analysis, machine learning, and predictive modeling to contribute effectively to the data science landscape."
''')
#####################
# Navigation

 st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

 st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/vengatesan2612/" target="_blank">Portfolio</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
 def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

 def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

 def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
 def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
 st.markdown('''
## Education
''')


 txt('**Data Science Mastery Program** , *GUVI Geek Networks (IITM Research Park)*, Chennai',
'2023')
 st.markdown('''
- Data Science Professional with IIT Certification in Advanced Programming.
- I have successfully completed a comprehensive Python programming course, equipping me with a strong foundation in coding. Additionally, I have gained proficiency in working with databases, including SQL and MongoDB, enabling me to effectively manage and manipulate data. 
-  My aptitude for data visualization is demonstrated through practical projects where I have effectively communicated insights from complex datasets. Currently, I am actively engaged in various machine learning projects, honing my skills in predictive modeling and data analysis."
''')


 txt('**Bachelor of Engineering** (Civil),  *AVS Engineering College*, Salem',
'2014-2018')
 st.markdown('''
- GPA: 7.0
- Recipient of the esteemed Best Project Award (UG) from the Institution of Engineers (India) for exceptional contributions to a concrete strength testing project.
- My undergraduate coursework also encompassed comprehensive learning in building estimation and construction analysis. 
-  Through specialized course, I acquired a deep understanding of cost estimation, project planning, and construction methodologies. 
''')
 add_vertical_space(2)


#####################
 st.markdown('''
## Work Experience
''')

 txt('**Site Engineer**, *Vijayalakshmi Builders, Chennai*',
'2019-2022')
 st.markdown('''
- Managing an industrial building, such as an agro-production company, involves estimating the project, creating detailed drafts, analyzing construction management activities, progressing towards completion, calculating material requirements, and providing advance reports. 
- Outline the project's safety procedures and activities, and establish safety measures for the labor force.
- Establish a budget and oversee procurement processes to ensure smooth wage disbursement and construction operations.
''')


 txt('**Junior Site Engineer**, CMK Projects Pvt Ltd, Chennai',
'2018-2019')
 st.markdown('''
- Worked as a junior trainee engineer at the Tamil Nadu Slum Clearance Board (TNSCB) through a private sector company. This role involved being part of a high-budget project focused on constructing and managing over 1000 tenement apartments.
- I gained extensive knowledge in construction management. I was exposed to reviewing project blueprints and budgets, and I actively participated in overseeing on-site activities in collaboration with senior officials.
- Responsible for generating various site reports, compiling measurement reports, and submitting weekly wage details for the labor force. Additionally, I undertook the task of calculating site materials and preparing plans for upcoming activities.
''')
 add_vertical_space(2)
#####################
 st.markdown('''
## Projects 
''')
 txt4('YouTube data harvesting and warehousing', 'Develope a Streamlit application that allows users to access and analyze data from multiple YouTube channels.', 'https://github.com/Vengatesan-K/Youtube-Data-Harvesting-and-Warehousing')
 st.image("Images/ytt.png")
 txt4('PhonePe Pulse Data Visualization', ' Extract phonepe pulse data and process it to obtain insights and information that can be visualized in a user-friendly manner.', 'https://github.com/Vengatesan-K/PhonePe-Pulse-Data-Visualization')
 st.image("Images/php.png")
 txt4('Stock Price Analysis', 'Creating a stock price analysis application using Python and Streamlit combines technical skills with financial knowledge.','https://github.com/Vengatesan-K')
 st.image("Images/sti.png")
 txt4('Find Pdf Password', '📑PDF password recovery tool.', 'https://github.com/Vengatesan-K')
 st.image("Images/pdf.png")
 txt4('Phonepe Dahshboard', 'powerbi dashboard for phonepe pulse data from 2018 to 2022','https://github.com/Vengatesan-K/PowerBI-PhonePe')
 st.image("Images/phpp.png")
 
 st.markdown('''
## Social Media
''')
 add_vertical_space(2)
 
 tab1,tab2,tab3 = st.tabs(['GitHub','LinkedIn','Twitter'])
 
 with tab1:
  mention(
    label="VengatesanK",
    icon="github", 
    url="https://github.com/Vengatesan-K",
)
 with tab2:
   mention(
    label="Vengatesan@2612",
    icon="💼", 
    url="https://www.linkedin.com/in/vengatesan2612/",
)
 with tab3:
   mention(
    label="Vengatesan K",
    icon="twitter", 
    url="https://twitter.com/Vengatesan2612",
)
   
