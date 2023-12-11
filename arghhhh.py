import streamlit as st 
import openai  
import json
import pandas as pd


user_api_key = st.sidebar.text_input("OpenAI API key", type="password") 
 
client = openai.OpenAI(api_key=user_api_key) 
prompt =  """Act as a social media coordinator. Write a product slogan. You will receive product description and
            you should give 20 ideas of product slogan and also give description to support the slogan.
            List the slogan in a Json array, one slogan per line. 
            Each slogan should have 2 fields,
            -"Slogan"
            -"Slogan description": the description of the slogan to support its suitability
            Don't say anything at first. Wait for the user to say something.
            """

st.title('Cool slogan serving here!')
st.markdown('Input your product description to get slogan ideas. \n\
            The AI will give you 20 ideas of slogan and its description')

user_input = st.text_area("Enter product description:", "Your text here")

#submit button after text input
if st.button('Submit'):
    messages_so_far = [
            {"role": "system", "content": prompt},
             {'role': 'user', 'content': user_input},
         ]
    response = client.chat.completions.create(
             model="gpt-3.5-turbo",
             messages=messages_so_far
     )                     
     
    st.markdown('**AI response:**')
    slogan_dict = response.choices[0].message.content
        
    sd = json.loads(slogan_dict)
    print(sd) 
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df)

    #response_fromAI = """{"sloganList": [ {"Product name": "Ice Cream", "Slogan": "Indulge in Pure Delight", "Slogan description": "This slogan emphasizes the delicious and satisfying experience of enjoying ice cream, making it irresistible to consumers."}, {"Product name": "Ice Cream", "Slogan": "Cool Treat for Hot Days", "Slogan description": "This slogan highlights the refreshing nature of ice cream, making it the perfect choice to beat the heat during summer."}, {"Product name": "Ice Cream", "Slogan": "Frozen Bliss in Every Bite", "Slogan description": "This slogan conveys the idea that each bite of ice cream brings a moment of pure happiness and satisfaction."}, {"Product name": "Ice Cream", "Slogan": "Sweeten Your Day", "Slogan description": "This slogan suggests that ice cream can add a touch of sweetness and joy to any day, making it a desirable treat."}, {"Product name": "Ice Cream", "Slogan": "Taste the Magic", "Slogan description": "This slogan implies that ice cream has a unique and delightful taste that is almost magical, creating a sense of anticipation."}, {"Product name": "Ice Cream", "Slogan": "Scoop Up Happiness", "Slogan description": "This slogan evokes the idea that ice cream can bring joy and happiness with every scoop, appealing to consumers looking for a positive experience."}, {"Product name": "Ice Cream", "Slogan": "Crafted with Deliciousness", "Slogan description": "This slogan suggests that ice cream is carefully made using high-quality ingredients, ensuring a delicious taste that consumers crave."}, {"Product name": "Ice Cream", "Slogan": "The Perfect Frozen Treat", "Slogan description": "This slogan emphasizes that ice cream is the ideal choice for a frozen dessert, with its creamy texture and wide variety of flavors."}, {"Product name": "Ice Cream", "Slogan": "Discover a World of Flavors", "Slogan description": "This slogan invites consumers to explore the wide range of flavors available in ice cream, offering a sense of adventure and variety."}, {"Product name": "Ice Cream", "Slogan": "A Scoop of Happiness", "Slogan description": "This slogan suggests that ice cream is not just a dessert, but a source of joy and delight, providing a sense of comfort and happiness."}, {"Product name": "Ice Cream", "Slogan": "Experience Frozen Euphoria", "Slogan description": "This slogan conveys the idea that consuming ice cream leads to a state of pure bliss and satisfaction, creating an irresistible appeal."}, {"Product name": "Ice Cream", "Slogan": "Twist, Lick, and Enjoy", "Slogan description": "This slogan playfully encourages consumers to savor ice cream by engaging with it in a fun and interactive way, creating a memorable experience."}, {"Product name": "Ice Cream", "Slogan": "Cool Down with Creaminess", "Slogan description": "This slogan highlights the smooth and creamy texture of ice cream, making it a desirable choice for those wanting a refreshing treat."}, {"Product name": "Ice Cream", "Slogan": "Satisfy Your Sweet Tooth", "Slogan description": "This slogan appeals to consumers with a sweet tooth, suggesting that ice cream is the perfect dessert to satisfy their cravings."}, {"Product name": "Ice Cream", "Slogan": "Unleash Your Inner Child", "Slogan description": "This slogan implies that enjoying ice cream allows people to tap into their playful side, offering a sense of nostalgia and carefree fun."}, {"Product name": "Ice Cream", "Slogan": "A Scoop of Pure Happiness", "Slogan description": "This slogan captures the essence of ice cream as a source of pure joy and happiness, making it impossible to resist."}, {"Product name": "Ice Cream", "Slogan": "Cool Indulgence for Every Occasion", "Slogan description": "This slogan suggests that ice cream is the perfect treat for any occasion, offering a refreshing and indulgent option to enjoy."}, {"Product name": "Ice Cream", "Slogan": "Taste the Sweet Life", "Slogan description": "This slogan reflects the idea that ice cream brings a touch of sweetness and enjoyment to life, making it a favorite indulgence for many."}, {"Product name": "Ice Cream", "Slogan": "Melt into Deliciousness", "Slogan description": "This slogan evokes the idea that ice cream has a tempting melting quality, creating a sense of indulgence and pleasure."}, {"Product name": "Ice Cream", "Slogan": "Every Bite, a Moment of Bliss", "Slogan description": "This slogan emphasizes that each bite of ice cream provides a moment of pure bliss and satisfaction, making it a truly enjoyable dessert."} ]}"""
   
   
   
   
   
    # json_dict = json.loads(slogan_dict) 
    # response_indict = json_dict[list(json_dict.keys())[0]]
    # response_formulated = {
    #     "Product name": [dict_unit["Product name"] for dict_unit in response_indict],
    #     "Slogan": [dict_unit["Slogan"] for dict_unit in response_indict],
    #     "Slogan description": [dict_unit["Slogan description"] for dict_unit in response_indict],
    # }


    # data_df = pd.DataFrame.from_dict(response_formulated)
    # st.table(data_df)
