from bing_image_downloader import downloader

# List of keywords for the dataset
queries = [
    "passenger shed",
    "bus shelter",
    "waiting shed",
    "seid paisinéirí",
]

for query in queries:
    print(f"Starting download for: {query}")
    downloader.download(
        query, 
        limit=50,  # Downloads 50 images per keyword
        output_dir='Passenger_Shed_Dataset', 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60
    )

print("Download complete!")