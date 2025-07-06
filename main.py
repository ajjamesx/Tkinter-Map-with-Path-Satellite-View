import tkinter as tk
from tkintermapview import TkinterMapView

# Create main window
root = tk.Tk()
root.geometry("800x600")
root.title("Tkinter Map with Path & Satellite View")

# Create map widget
map_widget = TkinterMapView(root, width=800, height=500, corner_radius=0)
map_widget.pack(pady=10)

# Set initial position and zoom
map_widget.set_position(48.8584, 2.2945)  # Eiffel Tower
map_widget.set_zoom(15)

# Add markers
marker1 = map_widget.set_marker(48.8584, 2.2945, text="Eiffel Tower")
marker2 = map_widget.set_marker(48.8606, 2.3376, text="Louvre Museum")

# Draw path between markers
def draw_path():
    path = map_widget.set_path([
        (marker1.position[0], marker1.position[1]),
        (marker2.position[0], marker2.position[1])
    ])
    print("Path drawn between markers.")

# Toggle satellite view
def toggle_satellite():
    map_widget.set_tile_server(
        "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
        max_zoom=19
    )
    print("Satellite view enabled.")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

draw_btn = tk.Button(btn_frame, text="Draw Path", command=draw_path)
draw_btn.pack(side="left", padx=10)

satellite_btn = tk.Button(btn_frame, text="Satellite View", command=toggle_satellite)
satellite_btn.pack(side="left", padx=10)

root.mainloop()