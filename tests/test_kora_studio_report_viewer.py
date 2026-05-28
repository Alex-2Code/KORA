from __future__ import annotations

from kora.studio_report_viewer import (
    REPORT_EXPORT_CLAIM_BOUNDARY,
    REPORT_VIEWER_CLAIM_BOUNDARY,
    REPORT_VIEWER_COUNTERS,
    REPORT_VIEWER_FIXTURE_PATH,
    get_report_export_placeholder,
    get_report_viewer_placeholder,
    get_report_viewer_status_fields,
)


def test_report_viewer_placeholder_is_fixture_only_and_local_safe() -> None:
    viewer = get_report_viewer_placeholder()

    assert viewer["report_viewer_status"] == "fixture_metadata_placeholder"
    assert viewer["fixture_type"] == "report_viewer_metadata"
    assert viewer["report_fixture_path"] == REPORT_VIEWER_FIXTURE_PATH
    assert viewer["privacy_class"] == "synthetic"
    assert viewer["supported_fixture_only"] is True
    assert viewer["arbitrary_local_file_scan_enabled"] is False
    assert viewer["local_file_picker_connected"] is False
    assert viewer["upload_enabled"] is False
    assert viewer["provider_calls_enabled"] is False
    assert viewer["cloud_sync_enabled"] is False
    assert viewer["generated_report_commit_enabled"] is False
    assert viewer["counters"] == REPORT_VIEWER_COUNTERS
    assert "does not scan arbitrary local files" in viewer["claim_boundary"]
    assert "upload reports" in viewer["claim_boundary"]
    assert "new benchmark evidence" in viewer["claim_boundary"]


def test_report_export_placeholder_is_disabled() -> None:
    export = get_report_export_placeholder()

    assert export["report_export_status"] == "placeholder_not_connected"
    assert export["export_action_enabled"] is False
    assert export["export_action_label"] == "Export not connected yet"
    assert export["writes_generated_reports"] is False
    assert export["uploads_reports"] is False
    assert export["commits_generated_reports"] is False
    assert export["claim_boundary"] == REPORT_EXPORT_CLAIM_BOUNDARY


def test_report_viewer_status_fields_expose_boundaries() -> None:
    status_fields = get_report_viewer_status_fields()

    assert status_fields["report_viewer_status"] == "fixture_metadata_placeholder"
    assert status_fields["report_viewer_claim_boundary"] == REPORT_VIEWER_CLAIM_BOUNDARY
    assert status_fields["report_export_status"] == "placeholder_not_connected"
    assert status_fields["report_export_claim_boundary"] == REPORT_EXPORT_CLAIM_BOUNDARY
    assert status_fields["report_viewer_placeholder"]["counters"]["avoided_model_calls"] == 8
    assert status_fields["report_export_placeholder"]["export_action_enabled"] is False
