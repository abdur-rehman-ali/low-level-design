from abc import ABC, abstractmethod

class Publisher(ABC):
    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class Subscriber(ABC):
    @abstractmethod
    def update(self, message):
        pass

class NewsPublisher(Publisher):
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)

class EmailSubscriber(Subscriber):
    def __init__(self, email):
        self._email = email

    def update(self, message):
        print(f"Email sent to {self._email}: {message}")


if __name__ == "__main__":
    news_publisher = NewsPublisher()

    subscriber1 = EmailSubscriber("user1@example.com")
    subscriber2 = EmailSubscriber("user2@example.com")

    news_publisher.subscribe(subscriber1)
    news_publisher.subscribe(subscriber2)

    news_publisher.notify("Breaking news: Python 4.0 is released!")

