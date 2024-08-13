def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    list_ = [ ".com", ".ru", ".net"]
    count = 0
    if "@" not in sender or "@" not in recipient:
        print('Ошибка в записи почты, отсутствует знак @')
        return
    for i in list_:
        if i in sender:
            count += 1
        if i in recipient:
            count += 1
    if sender == recipient:
        print('Нельзя отправлять письма самому себе')
        return
    if count >= 2:
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient)
        else:
            print(f"Нестандартный отправитель! Письмо отправлено с адреса ", sender, " на адрес ", recipient)
    else:
        print(f"Письмо невозможно отправить с адреса ", sender, " на адрес ", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
