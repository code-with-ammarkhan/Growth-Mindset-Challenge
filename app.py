import streamlit as st

# Page config
st.set_page_config(
    page_title="Growth Mindset Project",
    page_icon="☘️"
)

# 1) Growth Mindset AI banner sab se upar
st.image("growth_mindset_ai.png", use_column_width=True)

# Title
st.title("Growth Mindset Challenge: Web App With Streamlit")

# Purple line
st.image("purple_line.png", use_column_width=True)

# Welcome Section
st.header("🚀 Welcome to Your Growth Journey! ")
st.write("""
Dare to challenge yourself, transform failures into wisdom, 
and unlock the limitless potential within you. 
This AI-powered platform is your companion in cultivating a growth mindset 
through deep reflection, meaningful challenges, and impactful achievements. 🌟
""")

# Purple line
st.image("purple_line.png", use_column_width=True)

# Quote Section
st.header("💡 Today's Growth Mindset Insight! ")
st.write("""
Success is never the ultimate destination, and failure is never the end—
what truly matters is the unwavering courage to keep moving forward.
- Winston Churchill
""")

# Need More Motivation? button image
st.image("need_more_motivation.png", width=250)

# Purple line
st.image("purple_line.png", use_column_width=True)

# Challenge input
st.header("⚡ What's Your Challenge Today? ")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started")

# Purple line
st.image("purple_line.png", use_column_width=True)

# Reflection section
st.header("🧠 Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experiences helps you grow! Share your difficulties.")

# Purple line
st.image("purple_line.png", use_column_width=True)

# Achievements section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🤩")

# Purple line
st.image("purple_line.png", use_column_width=True)

# Footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**©️ Created By Code With Ammar**")
