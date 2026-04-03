class Message:
    def __init__(self, content, receiver):
        self.content = content
        self.receiver = receiver

    def __str__(self):
        return f"{self.content}"
    

class UserGroup:
    def __init__(self, name, send_messages, message_limit, pinning_messages):
        self.name = name
        self.send_messages = send_messages
        self.message_limit = message_limit
        self.pinning_messages = pinning_messages

        def __str__(self):
            output = f"{self.name} User Group:\n"
            output += f"Send Messages: {self.send_messages}\n"
            output += f"Message Limit: {self.message_limit}\n"
            output += f"Pinning Messages: {self.pinning_messages}"
            return output


class User:
    def __init__(self, id, group):
        self.id = id
        self.group = group
        self._message_count = 0
        self._received_messages = []
        self._pinned_messages = []

    @property
    def received_messages(self):
        return self._received_messages

    @property
    def pinned_messages(self):
        return self._pinned_messages

    def send_message(self, recipient, message):
        if self.group.send_messages:
            if self.group.message_limit == "Unlimited" or len(self.received_messages) < self.group.message_limit:
                recipient.receive_message(self, message)
                self._message_count += 1

    def receive_message(self, sender, message):
        self.received_messages.append(message)

    def delete_message(self, message):
        if message in self.received_messages:
            self.received_messages.remove(message)

    def pin_message(self, message):
        if message not in self.pinned_messages:
            self.pinned_messages.append(message)
            self.received_messages.remove(message)

    def unpin_message(self, message):
        if message in self.pinned_messages:
            self.pinned_messages.remove(message)
            self.received_messages.append(message)

    def __str__(self):
        output = f"{self.id}:\n"
        output += f"Group: {self.group.name}\n"
        output += "Pinned Messages:\n"
        for message in self.pinned_messages:
            output += f"{message}\n"
        output += "Received Messages:\n"
        for message in self.received_messages:
            output += f"{message}\n"

        return output


def test_discord():
    unverified = UserGroup("Unverified", False, 0, False)
    verified = UserGroup("Verified", True, 100, False)
    nitro = UserGroup("Nitro", True, "Unlimited", True)

    user1 = User("user1", unverified)
    user2 = User("user2", verified)
    user3 = User("user3", nitro)

    message1 = Message("Hello, user2!", user3)
    message2 = Message("Hi, user2!", user1)
    message3 = Message("Welcome to the server! (To User 1)", user1)

    user2.send_message(user2, message1)
    user2.send_message(user2, message2)
    user3.send_message(user1, message3)

    print(user1)
    print(user2)
    print(user3)

    user2.pin_message(message1)

    print(user1)
    print(user2)
    print(user3)

test_discord()

