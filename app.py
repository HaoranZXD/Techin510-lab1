import streamlit as st

st.set_page_config(
    page_title="Haoran Zeng",
    page_icon="🤖",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
) 

col1, col2 = st.columns([0.4, 0.6])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![](https://avatars.githubusercontent.com/u/148395441?s=400&u=61ba9a316cf6f4c37bf88522b51aa3d79e34ad45&v=4)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://avatars.githubusercontent.com/u/148395441?s=400&u=61ba9a316cf6f4c37bf88522b51aa3d79e34ad45&v=4')
with col2:
    st.markdown(
        """
    # Haoran Zeng (He/Him)
                
    ### Email: [haoranz@uw.edu](haoranz@uw.edu)
    """
    )

st.markdown(
    """
# Education
### University of Washington
Master of Science in Technology Innovation
### Tsinghua University
Master of Arts in Design Studies
### Tongji University
Bachelor of Engineering in Industrial Design
"""


)

st.markdown(
    """
# Professional Experience
### Zilliz
- Role: Design Intern
- Key Projects and Accomplishments: Branding Overhaul
### Unilumin LED
- Role: Project Manager Trainee
- Key Projects and Accomplishments: LED Display Project Leadership

"""


)

st.markdown(
    """
# Hobbies and Interests
"""

)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
    ### 🎵Music
    """
    )
with col2:
    st.markdown(
        """
    ### 🎞️Movies
    """
    )
with col3:
    st.markdown(
        """
    ### 👟Sports
    """
    )


st.markdown(
    """
# Projects
### Future Mobility System Design Sponsored by Aston Martin
- Explored potential technological advancements and societal values shaping future mobility, envisioning a 2050 
urban transport system rewarding environmental contributors. In this concept, Aston Martin evolves from a car 
manufacturer to an exclusive service provider, leveraging the Eco-coin system and superconducting magnetic 
levitation technology.

### Packaging Upcycling Sponsored by LVMH
- Investigated the fusion of bio-based materials with used packaging. Conceived an installation using repurposed 
paper boxes, a set of 3D-printed molds, and a unique production process inspired by Dior's flower embroidery 
dresses. This design was chosen from 54 projects for exhibition at The Bund Finance Center by LVMH.

### Beijing Changping Urban Renewal New Scene Design
- Revitalized street vitality through art curation, organized street art events, and designed a series of public art 
installations. Received top honors and was invited for further design development and execution. The project is 
currently in the implementation phase.
"""

)


col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 50%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/148395441?s=400&u=61ba9a316cf6f4c37bf88522b51aa3d79e34ad45&v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)