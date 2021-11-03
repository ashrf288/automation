import  re


reg_num = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)', re.VERBOSE)

reg_mail = re.compile(r'([a-zA-Z0-9._%+-]+ @[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))', re.VERBOSE)


with open('potential-contacts.txt', 'r') as f:
    text = f.read().replace('\n', '')


phones = []
emails = []

for i in reg_num.findall(text):
    phone_num = '-'.join([i[1], i[3], i[5]])
    phone_num = re.sub(r'[(|)]','', phone_num)
    if phone_num not in phones:
        phones.append(phone_num)
for i in reg_mail.findall(text):
    if i[0] not in emails:
        emails.append(i[0])

phones.sort()
emails.sort()

with open("phone_numbers.txt","w") as f:
    for element in phones:
     f.write(element + "\n")

with open("emails.txt","w") as f:
    for element in emails:
     f.write(element + "\n")

