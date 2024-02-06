def test_redirect(client_with_test_fs):
    resp = client_with_test_fs.get("/pdf/cs/0212040v1.pdf")
    assert resp.status_code == 301 and  resp.headers["Location"].endswith("/pdf/cs/0212040v1")

    resp = client_with_test_fs.get("/pdf/1208.6335v1.pdf")
    assert resp.status_code == 301 and resp.headers["Location"].endswith("/pdf/1208.6335v1")
