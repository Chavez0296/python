class Node:
    def __init__(self, data) -> None:
        self._data = data
        self._next = None
    
    def get_data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data

    data = property(get_data,set_data)

    def get_next(self):
        return self._next
    
    def set_next(self, node_next):
        self._next = node_next

    next = property(get_next,set_next)

    def __str__(self) -> str:
        return str(self._data)