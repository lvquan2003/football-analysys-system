import os
import shutil
import streamlit as st
import subprocess

def update_main_py(video_path):
    with open('main.py', 'r') as file:
        content = file.readlines()

    for i, line in enumerate(content):
        if line.strip().startswith("video_frames = read_video"):
            normalized_path = video_path.replace("\\", "/")
            content[i] = f"    video_frames = read_video('{normalized_path}')\n"
            break

    with open('main.py', 'w') as file:
        file.writelines(content)

def clear_stub_folder(stub_folder):
    if os.path.exists(stub_folder):
        for file in os.listdir(stub_folder):
            file_path = os.path.join(stub_folder, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)

def clear_output_video(output_video_path):
    if os.path.exists(output_video_path):
        os.remove(output_video_path)

def run_main_py():
    subprocess.run(['python', 'main.py'], check=True)

def display_video(video_path):
    video_file = open(video_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

# Streamlit appapp
# st.title("Football Analysys App")

st.markdown(
    """
    <style>
    .main {
        background-image: url('https://img.freepik.com/premium-vector/dynamic-gradient-football-background_1226107-217.jpg?semt=ais_hybrid');
        background-size: cover;
        background-repeat: no-repeat;
        padding: 50px;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
    }
    </style>
    <div class="main">
    <h1 class="title"> Football Analysis App</h1>
    </div>
    """, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

stub_folder = "stubs"
input_folder = "input_videos"
output_folder = "output_videos"
output_video_path = os.path.join(output_folder, "output_video.mp4")

clear_stub = st.checkbox("Clear stub folder before processing", value=False)

if uploaded_file is not None:
    input_video_path = os.path.join(input_folder, uploaded_file.name)
    input_video_path = os.path.normpath(input_video_path)  
    with open(input_video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Video saved to {input_folder} as {uploaded_file.name}")

    # Display the uploaded input video
    st.subheader("Input Video:")
    st.video(uploaded_file)  

    update_main_py(input_video_path)

    if clear_stub:
        clear_stub_folder(stub_folder)
        st.warning("Cleared stub folder.")

    # Clear the previous output video
    clear_output_video(output_video_path)

    if st.button("Process Video"):
        st.info("Processing video...")
        try:
            run_main_py()
            st.success("Processing complete!")

            if os.path.exists(output_video_path):
                st.subheader("Processed Video:")
                display_video(output_video_path)

                # Provide a download link for the output video
                # with open(output_video_path, "rb") as file:
                #     btn = st.download_button(
                #         label="Download Processed Video",
                #         data=file,
                #         file_name="output_video.mp4",
                #         mime="video/x-msvideo"
                #     )
            else:
                st.error("Output video not found!")
        except subprocess.CalledProcessError as e:
            st.error(f"Error occurred while running main.py: {e}")
else:
    st.error("Please upload a video before processing.")
