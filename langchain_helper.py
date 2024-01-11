import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from dotenv import load_dotenv

load_dotenv()


def generate_future_story(user_name, user_age, user_location, story_input, future_year, openai_api_key):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    prompt_template_name = PromptTemplate(
        input_variables = ['user_name','user_age', 'user_location', 'story_input', 'future_year'],
        template = "I have a User with the following details: Name: {user_name} Age: {user_age} Location:{user_location} and I want to generate a future story inspired by {story_input} for the future year: {future_year}"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="story_response")

    response = name_chain({'user_name': user_name, 'user_age': user_age, 'user_location': user_location, 'story_input': story_input, 'future_year': future_year})


    return response

if __name__ == "__main__":
    print(generate_future_story("Osman", "25", 'Canada east', 'Blah blah', '2050'))
