import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO




def generate_plots(n=None):
    # Directory containing JSON files
    directory = "data"
    # Initialize dictionaries to hold data for each field
    data = {
        "total_documents_processed": [],
        "textMessages": [],
        "forwarded_messages": [],
        "images": [],
        "videos": [],
        "audios": [],       
        "links": [],      
        "timestamps": []
    }

    # Read all JSON files from the directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".json"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                # Convert current_date and current_time to a datetime object
                timestamp = f"{json_data['current_date']} {json_data['current_time'].split()[-1]}"
                datetime_obj = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                # Append the data to respective lists
                data["timestamps"].append(datetime_obj)
                data["audios"].append(json_data["audios"])
                data["images"].append(json_data["images"])
                data["links"].append(json_data["links"])
                data["forwarded_messages"].append(json_data["messages"])
                data["textMessages"].append(json_data["textMessages"])
                data["total_documents_processed"].append(json_data["total_documents_processed"])
                data["videos"].append(json_data["videos"])

    # Sort the data by timestamps
    sorted_indices = sorted(range(len(data["timestamps"])), key=lambda i: data["timestamps"][i])
    for key in data:
        data[key] = [data[key][i] for i in sorted_indices]

    # Slice data to get the last n points if n is provided
    if n:
        for key in data:
            data[key] = data[key][-n:]

    # List of fields to plot
    fields = ["audios", "images", "links", "forwarded_messages", "textMessages", "total_documents_processed", "videos"]

    images = []
    # Create plots for each field
    for field in fields:
        plt.figure(figsize=(10, 6))
        plt.plot(data["timestamps"], data[field], marker='o', linestyle='-')
        plt.title(f"{field.capitalize()} Over Time")
        plt.xlabel("Time")
        plt.ylabel(field.capitalize())
        plt.grid(True)
        plt.tight_layout()

        # Save the plot to a BytesIO object
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        images.append(img_buffer)

        # Clear the plot
        plt.close()

    return images

# # Example Usage
# # Without argument, plots for all data points
# all_plots = generate_plots()
# print(f"Generated {len(all_plots)} plots for all data points")

# # With argument, plots for last 5 data points
# last_5_plots = generate_plots(n=5)
# print(f"Generated {len(last_5_plots)} plots for the last 5 data points")


# generate_table(n=10)