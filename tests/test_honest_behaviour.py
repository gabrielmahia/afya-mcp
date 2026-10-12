from afya_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_an_unknown_trimester_is_an_error_not_silently_first_trimester_advice():
    """A health tool must not answer a question it did not understand with first-trimester guidance."""
    r = _fn("maternal_health_guide")("fourth")
    assert "error" in r and r["valid_trimesters"] == ["first", "second", "third"] and "anc_visits" not in r


def test_known_trimesters_and_ordinal_spellings_still_work():
    for t in ("first", "2nd", "Third"):
        assert "anc_visits" in _fn("maternal_health_guide")(t)


def test_specific_concern_really_is_ignored_as_the_description_says():
    assert _fn("maternal_health_guide")("second", "headache") == _fn("maternal_health_guide")("second", None)


def test_the_facility_finder_is_described_as_a_template_and_says_so_in_its_output():
    r = _fn("health_facility_finder")("Kisumu")
    assert r["source"].startswith("DEMO") and all(f["name"].endswith("Kisumu") or "Kisumu" in f["name"] for f in r["facilities"])
