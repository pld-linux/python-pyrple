%define		module	pyrple
%define		ver_y	2004
%define		ver_m	01
%define		ver_d	26

Summary:	Pyrple - parser for RDF/XML, N3, and N-Triples
Summary(pl):	Pyrple - parser dla RDF/XML, N3, N-Triples
Name:		python-%{module}
Version:	%{ver_y}%{ver_m}%{ver_d}
Release:	2
License:	BSD-like (see LICENSE.txt)
Vendor:		Robin Dunn <robin@alldunn.com>
Group:		Development/Languages/Python
Source0:	http://infomesh.net/pyrple/%{module}-%{ver_y}-%{ver_m}-%{ver_d}.tar.gz
# Source0-md5:	dfa643e209bb1948c25cab604fd78adc
URL:		http://infomesh.net/pyrple/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyrple parses RDF/XML, N3, and N-Triples. It has in-memory storage
with API-level querying, experimental marshalling, many utilities, 
and is small and minimally interdependent. It can do graph isomorphism
testing, rule application, etc.

%description -l pl
Pyrple analizuje dane RDF/XML, N3, N-Triplets. Ma przechowywanie
danych w pamiêci z odpytywaniem na poziomie API, eksperymentalnym
porz±dkowaniem, wieloma narzêdziami. Jest ma³y i ma minimalne
zale¿no¶ci. Mo¿e sprawdzaæ izomorficzno¶æ grafów, dzia³anie regu³ itp.

%prep
%setup -q -n %{module}-%{ver_y}-%{ver_m}-%{ver_d}

%build
%{py_comp} .
%{py_ocomp} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

find . -name \*.py | xargs rm -f

cp -R . $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{py_sitescriptdir}/%{module}
