import pytest

from summarizer import MAX_INPUT_CHARACTERS, SummaryLength, summarize_text


@pytest.mark.asyncio
async def test_empty_text_is_rejected():
    with pytest.raises(ValueError, match="Text cannot be empty"):
        await summarize_text("   ")


@pytest.mark.asyncio
async def test_oversized_text_is_rejected():
    text = "א" * (MAX_INPUT_CHARACTERS + 1)

    with pytest.raises(ValueError, match="Text is too long"):
        await summarize_text(text, SummaryLength.MEDIUM)


def test_summary_length_values():
    assert SummaryLength.SHORT.value == "short"
    assert SummaryLength.MEDIUM.value == "medium"
    assert SummaryLength.DETAILED.value == "detailed"
