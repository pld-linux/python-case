#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python unittest utilities
Summary(pl.UTF-8):	Pythonowe narzędzia do testów jednostkowych
Name:		python-case
Version:	1.5.3
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/case/
Source0:	https://files.pythonhosted.org/packages/source/c/case/case-%{version}.tar.gz
# Source0-md5:	169acc1fe087b8938cdf31da8ab426be
URL:		https://pypi.org/project/case/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools >= 1:20.6.7
%if %{with tests}
BuildRequires:	python-mock >= 2.0
BuildRequires:	python-nose >= 1.3.7
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools >= 1:20.6.7
%if %{with tests}
BuildRequires:	python3-nose >= 1.3.7
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_celery >= 1.1
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python unittest utilities.

%description -l pl.UTF-8
Pythonowe narzędzia do testów jednostkowych.

%package -n python3-case
Summary:	Python unittest utilities
Summary(pl.UTF-8):	Pythonowe narzędzia do testów jednostkowych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-case
Python unittest utilities.

%description -n python3-case -l pl.UTF-8
Pythonowe narzędzia do testów jednostkowych.

%package apidocs
Summary:	API documentation for Python case module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona case
Group:		Documentation

%description apidocs
API documentation for Python case module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona case.

%prep
%setup -q -n case-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m nose case/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m nose case/tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc Changelog LICENSE README.rst
%{py_sitescriptdir}/case
%{py_sitescriptdir}/case-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-case
%defattr(644,root,root,755)
%doc Changelog LICENSE README.rst
%{py3_sitescriptdir}/case
%{py3_sitescriptdir}/case-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,reference,*.html,*.js}
%endif
