## 🗺️ Tkinter Map with Path & Satellite View
This Python application displays an interactive map using the TkinterMapView library. It provides a GUI for visualizing geographic locations, placing markers, drawing paths, and toggling to satellite view using Google Maps tiles.
📦 Features
- Embedded map inside a Tkinter window (no browser required)
- Predefined markers for Eiffel Tower and Louvre Museum
- Button to draw a direct path between the two markers
- Button to switch tile server to satellite imagery
  
🚀 Getting Started
1. Install Dependencies
Make sure you have Python installed, then run:
pip install tkintermapview

2. Run the Application
python your_script_name.py

🧠 How It Works
- The map centers on the Eiffel Tower at startup (set_position)
- Two markers are placed using set_marker
- Clicking Draw Path connects the markers visually using set_path
- Clicking Satellite View switches to high-resolution satellite tiles using a Google Maps server:
map_widget.set_tile_server("https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", max_zoom=19)



🔧 Customization Tips
- You can replace coordinates with any other latitude/longitude pair
- Add more markers, dynamic paths, draggable interactions, or tabbed views
- For other tile styles, check out OpenStreetMap or custom providers

📁 File Structure
map_app/
├── main.py         # Main script with Tkinter GUI
└── README.md       # You’re reading it!



📍 Example Coordinates Used
| Location | Latitude | Longitude | 
| Eiffel Tower | 48.8584 | 2.2945 | 
| Louvre Museum | 48.8606 | 2.3376 | 
