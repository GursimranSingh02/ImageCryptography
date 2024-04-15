from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from io import BytesIO


# Function to encrypt the image
def encrypt_image(image_path, key_file, encrypted_file):
    # Open image
    img = Image.open(image_path)

    # Convert image to bytes and apply padding 
    img_byte_arr = pad(img.tobytes(), 16)

    # Generate a random IV
    iv = get_random_bytes(16)
  
    # Open and read the key
    with BytesIO(key_file.getvalue()) as f:
        key = f.read()

    # Creating a cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt image byte array
    encrypted_img_byte_arr = cipher.encrypt(img_byte_arr)

    # Save IV, image size, and encrypted image
    with open(encrypted_file, 'wb') as encrypted_file:
        encrypted_file.write(iv)
        encrypted_file.write(img.size[0].to_bytes(8, byteorder='big'))
        encrypted_file.write(img.size[1].to_bytes(8, byteorder='big'))
        encrypted_file.write(encrypted_img_byte_arr)



# Function to decrypt the image 
def decrypt_image(encrypted_img_file, key_file, decrypted_file):
    
    # Read the content of the uploaded encrypted image file
    encrypted_img_byte_arr = BytesIO(encrypted_img_file.read())

    # Read IV, image size, and byte array
    with encrypted_img_byte_arr as encrypted_file:
        iv = encrypted_file.read(AES.block_size)
        width = int.from_bytes(encrypted_file.read(8), byteorder='big')
        height = int.from_bytes(encrypted_file.read(8), byteorder='big')
        encrypted_img_byte_arr = encrypted_file.read()

    # Read the content of the uploaded key file
    key = BytesIO(key_file.read()).read()

    # Creating cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Unpad the padded contents
    decrypted_img_byte_arr = unpad(cipher.decrypt(encrypted_img_byte_arr), 16)

    # Decrypt image byte array
    decrypted_img = Image.frombytes('RGB', (width, height), decrypted_img_byte_arr)

    # Save the decrypted image
    decrypted_img.save(decrypted_file)


# Generating a random key 
def generate_key(file_name):
    key_val = get_random_bytes(16)
    with open(file_name, 'wb') as key_file:
        key_file.write(key_val)
