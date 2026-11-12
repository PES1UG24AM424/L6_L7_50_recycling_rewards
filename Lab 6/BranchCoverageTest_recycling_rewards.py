
import pytest
from recycling_rewards import (
    reward_points,
    collection_accepted,
    slot_status
)


@pytest.mark.parametrize("material,weight,bonus,expected", [
    ("paper", 3, False, 0),
    ("paper", 6, False, 6),
    ("paper", 5, True, 6),
    ("plastic", 4, False, 6),
    ("plastic", 3, True, 6),
    ("metal", 3, False, 12),
    ("metal", 2, True, 0),
    ("metal", 25, False, 414),
    ("paper", 30, False, 250),
])
def test_reward_points(material, weight, bonus, expected):
    assert reward_points(material, weight, bonus) == expected


def test_unknown_material():
    with pytest.raises(ValueError):
        reward_points("glass", 10, False)


def test_negative_weight():
    with pytest.raises(ValueError):
        reward_points("paper", -1, False)


@pytest.mark.parametrize("weight,bags,hazardous,expected", [
    (4, 5, True, True),
    (6, 2, True, False),
    (20, 2, False, True),
    (60, 2, False, False),
    (20, 4, False, False),
])
def test_collection(weight, bags, hazardous, expected):
    assert collection_accepted(weight, bags, hazardous) == expected


@pytest.mark.parametrize("minutes,morning,holiday,expected", [
    (20, True, False, "open"),
    (10, False, False, "open"),
    (35, True, True, "open"),
    (10, True, False, "late"),
    (0, True, False, "missed"),
    (25, False, True, "open"),
])
def test_slots(minutes, morning, holiday, expected):
    assert slot_status(minutes, morning, holiday) == expected
