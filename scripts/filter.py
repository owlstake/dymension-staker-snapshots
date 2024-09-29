import csv

# Set the voting power threshold (can be modified as needed)
voting_power = 100

# Function to filter rows with "delegated dym" less than voting_power and save them to a new CSV file
def filter_and_save_delegated_dym(input_file_path, output_file_path, voting_power):
    # Open the input CSV file for reading
    with open(input_file_path, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # Open the output CSV file for writing filtered data
        with open(output_file_path, mode='w', newline='') as csvoutfile:
            fieldnames = csvreader.fieldnames  # Get the field names (header) from the input file
            csvwriter = csv.DictWriter(csvoutfile, fieldnames=fieldnames)
            
            # Write the header (column names) to the new CSV file
            csvwriter.writeheader()
            
            # Iterate over each row in the input CSV file
            for row in csvreader:
                # Convert the "delegated dym" value to a float for comparison
                delegated_dym = float(row['delegated dym'])
                
                # If "delegated dym" is less than the voting power threshold, write the row to the new file
                if delegated_dym < voting_power:
                    csvwriter.writerow(row)

# Input CSV file path and output CSV file path
input_file_path = 'delegators.csv'
output_file_path = 'filtered_delegators.csv'

# Call the function to filter rows and save them to the new CSV file
filter_and_save_delegated_dym(input_file_path, output_file_path, voting_power)
