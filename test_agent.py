"""Standalone smoke tests for the exception agent tools."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from agent import ExceptionResolver, calculate_variance, flag_unresolvable_exception, lookup_fx_rate  # noqa: E402


def main() -> int:
    assert calculate_variance(100.00, 98.00) == -2.0
    assert flag_unresolvable_exception("ORD-TEST", "No verified linkage") == {
        "order_id": "ORD-TEST",
        "status": "EXCEPTION",
        "reason": "No verified linkage",
    }
    assert lookup_fx_rate("UNKNOWN", "2026-08-25") is None

    result = ExceptionResolver().resolve(
        "ORD-TEST",
        {"order_id": "ORD-TEST", "gross_amount": "100.00"},
        None,
        None,
    )
    assert result.status.value == "EXCEPTION"
    assert result.exception_reason
    print("Agent smoke test passed: tools and conservative fallback are operational.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
