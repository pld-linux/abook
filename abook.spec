Summary:	Text-based addressbook program
Name:		abook
Version:	0.4.11
Release:	1
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	ftp://abook.sourceforge.net/pub/abook/%{name}-%{version}.tar.gz
URL:		http://members.linuxstart.com/~jheinonen/abook/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abook is a text-based addressbook program designed to use with mutt
mail client.

%prep
%setup  -q
%build
autoheader;autoconf;automake; 
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog NEWS README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
