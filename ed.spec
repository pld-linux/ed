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
Patch:		ed-info.patch
Prereq:		/sbin/install-info
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
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr \
	--exec-prefix=/

rm -f ed.info
make 

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr \
    exec_prefix=$RPM_BUILD_ROOT \
    mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
    infodir=$RPM_BUILD_ROOT%{_infodir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/red.1
echo .so ed.1 > $RPM_BUILD_ROOT%{_mandir}/man1/red.1

gzip -9nf $RPM_BUILD_ROOT/usr/{share/man/man1/*,share/info/*info*} \
	NEWS POSIX README

%post
/sbin/install-info %{_infodir}/ed.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/ed.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /bin/*

%{_infodir}/ed.info.gz
%{_mandir}/man1/*

%changelog
* Mon Jun 07 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [0.2-15]
- spec cleanup

* Thu Apr 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-14]
- recompiles on new rpm.

* Thu Apr  1 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-13]
- removed man group from man pages,
- added gzipping %doc,
- removed striping binaries (added LDFLAGS="-s" to ./configure env),
- added ed-info.patch.

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2-6d]
- translation modified for pl,
- restricted ELF binary permission,
- major modifications of the spec file.

* Thu Jul 23 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.2-6]
- build against glibc-2.1.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added install-info support
- added BuildRoot
- correct URL in Source line

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
