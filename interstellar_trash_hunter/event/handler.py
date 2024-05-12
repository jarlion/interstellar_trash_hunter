from typing import Any


class HandlerArguments:

    def __init__(self, params: Any = None, target=None) -> None:
        self.params = params
        self.target = target


class Handler:
    """Handler class for event handling."""

    def __init__(self):
        self.handlers = []

    def add(self, handler) -> "Handler":
        if handler in self.handlers:
            return self
        self.handlers.append(handler)
        return self

    def remove(self, handler) -> "Handler":
        if handler in self.handlers:
            self.handlers.remove(handler)
        return self

    def removeAll(self) -> "Handler":
        self.handlers = []
        return self

    def trigger(self, params: HandlerArguments) -> "Handler":
        for handler in self.handlers:
            handler(params)
        return self
