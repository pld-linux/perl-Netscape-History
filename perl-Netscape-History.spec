%include	/usr/lib/rpm/macros.perl
Summary:	Netscape-History perl module
Summary(pl):	Modu³ perla Netscape-History
Name:		perl-Netscape-History
Version:	3.00
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Netscape/Netscape-History-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-URI
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netscape-History - module for accessing Netscape history database.

%description -l pl
Netscape-History umo¿liwia dostêp do bazy danych historii Netscape'a.

%prep
%setup -q -n Netscape-History-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Netscape
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Netscape/History.pm
%{perl_sitelib}/Netscape/HistoryURL.pm
%{perl_sitearch}/auto/Netscape/.packlist

%{_mandir}/man3/*
