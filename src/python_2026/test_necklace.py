# ---------------------------------------------------------------------------
# Examples from the specification
# ---------------------------------------------------------------------------
import pytest

from python_2026.beautiful_necklace import is_beautiful


@pytest.mark.parametrize(
    "necklace, expected",
    [
        ("..**..**..**", True),  # 3 pads of len 2, distancers of len 2
        ("..**..**...**", False),  # 2nd distancer is longer
        ("..***.***.***.***", True),  # 4 pads of len 3, distancers of len 1
        ("..***..***..**...", False),  # 3rd pad is shorter
    ],
)
def test_spec_examples(necklace, expected):
    assert is_beautiful(necklace) is expected


# ---------------------------------------------------------------------------
# Beautiful necklaces
# ---------------------------------------------------------------------------

def test_single_pad_no_padding():
    assert is_beautiful("***") is True


def test_single_star():
    assert is_beautiful("*") is True


def test_single_pad_with_leading_and_trailing_dots():
    assert is_beautiful("....**....") is True


def test_two_pads_equal_distancer():
    assert is_beautiful("**.**") is True


def test_pads_of_length_one():
    assert is_beautiful("*.*.*.*") is True


def test_long_distancers():
    assert is_beautiful("**.....**.....**") is True


def test_asymmetric_leading_and_trailing_dots_ignored():
    # 1 leading dot, 5 trailing dots – must not matter
    assert is_beautiful(".**..**.....") is True


def test_trailing_dots_only():
    assert is_beautiful("***.***......") is True


def test_leading_dots_only():
    assert is_beautiful("......***.***") is True


def test_pad_length_differs_from_distancer_length():
    # pad len 4, distancer len 2 — lengths need only be consistent per kind
    assert is_beautiful("****..****..****") is True


def test_many_pads():
    assert is_beautiful(".".join(["**"] * 50)) is True


# ---------------------------------------------------------------------------
# Not beautiful necklaces
# ---------------------------------------------------------------------------

def test_first_pad_shorter():
    assert is_beautiful("*.**.**") is False


def test_last_pad_longer():
    assert is_beautiful("**.**.***") is False


def test_middle_pad_different():
    assert is_beautiful("**.***.**") is False


def test_first_distancer_shorter():
    assert is_beautiful("**.**..**") is False


def test_last_distancer_shorter():
    assert is_beautiful("**..**.**") is False


def test_middle_distancer_different():
    assert is_beautiful("**.**..**.**") is False


def test_both_pads_and_distancers_inconsistent():
    assert is_beautiful("*..**...***") is False


def test_inconsistency_hidden_by_padding():
    # leading/trailing dots are fine, but the inner distancers still differ
    assert is_beautiful("...**.**..**...") is False


def test_pad_mismatch_only_at_the_end_of_long_necklace():
    body = ".".join(["***"] * 20) + ".**"
    assert is_beautiful(body) is False


# ---------------------------------------------------------------------------
# Edge cases / invalid input
# ---------------------------------------------------------------------------

def test_empty_string_is_not_beautiful():
    # No pads at all — nothing to be beautiful.
    assert is_beautiful("") is False


def test_only_dots_is_not_beautiful():
    assert is_beautiful("......") is False


@pytest.mark.parametrize("necklace", ["***.**", "**..*.*", "**.***", "**.*..*"])
def test_invalid_characters_are_not_beautiful(necklace):
    assert is_beautiful(necklace) is False


def test_return_type_is_bool():
    assert isinstance(is_beautiful("**.**"), bool)
    assert isinstance(is_beautiful("**..*"), bool)