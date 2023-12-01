import pandas as pd

# Assuming your CSV file is named 'your_file.csv'
csv_file_path = '../data/top10milliondomains.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Extract the "domain" column
domains = df['Domain']

# Specify the output text file path
output_file_path = '../data/output_domains.txt'

# Write the domains to a text file
domains.to_csv(output_file_path, header=False, index=False)

print(f"Domains have been written to {output_file_path}")

