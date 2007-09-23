Summary:	Perl modules for ldap
Name:		perl-ldap
Version:	0.34
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{name}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.0
%endif
BuildRequires:  perl(Convert::ASN1)
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(GSSAPI)
BuildRequires:  perl(URI::ldap)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(XML::SAX::Writer)
BuildRequires:  perl(MIME::Base64)
Requires:	perl-Authen-SASL >= 2.00
Requires:	perl-XML-Parser
Requires:	perl-Convert-ASN1 >= 0.07
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
The perl-ldap distribution is a collection of perl modules
which provide an object-oriented interface to LDAP servers.

%prep

%setup -q -n %{name}-%{version}

%build
find -name \*.pm | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS README
%{perl_vendorlib}/LWP
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/Net
%{_mandir}/*/*
