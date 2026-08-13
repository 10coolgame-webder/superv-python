from main import solve_common_card_choice


def test_returns_yes_for_a_valid_split() -> None:
    assert solve_common_card_choice(["4", "2", "2"]) == "YES"


def test_returns_yes_when_a_prime_divisor_is_available() -> None:
    assert solve_common_card_choice(["3", "1", "2", "3"]) == "YES"


def test_returns_no_when_only_trivial_splits_work() -> None:
    assert solve_common_card_choice(["3", "1", "1", "1"]) == "NO"


def test_matches_sample_one() -> None:
    sample = ["7", "19", "7", "11", "31", "99", "13", "17"]
    assert solve_common_card_choice(sample) == "YES"


def test_matches_sample_two() -> None:
    sample = ["3", "3", "11", "17"]
    assert solve_common_card_choice(sample) == "NO"
