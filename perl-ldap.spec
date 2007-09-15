%define name perl-ldap
%define version 0.34
%define release %mkrel 2

Summary:	Perl modules for ldap
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://search.cpan.org/dist/%{name}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{name}-%{version}.tar.bz2
License:	GPL or Artistic
Group:		Development/Perl
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

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	perl-Authen-SASL >= 2.00
Requires:	perl-XML-Parser perl-Convert-ASN1 >= 0.07

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS README
%{_mandir}/*/*
%{perl_vendorlib}/LWP
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/Net

