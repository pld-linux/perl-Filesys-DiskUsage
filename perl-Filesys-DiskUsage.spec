#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Filesys
%define	pnam	DiskUsage
Summary:	Filesys::DiskUsage - Estimate file space usage (similar to `du`)
#Summary(pl.UTF-8):	
Name:		perl-Filesys-DiskUsage
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/M/MA/MANWAR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8eb2e83236fb039503c6f444fed4c4c2
URL:		https://metacpan.org/release/Filesys-DiskUsage
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Warn
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Estimate file space usage (similar to du)

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/fdu
%{perl_vendorlib}/Filesys/*.pm
%{_mandir}/man1/fdu.1p*
%{_mandir}/man3/*
