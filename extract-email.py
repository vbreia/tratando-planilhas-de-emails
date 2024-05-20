import re

def process_emails(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()

    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

    emails_formatted = ',\n'.join(emails)

    with open(output_file, 'w') as f:
        f.write(emails_formatted)
print(f'Todos os e-mails do arquivo foram obtidos\nArquivo emails_formated.txt criado na pasta /datalake.')
process_emails('emails.txt', './datalake/emails_processed.txt')
