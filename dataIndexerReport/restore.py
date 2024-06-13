import json
import os
from datetime import datetime

# Example list of JSON structures
json_list = [
    {
        "audios": 11669,
        "current_date": "2024-06-12",
        "current_time": "Wednesday, June 12, 2024 13:27:25",
        "images": 1676067,
        "links": 465661,
        "messages": 44358,
        "textMessages": 2079162,
        "total_documents_processed": 4514915,
        "videos": 237998
    },
    {
    "audios": 11615,
    "current_date": "2024-06-10",
    "current_time": "Monday, June 10, 2024 06:47:07",
    "images": 1687751,
    "links": 463764,
    "messages": 44708,
    "textMessages": 2063730,
    "total_documents_processed": 4511771,
    "videos": 240203
    },
    {
    "audios": 11551,
    "current_date": "2024-06-09",
    "current_time": "Sunday, June 9, 2024 06:39:50",
    "images": 1678548,
    "links": 463107,
    "messages": 44533,
    "textMessages": 2055977,
    "total_documents_processed": 4492953,
    "videos": 239237
    },
    {
    "audios": 11431,
    "current_date": "2024-06-08",
    "current_time": "Saturday, June 8, 2024 06:55:48",
    "images": 1657747,
    "links": 462343,
    "messages": 44082,
    "textMessages": 2046026,
    "total_documents_processed": 4457705,
    "videos": 236076
    },
    {
    "audios": 11317,
    "current_date": "2024-06-07",
    "current_time": "Friday, June 7, 2024 06:55:46",
    "images": 1626905,
    "links": 459004,
    "messages": 43266,
    "textMessages": 2004676,
    "total_documents_processed": 4376708,
    "videos": 231540
    },
    {
    "audios": 11357,
    "current_date": "2024-06-06",
    "current_time": "Thursday, June 6, 2024 15:01:05",
    "images": 1607141,
    "links": 458299,
    "messages": 42984,
    "textMessages": 2008344,
    "total_documents_processed": 4360282,
    "videos": 232157
    },
    {
    "audios": 11279,
    "current_date": "2024-06-05",
    "current_time": "Wednesday, June 5, 2024 12:41:33",
    "images": 1615486,
    "links": 455364,
    "messages": 42462,
    "textMessages": 1985148,
    "total_documents_processed": 4339108,
    "videos": 229369
    },
    {
    "audios": 11160,
    "current_date": "2024-06-04",
    "current_time": "Tuesday, June 4, 2024 15:28:06",
    "images": 1616278,
    "links": 456017,
    "messages": 42622,
    "textMessages": 1980573,
    "total_documents_processed": 4338304,
    "videos": 231654
    },
    {
    "audios": 10998,
    "current_date": "2024-06-03",
    "current_time": "Monday, June 3, 2024 13:10:28",
    "images": 1592279,
    "links": 452765,
    "messages": 41501,
    "textMessages": 1956977,
    "total_documents_processed": 4280331,
    "videos": 225811
    },
    {
    "audios": 10998,
    "current_date": "2024-06-02",
    "current_time": "Sunday, June 2, 2024 21:00:23",
    "images": 1592279,
    "links": 452765,
    "messages": 41501,
    "textMessages": 1956977,
    "total_documents_processed": 4280331,
    "videos": 225811
    },
    {
    "audios": 10842,
    "current_date": "2024-06-01",
    "current_time": "Saturday, June 1, 2024 14:13:32",
    "images": 1601062,
    "links": 450307,
    "messages": 41819,
    "textMessages": 1940123,
    "total_documents_processed": 4270250,
    "videos": 226097
    },
    {
    "audios": 10731,
    "current_date": "2024-05-31",
    "current_time": "Friday, May 31, 2024 16:57:39",
    "images": 1565371,
    "links": 447954,
    "messages": 40934,
    "textMessages": 1913301,
    "total_documents_processed": 4200353,
    "videos": 222062
    },
    {
    "audios": 9818,
    "current_date": "2024-05-30",
    "current_time": "Thursday, May 30, 2024 15:16:19",
    "images": 1538907,
    "links": 441381,
    "messages": 40067,
    "textMessages": 1868254,
    "total_documents_processed": 4114484,
    "videos": 216057
    },
    {
    "audios": 9818,
    "current_date": "2024-05-30",
    "current_time": "Thursday, May 30, 2024 14:18:12",
    "images": 1538907,
    "links": 441381,
    "messages": 40067,
    "textMessages": 1868254,
    "total_documents_processed": 4114484,
    "videos": 216057
    },
    {
    "audios": 9818,
    "current_date": "2024-05-30",
    "current_time": "Thursday, May 30, 2024 03:06:27",
    "images": 1538907,
    "links": 441381,
    "messages": 40067,
    "textMessages": 1868254,
    "total_documents_processed": 4114484,
    "videos": 216057
    },
    {
    "audios": 10402,
    "current_date": "2024-05-28",
    "current_time": "Tuesday, May 28, 2024 15:47:27",
    "images": 1545103,
    "links": 442505,
    "messages": 42348,
    "textMessages": 1861641,
    "total_documents_processed": 4133288,
    "videos": 231289
    },
    {
    "audios": 10395,
    "current_date": "2024-05-28",
    "current_time": "Tuesday, May 28, 2024 11:36:27",
    "images": 1542995,
    "links": 442135,
    "messages": 42299,
    "textMessages": 1856573,
    "total_documents_processed": 4125274,
    "videos": 230877
    },
    {
    "audios": 10010,
    "current_date": "2024-05-24",
    "current_time": "Friday, May 24, 2024 04:52:11",
    "images": 1535722,
    "links": 432960,
    "messages": 40706,
    "textMessages": 1809678,
    "total_documents_processed": 4046481,
    "videos": 217405
    },
    {
    "audios": 10010,
    "current_date": "2024-05-23",
    "current_time": "Thursday, May 23, 2024 01:41:03",
    "images": 1535267,
    "links": 432929,
    "messages": 40707,
    "textMessages": 1809572,
    "total_documents_processed": 4045874,
    "videos": 217389
    },
    {
    "audios": 10003,
    "current_date": "2024-05-22",
    "current_time": "Wednesday, May 22, 2024 15:09:47",
    "images": 1530605,
    "links": 432191,
    "messages": 22293,
    "textMessages": 1808117,
    "total_documents_processed": 3803209,
    "videos": 0
    },
    {
    "audios": 10003,
    "current_date": "2024-05-22",
    "current_time": "Wednesday, May 22, 2024 00:01:23",
    "images": 1530605,
    "links": 432191,
    "messages": 22293,
    "textMessages": 1808117,
    "total_documents_processed": 3803209,
    "videos": 0
    },
    {
    "audios": 10007,
    "current_date": "2024-05-21",
    "current_time": "Tuesday, May 21, 2024 16:10:24",
    "images": 1535491,
    "links": 433055,
    "messages": 22323,
    "textMessages": 1809852,
    "total_documents_processed": 3810728,
    "videos": 0
    },
    {
    "audios": 10007,
    "current_date": "2024-05-21",
    "current_time": "Tuesday, May 21, 2024 13:02:19",
    "images": 1535491,
    "links": 433055,
    "messages": 22323,
    "textMessages": 1809852,
    "total_documents_processed": 3810728,
    "videos": 0
    },
    {
    "audios": 9877,
    "current_date": "2024-05-20",
    "current_time": "Monday, May 20, 2024 12:02:01",
    "images": 1505320,
    "links": 430027,
    "messages": 39155,
    "textMessages": 1793259,
    "total_documents_processed": 3988780,
    "videos": 211142
    },
    {
    "audios": 9877,
    "current_date": "2024-05-20",
    "current_time": "Monday, May 20, 2024 04:21:16",
    "images": 1505320,
    "links": 430027,
    "messages": 39155,
    "textMessages": 1793259,
    "total_documents_processed": 3988780,
    "videos": 211142
    }
    # Add more JSON objects as needed
]

# Define directory to save files
directory = "data"

# Create directory if not exists
os.makedirs(directory, exist_ok=True)

# Iterate over each JSON object
for json_data in json_list:
    current_date = json_data["current_date"]
    current_time = json_data["current_time"].split()[-1]  # Get only the HH:MM:SS part
    timestamp = f"{current_date}_{current_time.replace(':', '-')}"
    file_name = f"json_{timestamp}.json"
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
    print(f"JSON saved to {file_path}")
