%include	/usr/lib/rpm/macros.python
%define		module	pyrple
%define		ver_y	2004
%define		ver_m	01
%define		ver_d	26

Summary:	Pyrple parses RDF/XML, N3, and N-Triples.
Name:		python-%{module}
Version:	%{ver_y}%{ver_m}%{ver_d}
Release:	1
License:	BSD-like (see LICENSE.txt)
Vendor:		Robin Dunn <robin@alldunn.com>
Group:		Development/Languages/Python
Source0:	http://infomesh.net/pyrple/%{module}-%{ver_y}-%{ver_m}-%{ver_d}.tar.gz
# Source0-md5:	dfa643e209bb1948c25cab604fd78adc
URL:		http://www.amk.ca/python/code/medusa.html
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyrple parses RDF/XML, N3, and N-Triples. It has in-memory storage
with API-level querying, experimental marshalling, many utilities, 
and is small and minimally interdependent. It can do graph isomorphism 
testing, rule application, etc.

%prep
%setup -q -n %{module}-%{ver_y}-%{ver_m}-%{ver_d}

%build
%{py_comp} .
%{py_ocomp} .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

find . -name \*.py | xargs rm -f
install -d $RPM_BUILD_ROOT/%{py_sitescriptdir}
cp -R . $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{module}
rm $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{module}/doc -fr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{py_sitescriptdir}/%{module}
