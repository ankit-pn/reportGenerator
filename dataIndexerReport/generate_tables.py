import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO


def transpose(matrix):
    # Assuming matrix is a list of lists
    if not matrix:
        return []
    
    # Dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize a new matrix for the transpose
    transpose_matrix = [[0]*rows for _ in range(cols)]
    
    # Compute transpose
    for i in range(rows):
        for j in range(cols):
            transpose_matrix[j][i] = matrix[i][j]
    
    return transpose_matrix

def generate_table_list(data):
    table = []
    for key in data:
        temp = [key]
        temp.extend(data[key])
        table.append(temp)
    
    print(table)
    
    resultant_table = transpose(table)
    # print(resultant_table)
    return resultant_table


def generate_table(n=None):
    directory = "data"
    data = {
        "timestamps": [],
        "total_documents_processed": [],
        "textMessages": [],
        "forwared_messages": [],
        "images": [],
        "videos": [],
        "audios": [],  
        "links": [] 
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
                # datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
                data["timestamps"].append(datetime_obj)
                data["audios"].append(json_data["audios"])
                data["images"].append(json_data["images"])
                data["links"].append(json_data["links"])
                data["forwared_messages"].append(json_data["messages"])
                data["textMessages"].append(json_data["textMessages"])
                data["total_documents_processed"].append(json_data["total_documents_processed"])
                data["videos"].append(json_data["videos"])

    # Sort the data by timestamps
    sorted_indices = sorted(range(len(data["timestamps"])), key=lambda i: data["timestamps"][i])
    for key in data:
        data[key] = [data[key][i] for i in sorted_indices]
        # print(key," ",data[key])
        # if key == "timestamps":
        #     data[key]=data[key].strftime("%Y-%m-%d %H:%M:%S")
    
     # Slice data to get the last n points if n is provided
    if n:
        for key in data:
            data[key] = data[key][-n:]


    return generate_table_list(data)




def generate_increase_table(n=None):
    directory = "data"
    data = {
        "timestamps": [],
        "total_documents_processed": [],
        "textMessages": [],
        "forwared_messages": [],
        "images": [],
        "videos": [],
        "audios": [],  
        "links": [] 
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
                data["forwared_messages"].append(json_data["messages"])
                data["textMessages"].append(json_data["textMessages"])
                data["total_documents_processed"].append(json_data["total_documents_processed"])
                data["videos"].append(json_data["videos"])

    # Sort the data by timestamps
    sorted_indices = sorted(range(len(data["timestamps"])), key=lambda i: data["timestamps"][i])
    for key in data:
        data[key] = [data[key][i] for i in sorted_indices]

    # Calculate increases at each timestamp
    increase_data = {
        "timestamps": data["timestamps"],
        "total_documents_processed_increase": [],
        "textMessages_increase": [],
        "forwared_messages_increase": [],
        "images_increase": [],
        "videos_increase": [],
        "audios_increase": [],  
        "links_increase": [] 
    }

    for i in range(len(data["timestamps"])):
        if i == 0:
            # No increase to calculate for the first timestamp
            continue
        else:
            increase_data["total_documents_processed_increase"].append(data["total_documents_processed"][i] - data["total_documents_processed"][i-1])
            increase_data["textMessages_increase"].append(data["textMessages"][i] - data["textMessages"][i-1])
            increase_data["forwared_messages_increase"].append(data["forwared_messages"][i] - data["forwared_messages"][i-1])
            increase_data["images_increase"].append(data["images"][i] - data["images"][i-1])
            increase_data["videos_increase"].append(data["videos"][i] - data["videos"][i-1])
            increase_data["audios_increase"].append(data["audios"][i] - data["audios"][i-1])
            increase_data["links_increase"].append(data["links"][i] - data["links"][i-1])

    if n:
        for key in increase_data:
            increase_data[key] = increase_data[key][-n:]

    return generate_table_list(increase_data)