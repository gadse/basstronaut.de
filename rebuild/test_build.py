import build

def test_setup_works():
    assert True


def test_enrich():
    expected = "a\nb\nc"

    encountered = build.enrich("b", "a", "c")

    assert expected == encountered

def test_body_extraction():
    expected = "foo"
    encountered = build.get_body("test_resources/hello.html")
    assert expected == encountered
