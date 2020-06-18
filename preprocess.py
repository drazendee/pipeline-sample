print("such preprocess, so wow")

f= open("/valohai/outputs/images.txt","w+")
for i in range(10):
     f.write("Images is line %d\r\n" % (i+1))
f.close()

f= open("/valohai/outputs/labels.txt","w+")
for i in range(10):
     f.write("Labels is line %d\r\n" % (i+1))
f.close()
