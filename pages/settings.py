import streamlit as st  # pip install streamlit
from firebase import upload_image
name = st.session_state["user_id"]

if name:
    st.write("## Update your profile")

    st.write("#### upload your image here")

    image_file = st.file_uploader('Upload image', type=['jpg', 'jpeg', 'png'])


# If both username and image file are provided, upload the image and display it
    if name and image_file:
        image_url = upload_image(name, image_file)
        st.success('Image uploaded successfully!')
        st.image(image_url, width=300)
else:
    st.write("## Sign-up to get started")
