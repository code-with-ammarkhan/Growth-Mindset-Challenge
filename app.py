#steamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="🔱")
st.title("Growth Mindset Challenge: Web App With Steamlit ")

st.header("🚀 Welcome to Your Growth Journey! ")
st.write("Dare to challenge yourself, transform failures into wisdom, and unlock the limitless potential within you. This AI-powered platform is your companion in cultivating a growth mindset through deep reflection, meaningful challenges, and impactful achievements. 🌟 ")

#quote section
st.header("💡 Today's Growth Mindset Insight! ")
st.write("Success is never the ultimate destination, and failure is never the end—what truly matters is the unwavering courage to keep moving forward.- Winston Churchill")


st.header("⚡ What's Your Challenge Today? ")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"💪You're facing: {user_input}. Keep pushing forward towards your goal!🚀")

else:
    st.warning("Tell us about your challenge to get started")

    #reflexing
    
    st.header(" Reflect on Your Learning")
    reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection {reflection}")
else:
 st.info("Reflection on past experience help you grow! Share your difficulties")


 #acheivements
 st.header("🏆 Celebrate Your Wins!")
 achivement = st.text_input("Share something you've recently accomplished")


if achivement: 
     st.success(f"🎉 Amazing! You acheived: {achivement}")
else:
     st.info("Big or small , every acheviment counts! Share one now 🤩")

    
#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**©️ Created By Code With Ammar**")


