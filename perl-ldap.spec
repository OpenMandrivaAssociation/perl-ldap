%define modname ldap
%define modver	0.44

Summary:	Perl modules for ldap
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{name}-%{modver}.tar.gz
Patch0:	perl-ldap-make_test_config_fixes.diff
BuildArch:	noarch
BuildRequires:	openldap-servers
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(CPAN)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Convert::ASN1)
BuildRequires:	perl(Encode)
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(HTTP::Negotiate)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(IO::Socket::INET6)
BuildRequires:	perl(LWP::MediaTypes)
BuildRequires:	perl(LWP::Protocol)
BuildRequires:	perl(Authen::SASL) >= 2.00
BuildRequires:	perl(URI::ldap) >= 1.1
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(XML::SAX::Base)
BuildRequires:	perl(XML::SAX::Writer)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl-devel

%description
The perl-ldap distribution is a collection of perl modules
which provide an object-oriented interface to LDAP servers.

%prep
%setup -qn %{name}-%{modver}
%apply_patches

# perl path
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"
chmod 644 contrib/*

cat > test.cfg << EOF
\$SERVER_EXE = "%{_sbindir}/slapd";
\$SERVER_TYPE = "openldap2+ssl+ipc+sasl";
\$SLAPD_DB = "bdb";
\$HOST = "127.0.0.1";
\$SCHEMA_DIR = "%{_datadir}/openldap/schema";
\$EXTERNAL_TESTS = 0;
1;
EOF
find -name \*.pm | xargs chmod 644

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
#make test

%install
%make_install

%files
%doc CREDITS README contrib
%{perl_vendorlib}/LWP
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/Net
%{_mandir}/man3/*

