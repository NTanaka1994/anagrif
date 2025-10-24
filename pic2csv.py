import numpy as np
import pandas as pd
from PIL import Image

im = Image.open("picture.png")
height = im.convert("L")
data = np.array(height)
frame = pd.DataFrame(data)
frame.to_csv("picture.csv", index=False)