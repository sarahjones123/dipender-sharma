"""Tests for the portfolio content generation script."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '02-doc-site-portfolio', 'scripts'))

from generate_content import (
    get_sample_profile,
    format_profile,
    format_project,
    wrap_output,
)


class TestGetSampleProfile:
    def test_returns_dict(self):
        assert isinstance(get_sample_profile(), dict)

    def test_has_required_keys(self):
        required = {'name', 'title', 'specialties', 'tools', 'experience'}
        assert required.issubset(get_sample_profile().keys())

    def test_has_projects(self):
        profile = get_sample_profile()
        assert 'projects' in profile
        assert len(profile['projects']) > 0

    def test_project_has_required_keys(self):
        for project in get_sample_profile()['projects']:
            required = {'name', 'description', 'contribution'}
            assert required.issubset(project.keys()), f"Project missing keys: {project}"

    def test_specialties_is_list(self):
        assert isinstance(get_sample_profile()['specialties'], list)

    def test_tools_is_list(self):
        assert isinstance(get_sample_profile()['tools'], list)

    def test_experience_is_list(self):
        assert isinstance(get_sample_profile()['experience'], list)


class TestFormatProfile:
    def test_includes_name(self):
        profile = get_sample_profile()
        assert profile['name'] in format_profile(profile)

    def test_includes_title(self):
        profile = get_sample_profile()
        assert profile['title'] in format_profile(profile)

    def test_includes_specialties(self):
        profile = get_sample_profile()
        result = format_profile(profile)
        for specialty in profile['specialties']:
            assert specialty in result

    def test_includes_company_names(self):
        profile = get_sample_profile()
        result = format_profile(profile)
        for job in profile['experience']:
            assert job['company'] in result

    def test_returns_string(self):
        assert isinstance(format_profile(get_sample_profile()), str)

    def test_handles_minimal_profile(self):
        minimal = {"name": "Test User", "title": "Writer"}
        result = format_profile(minimal)
        assert "Test User" in result
        assert "Writer" in result

    def test_handles_missing_optional_fields(self):
        # Should not raise even when optional keys are absent
        result = format_profile({"name": "A", "title": "B"})
        assert isinstance(result, str)


class TestFormatProject:
    def test_includes_project_name(self):
        project = get_sample_profile()['projects'][0]
        assert project['name'] in format_project(project)

    def test_includes_contribution(self):
        project = get_sample_profile()['projects'][0]
        assert project['contribution'] in format_project(project)

    def test_includes_outcome(self):
        project = get_sample_profile()['projects'][0]
        result = format_project(project)
        assert project['outcome'] in result

    def test_returns_string(self):
        project = get_sample_profile()['projects'][0]
        assert isinstance(format_project(project), str)

    def test_handles_minimal_project(self):
        minimal = {"name": "My Project", "description": "A test project"}
        result = format_project(minimal)
        assert "My Project" in result

    def test_handles_missing_optional_fields(self):
        # Should not raise when optional keys are absent
        result = format_project({"name": "X", "description": "Y"})
        assert isinstance(result, str)


class TestWrapOutput:
    def test_includes_original_content(self):
        content = "# About Me\nSome content here."
        assert content in wrap_output(content, "about")

    def test_includes_disclaimer(self):
        assert "review" in wrap_output("content", "about").lower()

    def test_returns_string(self):
        assert isinstance(wrap_output("content", "about"), str)

    def test_content_comes_before_disclaimer(self):
        content = "# My Page"
        result = wrap_output(content, "about")
        assert result.index(content) < result.index("---")
