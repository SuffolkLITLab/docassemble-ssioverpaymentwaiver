import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ssioverpaymentwaiver',
      version='0.5.4',
      description=('Request for Waiver of SSI Overpayment'),
      long_description='# SSI Overpayment waiver\r\n\r\nAn interview to help an individual appeal an overpayment set by the Social\r\nSecurity Administration.\r\n\r\n# Changelog\r\n* 2022-03-07 Minor fix of typo and voice\r\n* 2022-01-15 Add warning for rep payee about filing own copy\r\n* 2022-01-08 Bug fix\r\n* 2021-11-17 Finish the addendum stuff and other refinements\r\n* 2021-11-07 Get through more of VLP punchlist\r\n* 2021-11-06 Add 2019 version of SSA-632BK\r\n* 2021-10-03 Fix office locator\r\n* 2021-10-03 Merge previous fixes\r\n* 2020-12-12 Bug fixes\r\n* 2020-12-08 Bug fixes\r\n* 2020-12-05 duplicate id bug\r\n* 2020-11-27 Bugfixes\r\n* 2020-11-14 Add feedback form + show question ID on debug site\r\n* 2020-10-12 Fix template export value\r\n* 2020-09-28 Modified financial statement, prepared SSA-634\r\n* 2019-10-09 Bug fixes, language cleanup\r\n* 2019-09-29 Bug fixes (question order, hide irrelevant questions)\r\n* 2019-09-21 Bug fixes, finish implementing PDF fields\r\n* 2019-02-06 Preliminary mapping of all PDF fields\r\n* 2019-01-25 Bring to current\r\n* 2018-12-01 Improved financial statement (in progress) and logical questions for overpayment\r\n* Initial version - handles basic financial statement',
      long_description_content_type='text/markdown',
      author='Quinten Steenhuis',
      author_email='qsteenhuis@gmail.com',
      license='The MIT License',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=['docassemble.GithubFeedbackForm>=0.4.1.1', 'docassemble.income>=0.0.36', 'docassemble.ssa'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ssioverpaymentwaiver/', package='docassemble.ssioverpaymentwaiver'),
     )

