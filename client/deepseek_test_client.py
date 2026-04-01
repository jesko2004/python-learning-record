import pytest
import deepseek_client
from deepseek_client import get_client, ask_deepseek


def test_get_client_without_api_key(monkeypatch):
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)

    with pytest.raises(ValueError, match="DEEPSEEK_API_KEY"):
        get_client()


def test_get_client_with_api_key(fake_api_key):
    client = get_client()
    assert client is not None


def test_ask_deepseek_returns_message(monkeypatch):
    class FakeMessage:
        content = "asyncio 是 Python 的异步编程工具。"

    class FakeChoice:
        message = FakeMessage()

    class FakeResponse:
        choices = [FakeChoice()]

    class FakeCompletions:
        def create(self, **kwargs):
            return FakeResponse()

    class FakeChat:
        completions = FakeCompletions()

    class FakeClient:
        chat = FakeChat()

    monkeypatch.setattr(deepseek_client, "get_client", lambda: FakeClient())

    result = ask_deepseek("什么是 asyncio？")

    assert result == "asyncio 是 Python 的异步编程工具。"
