# Instructions to generate visualizations of the same images with changing cMAP values

1. Make sure the python enviorment is installed with matplotlib and pillow. If not, run the following command in your environment:
```
pip install matplotlib==3.5.2
pip install pillow==10.2.0
```

2. Run the following command to generate the visualization:

```python visualize_cmap.py```

The visualization image will be generated at `visualization_cMAP.png`.

In each row of the visualization, we visualize the original image and anonymized images of different cMAP values. The images are from VISPR dataset. *Lower cMAP values indicates better privacy preservation performance*.