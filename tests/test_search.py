from search import create_app


def test_empty_response() -> None:
    app = create_app()
    client = app.test_client()
    response = client.get('/search')
    assert response.status == '200 OK'
    assert response.data == (b'<?xml version="1.0" encoding="UTF-8"?>'
                             b'<item-list xmlns="http://libero.pub"/>')
    assert response.content_type == 'application/xml; charset=utf-8'
