# 3D Scatter Plot

This project generates a 3D scatter plot using random (or real) data and automatically saves the image in a folder with sequential filenames. The code uses Python, Matplotlib, and Numpy.

## Project Structure

* `main.py`: Main script for generating and visualizing the plot.
* `utils.py`: Utility function for saving plots with sequential names.
* `Dispersão PNGs/`: Folder where the generated plots are automatically saved.

## How to Use

1. **Install dependencies**:

   ```sh
   pip install matplotlib numpy
   ```

2. **Run the main script**:

   ```sh
   python main.py
   ```

3. The plot will be displayed on screen and automatically saved in the `Gráficos/` folder with a sequential name like `grafico_1_3d_teste.png`, `grafico_2_3d_teste.png`, etc.

## Customization

* To use your own data, replace the `x`, `y`, `z` arrays in [`main.py`](main.py).
* To change the output directory or filename prefix, edit the call to the [`salvar_grafico_sequencial`](utils.py) function in [`main.py`](main.py).

## Credits

Developed for study and visualization purposes.
