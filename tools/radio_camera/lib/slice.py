# Function to extract a 2D slice based on the specified dimension and index
def extract_2d_slice(three_d_array, dimension, index):
    if dimension == "x":
        # Extracting a 2D slice for the specific x value
        return three_d_array[index]
    elif dimension == "y":
        # Extracting a 2D slice for the specific y value
        return [
            [three_d_array[x][index][z] for z in range(len(three_d_array[0][0]))]
            for x in range(len(three_d_array))
        ]
    elif dimension == "z":
        # Extracting a 2D slice for the specific z value
        return [
            [three_d_array[x][y][index] for y in range(len(three_d_array[0]))]
            for x in range(len(three_d_array))
        ]
    else:
        raise ValueError("Invalid dimension! Choose from 'x', 'y', or 'z'.")
