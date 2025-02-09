Name:		python-dropbox
Version:	12.0.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/dropbox/dropbox-%{version}.tar.gz
Summary:	Official Dropbox API Client
URL:		https://pypi.org/project/dropbox/
License:	MIT License
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pytest-runner)
BuildSystem:	python
BuildArch:	noarch

%description
Official Dropbox API Client

%prep
%autosetup -p1 -n dropbox-%{version}

%files
%{py_sitedir}/dropbox
%{py_sitedir}/dropbox-*.*-info
