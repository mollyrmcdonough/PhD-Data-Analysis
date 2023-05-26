import os
import csv
import re

# Directory where the text files are stored
directory = os.getcwd()

# CSV file to store the data
csv_file = "output.csv"

# Initialize the CSV file with headers
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['I[mA]', 'Nb[/cm^3]', 'u[cm^2/Vs]', 'NS[[/cm^2]'])

# Process each text file
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), 'r') as f:
            lines = f.readlines()

        # Find the lines with the data
        for line in lines:
            # Regular expression to match the desired data
            match = re.search(r'\s+([\d\.E+-]+)\s+([\d\.E+-]+)\s+[\d\.E+-]+\s+[\d\.E+-]+\s+[\d\.E+-]+\s+[\d\.E+-]+\s+([\d\.E+-]+)\s+[\d\.E+-]+\s+[\d\.E+-]+\s+[\d\.E+-]+\s+[\d\.E+-]+\s+([\d\.E+-]+)', line)

            if match:
                data = match.groups()

                # Write the data to the CSV file
                with open(csv_file, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
