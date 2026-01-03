# strava_local_heatmap.py

Python script to reproduce the Strava Global Heatmap ([www.strava.com/heatmap](https://www.strava.com/heatmap)) with local GPX files

Optimized for cycling activities :bicyclist:

## Features

* Minimal Python dependencies (`numpy`+`matplotlib`)
* Fast (parse 3x faster than `gpxpy.parse`)

## Usage

* Export your activities from Strava (they are commonly provided as `.tcx.gz`) and place them in the `gpx` folder. (https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#h_01GG58HC4F1BGQ9PQZZVANN6WF)
* If your export contains `.tcx.gz` files, use the included converter to generate GPX files with timestamps:

```bash
python convert_tcx.py         # converts both .tcx and .tcx.gz files found in `gpx/`
```

* Alternatively, you can manually uncompress your TCX files (Linux/macOS):

```bash
gunzip gpx/*.tcx.gz
```

* Install the Python dependencies from `requirements.txt`.
* Run `python strava_local_heatmap.py` to generate a heatmap.

> **Important:** Do **not** commit personal activity data (the `gpx/` folder or any `.tcx`/`.tcx.gz` files), downloaded map tiles (`tiles/`), or generated heatmap images (`*.png`) to your public repository — the `.gitignore` already excludes these files to avoid leaking private data.

### Command-line options

```
usage: strava_local_heatmap.py [-h] [--dir DIR] [--filter FILTER] [--year YEAR [YEAR ...]]
                               [--bounds BOUND BOUND BOUND BOUND] [--output OUTPUT] [--zoom ZOOM] [--sigma SIGMA]
                               [--orange] [--csv]

optional arguments:
  -h, --help            show this help message and exit
  --dir DIR             GPX files directory (default: gpx)
  --filter FILTER       GPX files glob filter (default: *.gpx)
  --year YEAR [YEAR ...]
                        GPX files year(s) filter (default: all)
  --bounds BOUND BOUND BOUND BOUND
                        heatmap bounding box as lat_min, lat_max, lon_min, lon_max (default: -90 +90 -180 +180)
  --output OUTPUT       heatmap name (default: heatmap.png)
  --zoom ZOOM           heatmap zoom level 0-19 or -1 for auto (default: -1)
  --sigma SIGMA         heatmap Gaussian kernel sigma in pixel (default: 1)
  --orange              not a heatmap...
  --csv                 also save the heatmap data to a CSV file
```

Note: `ZOOM` is OpenStreetMap zoom level (the number following `map=` in [www.openstreetmap.org/#map=](https://www.openstreetmap.org))

On the use of histogram equalization: [https://medium.com/strava-engineering/the-global-heatmap-now-6x-hotter](https://medium.com/strava-engineering/the-global-heatmap-now-6x-hotter-23fc01d301de)

## Examples

command|output
-------|------
`strava_local_heatmap.py`|![heatmap.png](images/heatmap.png)
`strava_local_heatmap.py --orange`|![orange.png](images/orange.png)
`strava_local_heatmap.py --csv`|See https://umap.openstreetmap.fr/en/map/demo-heatmap_261644 (by [@badele](https://github.com/badele))

## Projects using strava_local_heatmap.py

[JeSuisUnDesDeux](https://gitlab.com/JeSuisUnDesDeux/jesuisundesdeux/tree/master/datas/traces)

## Troubleshooting

Arch Linux: `sudo pacman -S tk` (see [here](https://github.com/remisalmon/strava-local-heatmap/pull/3#issuecomment-443541311))
