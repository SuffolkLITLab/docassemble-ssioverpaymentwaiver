from docassemble.base.util import DAEmpty, currency
from docassemble.base.functions import update_language_function

try:
  # Older Docassemble versions re-exported this helper from functions.
  from docassemble.base.functions import currency_default
except ImportError:
  # Docassemble 1.10 moved it to the language currency module.
  from docassemble.base.language.currency import currency_default

def empty_currency(*pargs, **kwargs):
  if isinstance(pargs[0], DAEmpty):
    return ""
  return currency_default(*pargs, **kwargs)

update_language_function('*', 'currency', empty_currency)

def thousands(num:float) -> str:
  """
  Return a whole number formatted with thousands separator.
  """
  try:
    return f"{int(num):,}"
  except:
    return num
