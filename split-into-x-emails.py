# Escolha a quantidade de emails que serão divididos em cada arquivo
total_emails = 20
# Escolha o caminho e nome do arquivo txt que contém a lista de emails
emails_list = './datalake/unique_emails.txt'

def split_emails(file_name):
    with open(file_name, 'r') as f:
        emails = f.read().split(',\n')


    file_count = 1
    for i in range(0, len(emails), total_emails):
        with open(f'./datalake/splited/emails_LIST{file_count}_split{total_emails}.txt', 'w') as f:
            f.write(',\n'.join(emails[i:i+total_emails]))
        file_count += 1
    print(f'{file_count-1} Arquivos foram criados o total.')
    
split_emails(emails_list)