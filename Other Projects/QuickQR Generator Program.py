# QuickQR Generator Program

'''Key Features:
- Takes user input and generates a QR code for any text or link.
- Saves the QR code as a PNG image file.
- Easy-to-use and simple for beginners.'''

# IMPORT the qrcode library to generate QR codes
import qrcode

# Step 1: Get the data input from the user to convert into a QR code
data = input("Enter data which you want to convert into a QR code: ")

# Step 2: Generate the QR code image
img = qrcode.make(data)

# Step 3: Verify the type of the image object (optional)
type(img)  # qrcode.image.pil.PilImage

# Step 4: Save the generated QR code image to a file
file_name = input("Enter the name of the file to save the QR code (without extension): ")
img.save(file_name + ".png")  # Saves the image as 'filename.png'

# Final message to the user
print(f"QR Code successfully generated and saved as {file_name}.png")
