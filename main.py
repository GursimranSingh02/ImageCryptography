import streamlit as st
from ImageCryptography import generate_key, encrypt_image, decrypt_image

# Page configuration
st.set_page_config(page_title='AES Image Cryptor', page_icon='/Python/ImageCryption/user_secret.ico')

# Title
st.title('AES Image Cryptor')

# Radio buttons to select the mode 
choice = st.radio('Enter your choice', ('Encryption', 'Decryption'))

if choice == 'Encryption':
    # Choose the image file for encryption
    img_path = st.file_uploader('Choose an image file...', type=['jpg', 'jpeg', 'png']) 

    if img_path is None:
        st.warning('Please upload an image file for encryption.')
    else:
        # Choice for key
        key_option = st.radio('Choose the key', ('Existing Key', 'New Key'))

        if key_option == 'Existing Key':
            # Choose an existing key file
            key_path = st.file_uploader('Choose key file...', type=['key']) 
        elif key_option == 'New Key':
            # Provide the name for new key file
            User_file_name = st.text_input('Enter the name of Key File')

            # Button to generate new key
            key_generate_button = st.button('Generate Key')

            
            # To generate the key
            if key_generate_button:
                # Checks whether the input field is empty
                if User_file_name == '':
                    st.warning('Please enter the name of key')

                else:
                    # Extension added to key name
                    file_name = User_file_name + '.key'

                # Function to generate the key
                    generate_key(file_name)

                    st.success('Key Generated Successfully')
                    st.info('Now select this key using Existing Key option')

                # Download button for key
                if 'file_name' in locals():
                    st.download_button(label='Download Key', data=open(file_name, 'rb'), file_name=file_name)

        # Input field for the name of the encrypted file
        encrypt_image_name = st.text_input('Enter the name of encrypted file ', placeholder='EncryptedImage.enc')

        # Button to start encryption 
        submit = st.button('Encrypt')

        # To encrypt the image 
        if submit:
            if key_option == 'Existing Key' and key_path is None:
                st.warning('Please select an existing key file.')
            elif encrypt_image_name == '':
                st.warning('Please enter the name for the encrypted file.')
            else:
                encrypt_image(img_path, key_path, encrypt_image_name)
                st.success('Image Encrypted Successfully')

                # Download button for Encrypted File
                st.download_button(label='Download Encrypted File', data=open(encrypt_image_name, 'rb'), file_name=encrypt_image_name)


elif choice == 'Decryption':
    # Choose the encrypted image file for decryption
    encrypted_img_path = st.file_uploader('Choose an encrypted image file...', type=['enc'])

    if encrypted_img_path is None:
        st.warning('Please upload an encrypted image file for decryption.')
    else:
        # Choose the key
        key_path = st.file_uploader('Choose the key file...', type=['key'])

        if key_path is None:
            st.warning('Please upload a key file for decryption.')
        else:
            # Input field for the name of the decrypted file
            decrypt_image_name = st.text_input('Enter the name of decrypted file along with its extension', placeholder='DecryptedImage.jpg')

            # Button to start decryption
            submit = st.button('Decrypt')

            # To decrypt the image
            if submit:
                if decrypt_image_name == '':
                    st.warning('Please enter the name for the decrypted file.')
                else:
                    decrypt_image(encrypted_img_path, key_path, decrypt_image_name)
                    st.success('Image Decrypted Successfully')

                    # Download button for decrypted file
                    st.download_button(label='Download Decrypted File', data=open(decrypt_image_name, 'rb'), file_name=decrypt_image_name)
