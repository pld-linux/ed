Summary:	GNU Line Editor
Summary(de):	GNU-Zeileneditor 
Summary(fr):	Éditeur ligne de GNU
Summary(pl):	GNU edytor liniowy 
Summary(tr):	GNU satýr düzenleyici
Name:		ed
Version:	0.2
Release:	15
Copyright:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source:		ftp://prep.ai.mit.edu/pub/gnu/ed/%{name}-%{version}.tar.gz
Patch0:		ed-info.patch
Patch1:		ed-autoconf.patch
Prereq:		/usr/sbin/fix-info-dir
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is the GNU line editor.  It is an implementation of one of the first
editors under *nix. Some programs rely on it, but in general you probably
don't *need* it.

%description -l de
Dies ist der GNU-Zeileneditor, eine Implementierung einer der ersten
Editoren unter *nix. Manche Programme verlassen sich darauf, i.a. *brauchen*
Sie ihn wahrscheinlich nicht.

%description -l fr
Éditeur ligne de GNU. C'est une implantation de l'un des premiers éditeurs
d'*nix. Certains programmes en ont besoin, mais en général, vous n'en aurez
probablement pas l'utilité.

%description -l pl
Ed jest GNU implementacj± standardowego, pierwszego unixowego edytora.
Czê¶æ starszych programów mo¿e jeszcze korzystaæ z niego ale wiêkszo¶æ
ju¿ prawdopodobnie nie potrzebuje ed.

%description -l tr
Bu paket UN*X'in en eski metin düzenleyicilerinden birini içermektedir. Bazý
yazýlýmlar hala bu programa gereksinim duymaktadýrlar.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
chmod +w configure
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr \
	--exec-prefix=/

rm -f ed.info
make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man1/*,%{_infodir}/*info*} \
	NEWS POSIX README

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /bin/*

%{_infodir}/ed.info.gz
%{_mandir}/man1/*
