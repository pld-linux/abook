Summary:	Text-based addressbook program for mutt
Summary(pl):	Tekstowa ksi±¿ka adresowa dla klienta pocztowego mutt
Name:		abook
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/abook/%{name}-%{version}.tar.gz
# Source0-md5:	3aaddb943845a875e53a0064b76a2f80
Patch0:		%{name}-etc_dir.patch
URL:		http://abook.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abook is a text-based addressbook program designed to use with mutt
mail client.

%description -l pl
Abook to pracuj±ca w trybie tekstowym ksi±¿ka adresowa zaprojektowana
do u¿ycia z programem pocztowym mutt.

%prep
%setup -q
#%patch0 -p1

%build
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
