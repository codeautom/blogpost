import streamlit as st
from crewai import Crew
from agents import planner, writer, editor
from tasks import plan, write, edit

# Create a Streamlit interface
def main():
    st.title("Multi-Agent Workflow with CrewAI and Groq")

    # Text input for the topic
    topic = st.text_input("Enter a topic for the AI crew", "")

    if st.button("Genrate blog"):
        with st.spinner('Runing..'):
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
