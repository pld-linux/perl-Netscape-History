#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)

%define		pdir	Netscape
%define		pnam	History
%include	/usr/lib/rpm/macros.perl
Summary:	Netscape::History perl module
Summary(pl.UTF-8):	Moduł perla Netscape::History
Name:		perl-Netscape-History
Version:	3.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c818ccf480aae7bf6e62e0566b1fff73
URL:		http://search.cpan.org/dist/Netscape-History/
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netscape::History - module for accessing Netscape history database.

%description -l pl.UTF-8
Netscape::History umożliwia dostęp do bazy danych historii Netscape'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Netscape/History.pm
%{perl_vendorlib}/Netscape/HistoryURL.pm
%{_mandir}/man3/*
