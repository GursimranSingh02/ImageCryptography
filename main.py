import streamlit as st
from ImageCryptography import encrypt_image, decrypt_image, generate_key

# Page configuration
st.set_page_config(page_title='AES Image Cryptor', page_icon='user_secret.ico')

# Title
st.title('AES Image Cryptor')

# Radio buttons to select the mode 
choice = st.radio('Enter your choice', ('Encryption', 'Decryption'))

if(choice == 'Encryption'):
    # Choose the image file for encryption
    img_path = st.file_uploader('Choose an image file...', type=['jpg', 'jpeg', 'png']) 

    # Choice for key
    key_option = st.radio('Choose the key', ('Existing Key', 'New Key'))

    if(key_option == 'Existing Key'):
        # Choose an existing key file
        key_path = st.file_uploader('Choose key file...', type=['key']) 

    elif(key_option == 'New Key'):
        # Provide path for new key file
        key_path = st.text_input('Enter the path where you want to store the key file along with key file name', placeholder='/Folder/Sub-folder/KeyFile.key')

        # Button to generate new key
        key_generate_button = st.button('Generate Key')

        # To generate the key
        if key_generate_button == True:
            generate_key(key_path)
            st.success('Key Generated Successfully')
            st.info('Now select this key using Existing Key option')

    # Input field for the name and path of the encrypted file
    encrypt_image_name = st.text_input('Enter the name of encrypted file along with its path', placeholder='/Folder/Sub-folder/EncryptedFile.enc')

    # Button to start encryption
    submit = st.button('Encrypt')

    # To encrypt the image
    if submit:
        encrypt_image(img_path, key_path, encrypt_image_name)
        st.success('Image Encrypted Successfully')

elif(choice == 'Decryption'):
    # Choose the encrypted image file for decryption
    encrypted_img_path = st.file_uploader('Choose an encrypted image file...', type=['enc'])
   
    # Choose the key
    key_path = st.file_uploader('Choose the key file...', type=['key'])

    # Input field for the name and path of the decrypted file
    decrypt_image_name = st.text_input('Enter the name of decrypted file along with its path', placeholder='/Folder/Sub-folder/DecryptedFile.jpg')
    
    # Button to start decryption
    submit = st.button('Decrypt')

    # To decrypt the image
    if submit:
        decrypt_image(encrypted_img_path, key_path, decrypt_image_name)
        st.success('Image Decrypted Successfully')
       
