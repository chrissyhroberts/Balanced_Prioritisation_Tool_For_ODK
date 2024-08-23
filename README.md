# ODK_image_maps
A bunch of SVG files for use in trigram, digram and other image_maps

## Balanced Prioritisation Tool / Ternary decision allocator

This tool, found in the /tda folder includes a customisable python script which creates an SVG for image-map type questions in ODK Ecosystem platforms.

The script creates a ternary diagram with three variables. The main triangle consists of a 19x19 hexagonal map.
In ODK, the hexagons (which are painted transparently in SVG) become clickable and are mapped to a co-ordinate system which measures the triangular distance from the central hexagon. 

The coordinates are a Hamming distance metric, so the furthest extreme corners are 12 edges away from the central point.

The topmost apex is then the three vertexes are at 

top   :  -6,-6,12
left  :  -6,12,-6
right :  12,-6,-6

As you can see, a higher value in one vertex is associated with a lower score in the other two dimensions.
This means that the scores on each 'axis' are not numerically important per se, but rather that the relationships between the numbers mean something
It also provides for a pretty easy to understand visual device

https://github.com/user-attachments/assets/551da741-6dda-4a41-8d1c-3434fce3ae3e

