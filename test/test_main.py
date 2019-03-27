
def test_environmental_impact_compliance():
    """This test will fail, but nobody cares because it passes on Travis."""
    emissions = 12000
    legal_limit = 300
    assert emissions < legal_limit
