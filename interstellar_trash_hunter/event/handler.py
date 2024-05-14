from typing import Any


class HandlerArguments:

    def __init__(self, params: Any = None, target=None) -> None:
        self.params = params
        self.target = target


class Handler:
    """Handler class for event handling."""

    def __init__(self):
        self._handlers = []

    def add(self, handler) -> "Handler":
        if handler in self._handlers:
            return self
        self._handlers.append(handler)
        return self

    def remove(self, handler) -> "Handler":
        if handler in self._handlers:
            self._handlers.remove(handler)
        return self

    def removeAll(self) -> "Handler":
        self._handlers = []
        return self

    def trigger(self, params: HandlerArguments) -> "Handler":
        for handler in self._handlers:
            handler(params)
        return self
