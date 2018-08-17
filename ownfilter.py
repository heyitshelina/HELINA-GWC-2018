from PIL import Image

# PRESS ENTER TO BEGIN


# RGB values for recoloring.
print("the input for these should be close to the numbers 0, 51, 76")
darkBlue = ( int(input("pick a number from 0 to 255: ")), int(input("pick a number from 0 to 255: ")),  int(input("pick a number from 51 to 255: ")))

print("the input for these should be close to the numbers 217, 26, 33")#(0, 51, 76)
red = ( int(input("pick a number from 0 to 255: ")), int(input("pick a number from 0 to 255: ")),  int(input("pick a number from 51 to 255: ")))

print("the input for these should be close to the numbers 112, 150, 158")#(217, 26, 33)
lightBlue = ( int(input("pick a number from 0 to 255: ")), int(input("pick a number from 0 to 255: ")),  int(input("pick a number from 51 to 255: ")))

print("the input for these should be close to the numbers 252, 227, 166")#(112, 150, 158)
yellow = ( int(input("pick a number from 0 to 255: ")), int(input("pick a number from 0 to 255: ")),  int(input("pick a number from 51 to 255: ")))


# Import image.
my_image = Image.open("rihanna.jpeg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for pixel in image_list:
    intensity = pixel[0] + pixel[1] + pixel[2]
    if intensity <= 182:
        recolored.append(darkBlue)
    elif intensity >182 and intensity <= 364:
        recolored.append(red)
    elif intensity >364 and intensity <= 546:
        recolored.append(lightBlue)
    elif intensity >= 546:
        recolored.append(yellow)

new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"