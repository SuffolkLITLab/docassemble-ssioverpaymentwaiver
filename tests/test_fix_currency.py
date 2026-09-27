"""Regression checks for currency formatting across Docassemble API layouts."""

from docassemble.base.util import DAEmpty

from docassemble.ssioverpaymentwaiver import fix_currency


def test_currency_helper_imports_and_registers_for_docassemble_version():
    """Importing the C01 currency helper must work with old and new APIs."""
    assert callable(fix_currency.currency_default)
    assert callable(fix_currency.empty_currency)


def test_empty_values_still_render_as_blank():
    assert fix_currency.empty_currency(DAEmpty()) == ""


def test_nonempty_values_delegate_to_currency_default(monkeypatch):
    calls = []

    def currency_default(value, **kwargs):
        calls.append((value, kwargs))
        return "formatted"

    monkeypatch.setattr(fix_currency, "currency_default", currency_default)
    assert fix_currency.empty_currency(42, decimals=False) == "formatted"
    assert calls == [(42, {"decimals": False})]
