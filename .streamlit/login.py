import streamlit as st

# Define the usernames and passwords (you can store these securely using st.secrets)
valid_credentials = {
    "user1": "password1",
    "user2": "password2"
}

# Function to authenticate users
def authenticate(username, password):
    return valid_credentials.get(username) == password

# Login page
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password")
    return False

# Laboratory Team page (only accessible to authenticated users)
def laboratory_team_page():
    st.title("Laboratory Team")
    st.write("Welcome to the Laboratory Team page. Only authenticated users can access this.")

# Upload_Data page (only accessible to authenticated users)
def upload_data_page():
    st.title("Upload_Data")
    st.write("Welcome to the Upload_Data page. Only authenticated users can access this.")

# Main function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Laboratory Team", "Upload_Data"])

    if page == "Home":
        st.title("Home Page")
        st.write("Welcome to the home page.")

    elif page == "Laboratory Team":
        if login():
            laboratory_team_page()

    elif page == "Upload_Data":
        if login():
            upload_data_page()

if __name__ == "__main__":
    main()
