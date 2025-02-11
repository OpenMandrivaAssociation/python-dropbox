Name:		python-dropbox
Version:	12.0.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/dropbox/dropbox-%{version}.tar.gz
Summary:	Official Dropbox API Client
URL:		https://pypi.org/project/dropbox/
License:	MIT License
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(pytest-runner)
BuildRequires:	python%{pyver}dist(mock)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(six)
BuildRequires:	python%{pyver}dist(stone)
BuildSystem:	python
BuildArch:	noarch

%patchlist
dropbox-12.0.2-relax-stone-deps.patch

%description
Official Dropbox API Client

%prep -a
sed -i -e 's,pytest-runner==,pytest-runner>=,g' setup.py

%files
%{py_sitedir}/dropbox
%{py_sitedir}/dropbox-*.*-info
