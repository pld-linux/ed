Summary:	GNU Line Editor
Summary(de):	GNU-Zeileneditor
Summary(fr):	Éditeur ligne de GNU
Summary(ja):	GNU ¥é¥¤¥ó¥¨¥Ç¥£¥¿¡£
Summary(pl):	GNU edytor liniowy
Summary(tr):	GNU satýr düzenleyici
Name:		ed
Version:	0.2
Release:	27
License:	GPL
Group:		Applications/Editors
Source0:	ftp://prep.ai.mit.edu/pub/gnu/ed/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-autoconf.patch
Patch2:		%{name}-mkstemp.patch
Patch3:		%{name}-debian.patch
Patch4:		%{name}-configure.patch
URL:		http://www.gnu.org/software/ed/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_exec_prefix	/

%description
This is the GNU line editor. It is an implementation of one of the
first editors under *nix. Some programs rely on it, but in general you
probably don't *need* it.

%description -l de
Dies ist der GNU-Zeileneditor, eine Implementierung einer der ersten
Editoren unter *nix. Manche Programme verlassen sich darauf, i.a.
*brauchen* Sie ihn wahrscheinlich nicht.

%description -l fr
Éditeur ligne de GNU. C'est une implantation de l'un des premiers
éditeurs d'*nix. Certains programmes en ont besoin, mais en général,
vous n'en aurez probablement pas l'utilité.

%description -l ja
ed ¤Ï¹Ô»Ø¸þ¤Î¥Æ¥­¥¹¥È¥¨¥Ç¥£¥¿¤Ç¡¢( ÂÐÏÃÅª¤Ç¤â¥·¥§¥ë¥¹¥¯¥ê¥×¥È·ÐÍ³¤Ç¤â
) ¥Æ¥­¥¹¥È¥Õ¥¡¥¤¥ë¤ÎÀ¸À®¡¢É½¼¨¡¢½¤Àµ¤ËÍÑ¤¤¤é¤ì¤Þ¤¹¡£¼ç¤ÊÌÜÅª¤È¤·¤Æ¤Ï¡¢
¥Õ¥ë¥¹¥¯¥ê¡¼¥ó¥¨¥Ç¥£¥¿ ( Îã¤¨¤Ð emacs ¤ä vi ) ¤Ë¤è¤Ã¤Æ¤Ê¤µ¤ì¤Æ¤¤¤ë
ÄÌ¾ï¤ÎÍøÍÑ¤Ë ed ¤òÃÖ¤­´¹¤¨¤Æ¤­¤¿¤³¤È¤Ç¤¹¡£

ed ¤Ï½é´ü¤Î Unix ¥¨¥Ç¥£¥¿¤Ç¡¢¤¤¤í¤¤¤í¤Ê¥×¥í¥°¥é¥à¤Ë»È¤ï¤ì¤Æ¤­¤Þ¤·¤¿¡£
¤·¤«¤·¡¢°ìÈÌ¤Ë¤ÏÂ¿Ê¬¥¤¥ó¥¹¥È¡¼¥ë¤¹¤ëÉ¬Í×¤Ï¤Ê¤¯¡¢
Â¿Ê¬»È¤¤¤³¤Ê¤¹¤³¤È¤â¤Ê¤¤¤Ç¤·¤ç¤¦¡£

%description -l pl
Ed jest GNU implementacj± standardowego, pierwszego edytora
uniksowego. Czê¶æ starszych programów mo¿e jeszcze z niego korzystaæ,
ale wiêkszo¶æ ju¿ prawdopodobnie go nie potrzebuje.

%description -l tr
Bu paket UN*X'in en eski metin düzenleyicilerinden birini
içermektedir. Bazý yazýlýmlar hala bu programa gereksinim
duymaktadýrlar.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
chmod +w configure
%{__autoconf}
%configure

rm -f ed.info
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf NEWS POSIX README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /bin/*

%{_infodir}/*info*
%{_mandir}/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
