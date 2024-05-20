import csv

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        emails = f.readlines()

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Email'])
        for email in emails:
            writer.writerow([email.strip()])
    print('Arquivo emails.csv criado na pasta /datalake.')
convert_to_csv('./datalake/unique_emails.txt', './datalake/emails.csv')
