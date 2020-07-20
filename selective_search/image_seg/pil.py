from PIL import Image

im = Image.open("/Users/sunhao/Projects/vscode/python/RCNN/selective_search/image_seg/assets/test.jpg")

# Flip the image from left to right
im_flipped = im.transpose(method=Image.ROTATE_90)
# To flip the image from top to bottom,
# use the method "Image.FLIP_TOP_BOTTOM"
im_flipped.show()
print("test")