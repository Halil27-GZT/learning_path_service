import pytest

from app import clients


class _Capture:
    def __init__(self):
        self.calls = []


def test_fetch_topics_calls_expected_url(monkeypatch):
    cap = _Capture()
    
    def mock_get_json(url):
        cap.calls.append(url)
        return [{"id": "t1"}, {"name": "Topic 1"}]
    
    monkeypatch.setattr(clients, "get_json", mock_get_json)
    
    response = clients.fetch_topics()
    
    assert response == [{"id": "t1"}, {"name": "Topic 1"}]
    assert len(cap.calls) == 1
    assert cap.calls[0].endswith("/topics")
    
    
def test_fetch_skills_calls_expected_url(monkeypatch):
    cap = _Capture()
    
    def mock_get_json(url):
        cap.calls.append(url)
        return [{"id": "s1"}, {"name": "Skill 1"}]
    
    monkeypatch.setattr(clients, "get_json", mock_get_json)
    
    response = clients.fetch_skills()
    
    assert response == [{"id": "s1"}, {"name": "Skill 1"}]
    assert len(cap.calls) == 1
    assert cap.calls[0].endswith("/skills")
     
    
def test_fetch_resources_calls_expected_url_and_transforms_ids(monkeypatch):
    cap = _Capture()
    
    def mock_get_json(url):
        cap.calls.append(url)
        return [
            {"_id": "r1", "name": "Resource 1"},
            {"id": "r2", "name": "Resource 2"},
            {"name": "Resource 3"}
        ]
    
    monkeypatch.setattr(clients, "get_json", mock_get_json)
    
    response = clients.fetch_resources()
    
    assert response == [
        {"_id": "r1", "name": "Resource 1", "id": "r1"},
        {"id": "r2", "name": "Resource 2"},
        {"name": "Resource 3"}
    ]
    assert len(cap.calls) == 1
    assert cap.calls[0].endswith("/resources")
    
    
    
    
