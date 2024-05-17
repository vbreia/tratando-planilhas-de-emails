import csv

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        emails = f.readlines()

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Email'])
        for email in emails:
            writer.writerow([email.strip()])

convert_to_csv('./datalake/emails_processed.txt', './datalake/emails.csv')
