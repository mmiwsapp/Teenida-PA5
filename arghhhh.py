import streamlit as st 
import openai
import json
import pandas as pd


OPENAI_API_KEY= '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' 
client = openai.OpenAI(api_key=OPENAI_API_KEY)
prompt = """Act as a social media cooordinator. Write product slogan. You will receive product description and
            you should give 20 ideas of product slogan and also give description to support the slogan.
            List the slogan in a Json array, one slogan per line. 
            Each slogan should have 3 fields:
            -"Product name":product name from the user input
            -"Slogan"
            -"Slogan description": the description of the slogan to support its suitability
            Don't say anything at first. Wait for the user to say something.
            """
#user_input = "Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."


st.title('Cool slogan serving here!')
st.markdown('Input your product description to get slogan ideas. \n\
            The AI will give you 20 ideas of slogan and its description')

#Create and name sidebar
st.sidebar.header('Choose your product slogan')
st.sidebar.write("""#### Your OpenAi API key here""")
#Add text input to the sidebar
api_key_input = st.sidebar.text_input('Enter your API key:', 'Your OpenAI API key')
 


user_input = st.text_area("Enter product description:", "Your text here")

# submit button after text input

if st.button('Submit'):
    messages_so_far = [
            {"role": "system", "content": prompt},
            {'role': 'user', 'content': user_input},
        ]
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages_so_far
    )                     
     
    # Show the response from the AI in a box
    st.markdown('**AI response:**')
    translation_dict = response.choices[0].message.content
    
    sd = json.loads(translation_dict)
    print(sd) 
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df) 
