class Data:
    ListInstantSpeed = []
    MaxSpeed = 0
    checkbox = checkbox_read()

    def checkbox_read():
        fp = open("checkbox.txt", "r")
        global checkbox = True

    def checkbox_write():
        fp.write( str(img_sobel_x[y,x]) + " " + str(img_sobel_y[y,x]) + "\n")
