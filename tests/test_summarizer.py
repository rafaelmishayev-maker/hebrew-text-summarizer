"""Tests for the input-validation contract of :mod:`summarizer`.

These cases deliberately cover only the paths that run before any network
call, so the suite is deterministic and needs neither an API key nor network
access. The provider interaction itself is left to manual verification.
"""

import pytest

from summarizer import MAX_INPUT_CHARACTERS, SummaryLength, summarize_text


@pytest.mark.asyncio
async def test_empty_text_is_rejected():
    """Whitespace-only input must be rejected before a request is sent."""
    with pytest.raises(ValueError, match="Text cannot be empty"):
        await summarize_text("   ")


@pytest.mark.asyncio
async def test_oversized_text_is_rejected():
    """Input one character past the cap must be rejected, not truncated."""
    text = "א" * (MAX_INPUT_CHARACTERS + 1)

    with pytest.raises(ValueError, match="Text is too long"):
        await summarize_text(text, SummaryLength.MEDIUM)


def test_summary_length_values():
    """Guard the wire format of the enum.

    These strings are submitted by the form's radio inputs and echoed back
    into the template, so renaming a member without updating the HTML would
    silently break length selection.
    """
    assert SummaryLength.SHORT.value == "short"
    assert SummaryLength.MEDIUM.value == "medium"
    assert SummaryLength.DETAILED.value == "detailed"
