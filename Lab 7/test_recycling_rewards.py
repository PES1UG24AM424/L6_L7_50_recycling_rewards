from hypothesis import given, strategies as st
from recycling_rewards import (
    parse_collection,
    weight_average,
    net_points
)

@given(st.text() | st.none())
def test_parse_collection_no_crash(s):
    try:
        parse_collection(s)
    except (ValueError, TypeError):
        pass

@given(st.text() | st.none())
def test_weight_average_no_crash(s):
    try:
        weight_average(s)
    except (ValueError, TypeError):
        pass

@given(st.text() | st.none())
def test_net_points_no_crash(s):
    try:
        net_points(s)
    except (ValueError, TypeError):
        pass
