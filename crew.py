__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3

import streamlit as st
from crewai import Crew
from agents import planner, writer, editor
from tasks import plan, write, edit

# Create a Streamlit interface
def main():
    st.title("Multi-Agent Workflow with CrewAI and Groq")

    # Display introductory text
    st.markdown("""
    **
    CHATGROQ API USING OPEN SOURCE MODEL BY META : "llama3-70b-8192"
    """)

    # Text input for the topic
    topic = st.text_input("Enter a topic for the AI crew", "")

    if st.button("Generate blog"):
        with st.spinner('Running..'):
            try:
                # Initialize the crew
                crew = Crew(
                    agents=[planner, writer, editor],
                    tasks=[plan, write, edit],
                    verbose=2
                )

                # Kick off the crew with input topic
                result = crew.kickoff(inputs={"topic": topic})

                # Since result is likely a string, display it directly
                st.markdown(result, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
