%include	/usr/lib/rpm/macros.perl
Summary:	Netscape-History perl module
Summary(pl):	Modu³ perla Netscape-History
Name:		perl-Netscape-History
Version:	3.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Netscape/Netscape-History-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-URI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netscape-History - module for accessing Netscape history database.

%description -l pl
Netscape-History umo¿liwia dostêp do bazy danych historii Netscape'a.

%prep
%setup -q -n Netscape-History-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Netscape/History.pm
%{perl_sitelib}/Netscape/HistoryURL.pm
%{_mandir}/man3/*
