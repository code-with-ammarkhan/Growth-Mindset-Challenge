#steamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="☘️")

st.title("Growth Mindset Challenge: Web App With Steamlit ")

st.header("🚀 Welcome to Your Growth Journey! ")
st.write("Dare to challenge yourself, transform failures into wisdom, and unlock the limitless potential within you. This AI-powered platform is your companion in cultivating a growth mindset through deep reflection, meaningful challenges, and impactful achievements. 🌟 ")

# Quote section
st.header("💡 Today's Growth Mindset Insight! ")
st.write("Success is never the ultimate destination, and failure is never the end—what truly matters is the unwavering courage to keep moving forward.- Winston Churchill")

# Challenge input
st.header("⚡ What's Your Challenge Today? ")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started")

# Reflection section
st.header(" Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experiences helps you grow! Share your difficulties.")

# Achievements section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🤩")

# Footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**©️ Created By Code With Ammar**")
