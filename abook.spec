Summary:	Text-based addressbook program for mutt
Summary(pl):	Tekstowa ksi±¿ka adresowa dla klienta pocztowego mutt
Name:		abook
Version:	0.5.6
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/abook/%{name}-%{version}.tar.gz
# Source0-md5:	87d25df96864a7c507a4965e6d1da49d
Patch0:		%{name}-home_etc.patch
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

%description -l pl
Abook to pracuj±ca w trybie tekstowym ksi±¿ka adresowa zaprojektowana
do u¿ycia z programem pocztowym mutt.

%prep
%setup -q
%patch0 -p1

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
