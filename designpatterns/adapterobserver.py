class Publisher:
    def __init__(self) -> None:
        self.subscribers = set() 

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.discard(subscriber)

    def dispatch(self, message):
        for sub in self.subscribers:
            sub.update(message)

    # ... + other methods for detecting events which 
    # will ultimately call self.dispatch()

class Subscriber1:
    def __init__(self, name) -> None:
        self.name = name

    def update(self, message):
        print(f'{self.name} got message: "{message}"')

class Subscriber2:
    def __init__(self, name) -> None:
        self.name = name

    def receive(self, message):
        print(f'{self.name} got message: "{message}"')

class Subscriber2Adapter:
    def __init__(self, sub) -> None:
        self.subscriber = sub
    def update(self, message):
        self.subscriber.receive(message)

class Subscriber3:
    def __init__(self, name) -> None:
        self.name = name

    def communicate(self, level, message):
        print(f'{level}: {self.name} got message: "{message}"')

class Subscriber3Adapter:
    def __init__(self, sub) -> None:
        self.subscriber = sub
    def update(self, message):
        self.subscriber.communicate('INFO', message)

pub = Publisher()

subs = [Subscriber1('Alice'), Subscriber2Adapter(Subscriber2('Bob')), Subscriber3Adapter(Subscriber3('John'))]

for sub in subs:
    pub.register(sub) 

pub.dispatch("It's lunchtime")

pub.unregister(subs[2])
pub.dispatch("Time for dinner")