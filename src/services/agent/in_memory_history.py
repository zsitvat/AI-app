from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

store = {}


class InMemoryHistory:
    """
    A class to manage in-memory chat history for different sessions.
    """

    def get_history(self, user_id: str) -> BaseChatMessageHistory:
        """
        Retrieve the chat history for a given session.
        If the history does not exist, create a new one.

        Args:
            user_id (str): The unique identifier for the session.

        Returns:
            BaseChatMessageHistory: The chat history associated with the session.
        """
        if user_id not in store:
            store[user_id] = ChatMessageHistory()
        return store[user_id]

    def get_messages(self, user_id: str) -> list:
        """
        Retrieve all messages for a given session.

        Args:
            user_id (str): The unique identifier for the session.

        Returns:
            list[str]: A list of messages.
        """
        history = self.get_history(user_id)
        return history.messages

    def add_message(self, user_id: str, message: str) -> None:
        """
        Add a generic message to the chat history for a given session.

        Args:
            user_id (str): The unique identifier for the session.
            message (str): The message to add.
        """
        history = self.get_history(user_id)
        history.add_message(message)

    def add_ai_message(self, user_id: str, message: str) -> None:
        """
        Add an AI-generated message to the chat history for a given session.

        Args:
            user_id (str): The unique identifier for the session.
            message (str): The AI message to add.
        """
        history = self.get_history(user_id)
        history.add_ai_message(message)

    def add_user_message(self, user_id: str, message: str) -> None:
        """
        Add a user-generated message to the chat history for a given session.

        Args:
            user_id (str): The unique identifier for the session.
            message (str): The user message to add.
        """
        history = self.get_history(user_id)
        history.add_user_message(message)

    def clear_history(user_id: str) -> None:
        """
        Clear the chat history for a specific session.

        Args:
            user_id (str): The unique identifier for the session.
        """
        if user_id in store:
            del store[user_id]

    def get_all_sessions() -> dict[str, BaseChatMessageHistory]:
        """
        Retrieve all session histories.

        Returns:
            Dict[str, BaseChatMessageHistory]: A dictionary of all session histories.
        """
        return store
