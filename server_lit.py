import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit application.")

name = st.text_input("Enter your name:")
address = st.text_input("Enter your address:")
birthday = st.date_input("Select your birthday:")
customer_type = st.selectbox("Select customer type:", ["Regular", "Premium", "VIP"])
if st.button("Submit"):
    if name and address:
        with open("user_data.txt", "a") as file:
            file.write(f"Name: {name}, Address: {address}, Birthday: {birthday}, Customer Type: {customer_type}\n")

        st.success(f"Thank you, {name}! Your address {address} has been recorded.")
    else:
        st.error("Please fill in both fields.")


st.write("You can use this app to collect user information.")
st.write("This is a basic example of a Streamlit app that collects user input.")
st.write("Feel free to modify and expand this app as needed.")
st.write("Streamlit makes it easy to create interactive web applications with Python.")
st.write("You can run this app using the command: `streamlit run server_lit.py`")
st.write("Make sure you have Streamlit installed in your Python environment.")
st.write("Visit the [Streamlit documentation](https://docs.streamlit.io/) for more information.")
st.write("Happy coding with Streamlit!")
st.write("This app is designed to demonstrate basic user input handling in Streamlit.")
st.write("You can add more features and functionalities as you learn more about Streamlit.")
st.write("Streamlit is a powerful tool for building data-driven web applications.")
st.write("You can use this app to create dashboards, visualizations, and more.")
st.write("Explore the possibilities with Streamlit and create amazing applications.")
st.write("Remember to save your work and keep experimenting with different features.")