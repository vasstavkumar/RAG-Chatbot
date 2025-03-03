import streamlit as st
from api_utils import upload_document, list_documents, delete_document

def display_sidebar():
    model_options = ['llama3-8b-8192']
    st.sidebar.selectbox("Select Model", options=model_options, key="model")

    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx"])
    if uploaded_file and st.sidebar.button("Upload"):
        with st.spinner("Uploading..."):
            upload_response = upload_document(uploaded_file)
            if upload_response:
                st.sidebar.success(f"File uploaded successfully with ID {upload_response['file_id']}.")
                st.session_state.documents = list_documents()

    st.sidebar.header("Uploaded Documents")
    if st.sidebar.button("Refresh Document List"):
        st.session_state.documents = list_documents()

    if "documents" in st.session_state and st.session_state.documents:
        for doc in st.session_state.documents:
            st.sidebar.text(f"{doc['filename']} (ID: {doc['id']})")

        selected_file_id = st.sidebar.selectbox("Select a document to delete", 
                                                options=[str(doc['id']) for doc in st.session_state.documents])
        if st.sidebar.button("Delete Selected Document"):
            delete_response = delete_document(selected_file_id)
            if delete_response:
                st.sidebar.success(f"Document deleted successfully.")
                st.session_state.documents = list_documents()