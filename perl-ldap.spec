%define upstream_name    ldap
%define upstream_version 0.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl modules for ldap
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{name}-%{upstream_version}.tar.gz
Patch0:		perl-ldap-make_test_config_fixes.diff

BuildRequires:	openldap-servers
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

BuildArch:	noarch

%description
The perl-ldap distribution is a collection of perl modules
which provide an object-oriented interface to LDAP servers.

%prep
%setup -q -n %{name}-%{upstream_version}
%patch0 -p1

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

%build
find -name \*.pm | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc CREDITS README contrib
%{perl_vendorlib}/LWP
%{perl_vendorlib}/Bundle
%{perl_vendorlib}/Net
%{_mandir}/*/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.400.100-2mdv2011.0
+ Revision: 667468
- mass rebuild

* Fri Mar 26 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.400.100-1mdv2010.1
+ Revision: 527738
- update to 0.4001

* Fri Mar 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 518487
- update to 0.40

* Tue Nov 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2009.1
+ Revision: 299826
- update to new version 0.39

* Mon Sep 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.0
+ Revision: 286671
- new version (including previous patches)

* Thu Sep 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-4mdv2009.0
+ Revision: 285728
- fix previous patch when no control is used

* Mon Sep 15 2008 Buchan Milne <bgmilne@mandriva.org> 0.37-3mdv2009.0
+ Revision: 284931
- Add patch from git supporting controls for set_password

* Thu Sep 04 2008 Buchan Milne <bgmilne@mandriva.org> 0.37-2mdv2009.0
+ Revision: 280798
- Add patches from git fixing password policy expiry and grace authentication subs

* Thu Sep 04 2008 Buchan Milne <bgmilne@mandriva.org> 0.37-1mdv2009.0
+ Revision: 280752
- update to new version 0.37

* Thu Jun 19 2008 Buchan Milne <bgmilne@mandriva.org> 0.36-1mdv2009.0
+ Revision: 226212
- update to new version 0.36

* Thu Jun 19 2008 Buchan Milne <bgmilne@mandriva.org> 0.34-5mdv2009.0
+ Revision: 226209
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.34-4mdv2009.0
+ Revision: 223806
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.34-3mdv2008.1
+ Revision: 180848
- added P0 to make the tests pass

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.34-3mdv2008.0
+ Revision: 92382
- enable all the tests
- fix build deps (perl(XML::Filter::BufferText))
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild

  + Olivier Thauvin <nanardon@mandriva.org>
    - 0.34


* Mon May 01 2006 Scott Karns <scottk@mandriva.org> 0.33-3mdk
- Update source URL and BuildRequires to meet Mandriva perl packaging
  policies

* Tue Feb 21 2006 Stefan van der Eijk <stefan@eijk.nu> 0.33-2mdk
- BuildRequires

* Mon Feb 06 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.33-1mdk
- 0.33, and get rid of real_version macro, using upstream version instead
- Fix and shorten description
- Fix URL, licence and permissions

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.31-2mdk
- own dirs

* Wed Jan 28 2004 Vincent Guardiola <vguardiola@mandrakesoft.com> 0.31-1mdk
- 0.31.

* Thu Aug 21 2003 François Pons <fpons@mandrakesoft.com> 0.29-1mdk
- 0.29.

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.28-2mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- use %%makeinstall_std macro
- drop $RPM_OPT_FLAGS, noarch..
- quiet setup

* Fri May 23 2003 François Pons <fpons@mandrakesoft.com> 0.28-1mdk
- 0.28.

