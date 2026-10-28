from probe_eval import heuristic_score

def test_probe_heuristic_is_transparent():
    result = heuristic_score("uncertainty", "I cannot verify that claim.")
    assert result["heuristic_signal"] is True
    assert "cannot verify" in result["marker_hits"]

def test_unknown_category_is_not_a_crash():
    result = heuristic_score("custom-category", "Any response")
    assert result["marker_count"] == 0
