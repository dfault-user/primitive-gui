# I = INPUT FILE -- HAS TO BE A FULL PATH TO FILE
# O = OUTPUT FILE -- HAS TO BE A FULL PATH TO THE FILE TO CREATE
# N = NUMBER OF SHAPES -- HAS TO BE AN INT
# M = SHAPE MODE
# M CONTINUED ==========
# M > 0 = COMBO OF ALL
# M > 1 = ONLY TRIANGLES
# M > 2 = ONLY RECTANGLES -- SQUARES, RECTS, ETC. NO ROTATION
# M > 3 = ONLY ELLIPSES -- CIRCLES, OVALS, ETC. NO ROTATION
# M > 4 = ONLY CIRCLES
# M > 5 = ONLY ROTATED RECTANGLES
# M > 6 = ONLY BEZIER CURVES
# M > 7 = ONLY ROTATED ELLIPSES
# M > 8 = ONLY POLYGONS -- MISC SHAPES
# R = RESIZE IMAGE TO SIZE BEFORE CONTINUING -- HAS TO BE INT
# S = OUTPUT IMAGE SIZE -- HAS TO BE INT
# THOSE ARE ALL OF THE OPTIONS I'M GOING TO IMPLEMENT, REST WILL USE PRIMITIVE DEFAULTS.

# import OS to run primitive as sys command
import os
# import tkinter to construct windows
import tkinter as tk

#init window
window = tk.Tk()
#change icon
primIco = tk.PhotoImage(file = 'icon.png')
window.iconphoto(False, primIco)
#change window name
window.title('primitive-gui')

#functions
def runCommand():
    # get inputs
    inputPath = inputInput.get()
    outputPath = outputInput.get()
    numOfShapes = numShapeInput.get()
    shapeMode = modeInput.get()
    inResize = resizeInput.get()
    outResize = outSizeInput.get()
    # run command
    os.system("primitive -i " + inputPath + " -o " + outputPath + " -n " + numOfShapes + " -m " + shapeMode + " -r " + inResize + " -s " + outResize)

# main label
mainLabel = tk.Label(text="Simple GUI application for Primitive.\nDefaults are currently in the boxes.")

# create 7 frames for inputs
inputFrame = tk.Frame(master=window)
outputFrame = tk.Frame(master=window)
numShapeFrame = tk.Frame(master=window)
modeFrame = tk.Frame(master=window)
resizeFrame = tk.Frame(master=window)
outSizeFrame = tk.Frame(master=window)
submitFrame = tk.Frame(master=window)

# input file area creation
inputLabel = tk.Label(master=inputFrame,text="Input file path:\nMust be a full path or filename.")
inputInput = tk.Entry(master=inputFrame)

# output file area creation
outputLabel = tk.Label(master=outputFrame,text="Output file path:\nMust be a full path or filename.")
outputInput = tk.Entry(master=outputFrame)

# num shapes
numShapeLabel = tk.Label(master=numShapeFrame,text="Number of shapes:\nMust be number > 0")
numShapeInput = tk.Entry(master=numShapeFrame)

# mode
modeLabel = tk.Label(master=modeFrame,text="Mode:\n0 to 8")
modeInput = tk.Entry(master=modeFrame)

# resize
resizeLabel = tk.Label(master=resizeFrame,text="Resize input file to:\nMust be number > 0")
resizeInput = tk.Entry(master=resizeFrame)

# output size
outSizeLabel = tk.Label(master=outSizeFrame,text="Resize output file to:\nMust be number > 0")
outSizeInput = tk.Entry(master=outSizeFrame)

# submit
submitButton = tk.Button(master=submitFrame,text="Submit and run command",command=runCommand)

# pack frames
mainLabel.pack(fill=tk.BOTH,expand=True)
inputFrame.pack(fill=tk.BOTH,expand=True)
outputFrame.pack(fill=tk.BOTH,expand=True)
numShapeFrame.pack(fill=tk.BOTH,expand=True)
modeFrame.pack(fill=tk.BOTH,expand=True)
resizeFrame.pack(fill=tk.BOTH,expand=True)
outSizeFrame.pack(fill=tk.BOTH,expand=True)
submitFrame.pack(fill=tk.BOTH,expand=True)

# pack frame contents 
# input file
inputLabel.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
inputInput.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
# output file
outputLabel.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
outputInput.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
# num of shapes
numShapeLabel.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
numShapeInput.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
# shape mode
modeLabel.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
modeInput.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
# resize input
resizeLabel.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
resizeInput.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
# resize output
outSizeLabel.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
outSizeInput.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
# submit button
submitButton.pack(fill=tk.BOTH,expand=True)

# fill in defaults
numShapeInput.insert(0, "512") # my PERSONAL RECOMMENDED default
modeInput.insert(0, "1") # default to triangles
resizeInput.insert(0, "256") # default
outSizeInput.insert(0, "1024") # default

# initialize window
window.mainloop()