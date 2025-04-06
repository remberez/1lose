class NotFoundError(Exception):
    def __init__(self, *messages: str):
        self.messages = messages
        super().__init__(str(messages))  # Для обратной совместимости
