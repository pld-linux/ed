Summary:     GNU Line Editor
Summary(de): GNU-Zeileneditor 
Summary(fr): Éditeur ligne de GNU
Summary(pl): Edytor liniowy GNU
Summary(tr): GNU satýr düzenleyici
Name:        ed
Version:     0.2
Release:     12
Copyright:   GPL
Group:       Applications/Editors
Group(pl):   Aplikacje/Edytory
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:      ed-info.patch
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is the GNU line editor.  It is an implementation of one
of the first editors under *nix.  Some programs rely on it,
but in general you probably don't *need* it.

%description -l de
Dies ist der GNU-Zeileneditor, eine Implementierung einer
der ersten Editoren unter *nix. Manche Programme verlassen sich darauf,
i.a. *brauchen* Sie ihn wahrscheinlich nicht.

%description -l fr
Éditeur ligne de GNU. C'est une implantation de l'un des premiers
éditeurs d'*nix. Certains programmes en ont besoin, mais en
général, vous n'en aurez probablement pas l'utilité.

%description -l pl
Ed jest implementacj± GNU standardowego, pierwszego unixowego edytora.
Czê¶æ starszych programów mo¿e jeszcze korzystaæ z niego ale wiêkszo¶æ
ju¿ prawdopodobnie nie potrzrebuje ed.

%description -l tr
Bu paket UN*X'in en eski metin düzenleyicilerinden birini içermektedir. Bazý
yazýlýmlar hala bu programa gereksinim duymaktadýrlar.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--exec-prefix=/
rm -f ed.info*
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	exec_prefix=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/usr/man/man1/red.1
echo ".so ed.1" > $RPM_BUILD_ROOT/usr/man/man1/red.1
gzip -9fn $RPM_BUILD_ROOT/usr/{info/ed.info*,man/man1/*}

%post
/sbin/install-info /usr/info/ed.info.gz /etc/info-dir

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/ed.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS POSIX README 
%attr(755, root, root) /bin/*
/usr/info/ed.info*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Thu Dec 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-12]
- standarized {un}registering info pages (added ed-info.patch).
- red(1) man page is now maked as nroff include to ed(1),
- added gzipping man pages.

* Mon Dec 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-11]
- standarized {un}registering info pages,
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment.

* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-10]
- fixed --entry text in {un}registering info page for ed in %post %preun.

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2-9]
- added pl translation,
- major modifications of the spec file.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added install-info support
- added BuildRoot
- correct URL in Source line

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
