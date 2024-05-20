# Escolha o caminho e nome do arquivo txt que contém a lista de emails
emails_list = './datalake/emails_processed.txt'

def remove_duplicates(file_name):
    with open(file_name, 'r') as f:
        emails = f.read().split(',\n')

    unique_emails = set(emails)
    duplicates = len(emails) - len(unique_emails)

    with open('./datalake/unique_emails.txt', 'w') as f:
        f.write(',\n'.join(unique_emails))

    print(f'{duplicates} emails duplicados foram removidos.')

# Use a função
remove_duplicates(emails_list)