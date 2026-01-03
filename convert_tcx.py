import os
import glob
import xml.etree.ElementTree as ET

def tcx_to_gpx(directory='gpx'):
    tcx_files = glob.glob(os.path.join(directory, '*.tcx'))
    
    if not tcx_files:
        print("No .tcx files found!")
        return

    print(f"Found {len(tcx_files)} TCX files. Adding timestamps...")
    ns = {'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}

    for tcx_path in tcx_files:
        try:
            tree = ET.parse(tcx_path)
            root = tree.getroot()
            
            # Start GPX with a global time tag for the file
            gpx_content = [
                '<?xml version="1.0" encoding="UTF-8"?>',
                '<gpx version="1.1" creator="StravaHeatmapConverter">',
                '<metadata><time>2023-01-01T00:00:00Z</time></metadata>',
                '<trk><trkseg>'
            ]
            
            has_points = False
            for point in root.findall('.//ns:Trackpoint', ns):
                pos = point.find('ns:Position', ns)
                time_node = point.find('ns:Time', ns)
                
                if pos is not None:
                    lat = pos.find('ns:LatitudeDegrees', ns).text
                    lon = pos.find('ns:LongitudeDegrees', ns).text
                    # Use actual time if exists, otherwise use dummy
                    time_val = time_node.text if time_node is not None else "2023-01-01T00:00:00Z"
                    
                    gpx_content.append(f'<trkpt lat="{lat}" lon="{lon}"><time>{time_val}</time></trkpt>')
                    has_points = True
            
            gpx_content.append('</trkseg></trk></gpx>')
            
            if has_points:
                gpx_filename = tcx_path.replace('.tcx', '.gpx')
                with open(gpx_filename, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(gpx_content))
        except Exception as e:
            print(f"Error: {e}")

    print("--- Done! Try running the heatmap script now. ---")

if __name__ == '__main__':
    tcx_to_gpx()