import pytest
from unittest.mock import Mock, patch
from filter_sha import SHA_1


def test_business_logic():
    with patch("filter_sha.read_input") as mock:
        # `random_mock.return_value = 0.9` configures the mock object to make the `random` function always return 0.9 within the test context.
        mock.return_value = [
            "commit 6b2658ff925db7f0439821712404e3c35339a3b9",
            "Author: Till Tantau <tantau@users.sourceforge.net>",
            "Date:   Thu Jun 30 08:01:57 2005 +0000",
        ]
        sha = SHA_1("6b")
        sha.business_logic(mock())
        assert sha.commit == ["6b2658ff925db7f0439821712404e3c35339a3b9"]
