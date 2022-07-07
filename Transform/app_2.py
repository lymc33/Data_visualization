# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import base64
from PIL import Image

"""
Examples of different methods of adding local images to your Dash App
Note - Recommended to keep image files inside assets folder
- app.py
- assets/
    |-- my-image.png
"""

#Using direct image file path
image_path = '/Users/yairmartinez/Documents/GitHub/Data_visualization/Transform/assets/1_Venta_en_cantidad_por_estado.jpg'

#Using Pillow to read the the image
pil_img = Image.open('/Users/yairmartinez/Documents/GitHub/Data_visualization/Transform/assets/1_Venta_en_cantidad_por_estado.jpg')

# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard'),

    html.Img(src=image_path),                          # passing the direct file path
    html.Img(src=app.get_asset_url('assets/1_Venta_en_cantidad_por_estado.jpg')),    # usign get_asset_url function
   #html.Img(src=dash.get_asset_url('my-image.png'))    Or with newer Dash v2.2.0
    html.Img(src=pil_img),                             # using the pillow image variable
    # html.Img(src=b64_image(image_path)),               # using base64 to encode and decode the image file
])

if __name__ == "__main__":
    app.run_server()