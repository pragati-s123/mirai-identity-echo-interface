import streamlit as st

st.title("The Signal Vault")
st.write("Enter your identity and a message. The vault will confirm recipt once transmitted.")

# TAKE USER INPUT
user_name = st.text_input("Your Identity")
user_message = st.text_input("Your Message")


if st.button("TRANSMIT"):
    if user_name == "":
        st.error("Please provide your name.")
    elif user_message== "":
        st.warning("Please type a message to transmit. ")
    else:
        pass
    
st.success(f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}")

char_count = len(user_message)
token_count = char_count // 4
st.info(f"System Check: Your message will consume approximately {token_count} tokens from our context window.")