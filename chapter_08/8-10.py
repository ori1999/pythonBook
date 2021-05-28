messages = ['a', 'b', 'c']
sent_message = []


def show_message(messages):
    for message in messages:
        print(message)


def send_message(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_message.append(current_message)


# show_message(messages)
print(messages)
send_message(messages)
print(sent_message)
