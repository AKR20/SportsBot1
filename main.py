import streamlit as st
from diffusers import DiffusionPipeline
import config
import openai

openai.api_key = config.OPENAI_KEY

# Function to show the text to image page
def cricket_bot_page():
    st.title("Cricket Bot")
    
    # Create a text input for user input
    user_input = st.text_input("You:")
    
    # Create a button to send the user input to the cricket bot
    if st.button("Send"):
        # Define the cricket bot's instruction and prompt
        instruction = "You are a cricket expert and provide information and answers related to cricket. Please ask your cricket-related questions."
        prompt = f"{instruction}\n\nUser: {user_input}\nCricket Bot:"
        
        # Call the OpenAI cricket bot API to get a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.6,
            top_p=1.0,
            n=1,
            stop=None
        )
        
        # Extract the generated response from the API result
        bot_response = response.choices[0].text.strip()
        
        # Display the cricket bot's response
        st.text_area("Cricket Bot:", value=bot_response, height=200)

# Function to show the football bot page
def football_bot_page():
    st.title("Football Bot")
    
    # Create a text input for user input
    user_input = st.text_input("You:")
    
    # Create a button to send the user input to the football bot
    if st.button("Send"):
        # Define the football bot's instruction and prompt
        instruction = "You are a football expert and provide information and answers related to football. Please ask your football-related questions."
        prompt = f"{instruction}\n\nUser: {user_input}\nFootball Bot:"
        
        # Call the OpenAI football bot API to get a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.6,
            top_p=1.0,
            n=1,
            stop=None
        )
        
        # Extract the generated response from the API result
        bot_response = response.choices[0].text.strip()
        
        # Display the football bot's response
        st.text_area("Football Bot:", value=bot_response, height=200)

def main():
    # Set the page layout
    st.set_page_config(layout="wide")
    
    # Create a sidebar with options
    st.sidebar.title("Options")
    options = ["Cricket Bot", "Football Bot"]
    choice = st.sidebar.radio("Select a bot", options)
    
    # Render the selected bot page
    if choice == "Cricket Bot":
        cricket_bot_page()
    elif choice == "Football Bot":
        football_bot_page()

if __name__ == "__main__":
    main()
