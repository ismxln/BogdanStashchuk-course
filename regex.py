import re

my_str = 'My nickname is Maxelone'

res1 = re.search('Maxelone', my_str)  # <re.Match object; span=(15, 23), match='Maxelone'>
res2 = re.search('M......e', my_str)  # <re.Match object; span=(15, 23), match='Maxelone'>

print(res1, res2)

print(re.search('^M.*name', my_str))  # <re.Match object; span=(0, 11), match='My nickname'>


def check_mail(mail):
    mail_regexp = r'[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
    mail_check_pattern = re.compile(mail_regexp)
    result = 'valid' if mail_check_pattern.fullmatch(mail) else 'not valid'
    return (mail, result)

print(check_mail('bs@gmail.com'))
print(check_mail('bsgmail.com'))
print(check_mail('bs@gmailcom'))
print(check_mail('bs@mail.com'))
print(check_mail('@gmail.com'))
print(check_mail('bs@'))