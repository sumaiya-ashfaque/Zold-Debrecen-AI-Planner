from backend.services.data_service import planting_candidates
from backend.agents.planting_opportunity_agent import rank_candidates

def test_candidates_are_ranked_descending():
    ranked = rank_candidates(planting_candidates())
    scores = [x["properties"]["opportunity_score"] for x in ranked]
    assert scores == sorted(scores, reverse=True)
