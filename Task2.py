from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Encrypt the image by adding the key to each pixel
    encrypted_array = (img_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved at {output_path}")

def decrypt_image(image_path, key, output_path):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Decrypt the image by subtracting the key from each pixel
    decrypted_array = (img_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved at {output_path}")

# Example usage
print("Image Encryption and Decryption Program")
action = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt an image: ").lower()
image_path = input("Enter the path of the image: ")
key = int(input("Enter the encryption key (a number): "))
output_path = input("Enter the path to save the output image: ")

if action == 'encrypt':
    encrypt_image(image_path, key, output_path)
elif action == 'decrypt':
    decrypt_image(image_path, key, output_path)
else:
    print("Invalid action! Please type 'encrypt' or 'decrypt'.")
