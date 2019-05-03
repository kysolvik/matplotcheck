"""Tests for the base module"""
import pytest


""" PLOT TYPE TESTS """


def test_line_plot(pt_line_plt):
    """Test that the line plot returns true for line but false for bar or
    scatter."""
    pt_line_plt.assert_plot_type("line")

    with pytest.raises(AssertionError):
        pt_line_plt.assert_plot_type("bar")
    with pytest.raises(AssertionError):
        pt_line_plt.assert_plot_type("scatter")


def test_scatter_plot(pt_scatter_plt):
    """Test that the scatter plot returns true for line but false for bar or
    line."""
    pt_scatter_plt.assert_plot_type("scatter")

    with pytest.raises(AssertionError):
        pt_scatter_plt.assert_plot_type("bar")
    with pytest.raises(AssertionError):
        pt_scatter_plt.assert_plot_type("line")


def test_bar_plot(pt_bar_plt):
    """Test that the scatter plot returns true for line but false for bar or
    line."""
    pt_bar_plt.assert_plot_type("bar")

    with pytest.raises(AssertionError):
        pt_bar_plt.assert_plot_type("scatter")
    with pytest.raises(AssertionError):
        pt_bar_plt.assert_plot_type("line")


def test_invalid_plot_type(pt_line_plt):
    """Test that a ValueError is raised if an incorrect plot type is provided."""
    with pytest.raises(
        ValueError,
        match="Plot_type to test must be either: scatter, bar or line",
    ):
        pt_line_plt.assert_plot_type("foo")


""" TITLE TESTS """


def test_get_titles(pt_line_plt):
    """Check that the correct plot title is grabbed from the axis object.
    Note that get_titles maintains case."""
    assert "My Plot Title" == pt_line_plt.get_titles()[1]


def test_get_titles_suptitle(pt_line_plt):
    """Check that the correct suptitle gets grabbed from a figure with 2 subplots"""
    assert "My Figure Title" == pt_line_plt.get_titles()[0]


def test_title_contains_empty_expect(pt_line_plt):
    """Check title_contains when expected title is empty"""
    pt_line_plt.assert_title_contains([])


def test_title_contains_expect_none(pt_line_plt):
    """Check title_contains when expected title is None"""
    pt_line_plt.assert_title_contains(None)


def test_title_contains_axes(pt_line_plt):
    """Check title_contains for axes title"""
    pt_line_plt.assert_title_contains(
        ["My", "Plot", "Title"], title_type="axes"
    )


def test_title_contains_axes_badtext(pt_line_plt):
    """Check title_contains fails when given bad text"""
    with pytest.raises(
        AssertionError, match="Title does not contain expected text:foo"
    ):
        pt_line_plt.assert_title_contains(
            ["Title", "foo", "bar"], title_type="axes"
        )


def test_title_contains_invalid_title_type(pt_line_plt):
    """Check title_contains raises value error when given invalid title type"""
    with pytest.raises(
        ValueError, match="title_type must be one of the following"
    ):
        pt_line_plt.assert_title_contains(["Title"], title_type="all")


def test_title_contains_figure(pt_line_plt):
    """Check title_contains tester for figure/sup title"""
    pt_line_plt.assert_title_contains(
        ["My", "Figure", "Title"], title_type="figure"
    )


def test_title_contains_figure_nosuptitle(pt_bar_plt):
    """Check title_contains tester for figure title fails when there is no suptitle"""
    with pytest.raises(
        AssertionError, match="Expected title is not displayed"
    ):
        pt_bar_plt.assert_title_contains(
            ["My", "Figure", "Title"], title_type="figure"
        )


def test_title_contains_both_axes_figure(pt_line_plt):
    """Check title_contains tester for combined axes + figure titles"""
    pt_line_plt.assert_title_contains(
        ["My", "Figure", "Plot", "Title"], title_type="either"
    )


def test_title_contains_both_axes_figure_badtext(pt_line_plt):
    """Check title_contains tester for combined titles, should fail with bad text"""
    with pytest.raises(
        AssertionError, match="Title does not contain expected text:foo"
    ):
        pt_line_plt.assert_title_contains(
            ["My", "Figure", "Plot", "Title", "foo"], title_type="either"
        )


""" CAPTION TESTS """


def test_get_caption(pt_line_plt):
    """Make sure that get caption returns correct text string"""
    assert "Figure Caption" == pt_line_plt.get_caption().get_text()


def test_assert_caption_contains(pt_line_plt):
    """Test that caption contains passes given right text"""
    pt_line_plt.assert_caption_contains([["Figure"], ["Caption"]])


def test_assert_caption_contains_expect_empty(pt_line_plt):
    """Test that caption contains passes when expected text list is empty"""
    pt_line_plt.assert_caption_contains([])


def test_assert_caption_contains_expect_none(pt_line_plt):
    """Test that caption contains passes when expected text is None"""
    pt_line_plt.assert_caption_contains(None)


def test_assert_caption_contains_badtext(pt_line_plt):
    """Test that caption contains passes given wrong text"""
    with pytest.raises(
        AssertionError, match="Caption does not contain expected string: foo"
    ):
        pt_line_plt.assert_caption_contains([["foo"], ["bar"]])


def test_assert_caption_contains_nocaption(pt_bar_plt):
    """Test that caption_contains fails when there is no caption"""
    with pytest.raises(
        AssertionError, match="No caption exist in appropriate location"
    ):
        pt_bar_plt.assert_caption_contains([["Figure"], ["Caption"]])
