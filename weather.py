import streamlit as st
import requests



def main():
    st.header("Find the weather")
    city = st.text_input("Enter the city").lower()

if __name__ == "__main__":
    main()    



