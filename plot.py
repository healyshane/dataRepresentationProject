import pandas as pd
import matplotlib.pyplot as plt
import io
from batchDAO import batchDAO

def do_plot():
    # Loading 
    results = batchDAO.getAll()


    df = pd.DataFrame(results)
    
    df.plot(x = "id",y=["yield","time"], kind ="bar", title="Yield/Time per Batch")
 

    # attempting to save figure as bytes object and expose with FLASK
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image