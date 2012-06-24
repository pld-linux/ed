Summary:	GNU Line Editor
Summary(de):	GNU-Zeileneditor 
Summary(fr):	�diteur ligne de GNU
Summary(pl):	GNU edytor liniowy 
Summary(tr):	GNU sat�r d�zenleyici
Name:		ed
Version:	0.2
Release:	17
Copyright:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source:		ftp://prep.ai.mit.edu/pub/gnu/ed/%{name}-%{version}.tar.gz
Patch0:		ed-info.patch
Patch1:		ed-autoconf.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_exec_prefix	/

%description
This is the GNU line editor.  It is an implementation of one of the first
editors under *nix. Some programs rely on it, but in general you probably
don't *need* it.

%description -l de
Dies ist der GNU-Zeileneditor, eine Implementierung einer der ersten
Editoren unter *nix. Manche Programme verlassen sich darauf, i.a. *brauchen*
Sie ihn wahrscheinlich nicht.

%description -l fr
�diteur ligne de GNU. C'est une implantation de l'un des premiers �diteurs
d'*nix. Certains programmes en ont besoin, mais en g�n�ral, vous n'en aurez
probablement pas l'utilit�.

%description -l pl
Ed jest GNU implementacj� standardowego, pierwszego edytora uniksowego.
Cz�� starszych program�w mo�e jeszcze z niego korzysta�, ale wi�kszo��
ju� prawdopodobnie go nie potrzebuje.

%description -l tr
Bu paket UN*X'in en eski metin d�zenleyicilerinden birini i�ermektedir. Baz�
yaz�l�mlar hala bu programa gereksinim duymaktad�rlar.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
chmod +w configure
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure

rm -f ed.info
make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man1/*,%{_infodir}/*info*} \
	NEWS POSIX README

%post
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ -x /usr/sbin/fix-info-dir ] && /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /bin/*

%{_infodir}/ed.info.gz
%{_mandir}/man1/*
