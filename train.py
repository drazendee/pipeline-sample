print("training so much")

f=open("/valohai/inputs/dataset-images/images.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)

f=open("/valohai/inputs/dataset-labels/labels.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)