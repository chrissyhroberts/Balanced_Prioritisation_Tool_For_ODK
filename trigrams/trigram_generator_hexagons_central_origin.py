import math

# User modifiable parameters
hexagon_size = 20  # Radius of the hexagons
offset_x = 34  # Horizontal offset between hexagons
offset_y = 29  # Vertical offset between rows of hexagons
central_row = 6  # Central hexagon's row index
central_col = 6  # Central hexagon's column index
central_z = -12  # Central hexagon's z index
show_labels = False  # Set to False to hide labels
label_font_size = 12  # Font size for hexagon labels
apex_font_size = 25  # Font size for apex labels
hexagon_stroke_color = "none"  # Stroke color for hexagons

# Arrow and triangle offsets
arrow_offset_x = 0  # Offset for arrows on the x-axis
arrow_offset_y = 174  # Offset for arrows on the y-axis
triangle_offset_x = 0  # Offset for the triangle on the x-axis
triangle_offset_y = 348  # Offset for the triangle on the y-axis

# Arrow length and triangle size
arrow_length = 380  # Length of the arrows
triangle_size = 370  # Size of the enclosing triangle

# Canvas settings
canvas_width = 1000  # Width of the SVG canvas (increased for extra space)
canvas_height = 800  # Height of the SVG canvas

# Define the labels and their positions for the apexes
apex_labels = {
    "apex1": {"text": "People", "x": canvas_width / 2, "y": 25},  # Top apex
    "apex2": {"text": "Animals", "x": 100, "y": 680},  # Bottom-left apex
    "apex3": {"text": "Environment", "x": 915, "y": 680}  # Bottom-right apex
}

# Function to create a single hexagon path
def hexagon_path(cx, cy, size):
    points = []
    for i in range(6):
        angle = math.radians(60 * i + 30)  # Rotate the hexagon by 30 degrees
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        points.append(f"{x},{y}")
    return f"M{points[0]} " + " ".join([f"L{p}" for p in points[1:]]) + " Z"

# Function to create an arrow path
def arrow_path(x1, y1, length, angle):
    angle_rad = math.radians(angle)
    x2 = x1 + length * math.cos(angle_rad)
    y2 = y1 + length * math.sin(angle_rad)
    return f"M{x1},{y1} L{x2},{y2}"

svg_content = []

# Define the arrowhead marker
arrowhead_marker = """
<defs>
  <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="red" />
  </marker>
</defs>
"""

# Now loop through rows to create the hexagon paths, ensuring they are drawn first
id_counter = 1
for row in range(19):
    num_hexagons = row + 1
    for col in range(num_hexagons):
        cx = canvas_width / 2 + col * offset_x - (row * offset_x / 2)
        cy = 100 + row * offset_y

        # Calculate the coordinates relative to the central point (6, 6, -12)
        x = col - central_col
        y = (row - col) - central_row
        z = -(row) - central_z

        # Check if this hexagon is the central one (i.e., coordinates are (0, 0, 0))
        if x == 0 and y == 0 and z == 0:
            fill_color = "#808080"  # Grey color for the central hexagon
        else:
            fill_color = "none"  # Grey for other hexagons
        
        label = f"{x}_{y}_{z}"  # Label based on distance from the central point

        path_d = hexagon_path(cx, cy, hexagon_size)
        svg_content.append(f'<path id="{label}" d="{path_d}" fill="{fill_color}" stroke="{hexagon_stroke_color}" stroke-width="2" pointer-events="all"/>\n')
        
        # Add label if the flag is set to True
        if show_labels:
            svg_content.append(f'<text x="{cx}" y="{cy + 2}" font-family="Verdana" font-size="{label_font_size}" fill="black" text-anchor="middle" alignment-baseline="middle">{label}</text>\n')
        
        id_counter += 1

# Add the straight-edged triangle around the perimeter
start_x = canvas_width / 2
start_y = 100  # Starting y position remains the same

triangle_points = [
    (start_x + triangle_offset_x, start_y - triangle_size + triangle_offset_y),  # Top
    (start_x - triangle_size * math.sin(math.radians(60)) + triangle_offset_x, start_y + triangle_size * math.cos(math.radians(60)) + triangle_offset_y),  # Bottom-left
    (start_x + triangle_size * math.sin(math.radians(60)) + triangle_offset_x, start_y + triangle_size * math.cos(math.radians(60)) + triangle_offset_y)  # Bottom-right
]
triangle_d = f"M{triangle_points[0][0]},{triangle_points[0][1]} " + " ".join([f"L{p[0]},{p[1]}" for p in triangle_points[1:]]) + " Z"
svg_content.append(f'<path d="{triangle_d}" fill="none" stroke="black" stroke-width="3" pointer-events="none"/>\n')

# Add the three red arrows radiating from the central point
arrow_start_x = start_x + arrow_offset_x
arrow_start_y = start_y + 6 * offset_y + arrow_offset_y
arrows = [
    arrow_path(arrow_start_x, arrow_start_y, arrow_length, 270),  # Upwards
    arrow_path(arrow_start_x, arrow_start_y, arrow_length, 30),   # Down-right
    arrow_path(arrow_start_x, arrow_start_y, arrow_length, 150)   # Down-left
]

# Add arrow paths with arrowheads
for arrow_d in arrows:
    svg_content.append(f'<path d="{arrow_d}" stroke="red" stroke-width="3" marker-end="url(#arrowhead)" pointer-events="none"/>\n')

# Add the labels at the apexes using the defined positions
for apex in apex_labels.values():
    svg_content.append(f'<text x="{apex["x"]}" y="{apex["y"]}" font-family="Verdana" font-size="{apex_font_size}" fill="black" text-anchor="middle">{apex["text"]}</text>\n')

# Combine the SVG content into a complete SVG file structure
full_svg = f"""
<svg width="{canvas_width}" height="{canvas_height}" xmlns="http://www.w3.org/2000/svg">
  <title>Hexagon Triangle</title>
  {arrowhead_marker}
  <g>
    <title>Layer 1</title>
    {''.join(svg_content)}
  </g>
</svg>
"""

# Save the SVG content to a file
with open("hexagon.svg", "w") as file:
    file.write(full_svg)

"hexagon.svg"
