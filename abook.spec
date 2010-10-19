%define		_rel	pre2
#
Summary:	Text-based addressbook program for mutt
Summary(pl.UTF-8):	Tekstowa książka adresowa dla klienta pocztowego mutt
Name:		abook
Version:	0.6.0
Release:	0.%{_rel}.1
License:	GPL
Group:		Applications/Mail
Source0:	http://abook.sourceforge.net/devel/%{name}-%{version}%{_rel}.tar.gz
# Source0-md5:	1e4a7210b3507db7b3d47ee7a2457934
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-tinfo_link.patch
Patch2:		%{name}-vcard_import.patch
URL:		http://abook.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abook is a text-based addressbook program designed to use with mutt
mail client.

%description -l pl.UTF-8
Abook to pracująca w trybie tekstowym książka adresowa zaprojektowana
do użycia z programem pocztowym mutt.

%prep
%setup -q -n %{name}-%{version}%{_rel}
%patch0 -p1
%patch1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
