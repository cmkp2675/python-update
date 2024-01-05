import streamlit as st
import subprocess

# Function to switch Python versions using a virtual environment
def switch_python_version(new_version):
    # Create a virtual environment with the desired Python version
    venv_command = f"python -m venv venv_{new_version}"
    subprocess.run(venv_command, shell=True, check=True)

    # Activate the virtual environment
    activate_command = (
        f"source venv_{new_version}/bin/activate"  # For Linux/Mac
        if st.os_is_linux() or st.os_is_macos()
        else f"venv_{new_version}\\Scripts\\activate"  # For Windows
    )
    subprocess.run(activate_command, shell=True, check=True)

# Streamlit app code
st.title("Switch Python Version")

# Widget to input the desired Python version
new_version = st.text_input("Enter Python version to switch to:", "3.8")

# Button to trigger Python version switch
if st.button("Switch Python Version"):
    try:
        switch_python_version(new_version)
        st.success(f"Switched to Python version {new_version}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Rest of your Streamlit app code here

