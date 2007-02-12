Summary:	GNU Line Editor
Summary(de.UTF-8):   GNU-Zeileneditor
Summary(es.UTF-8):   Editor de líneas de la GNU
Summary(fr.UTF-8):   Éditeur ligne de GNU
Summary(ja.UTF-8):   GNU ラインエディタ。
Summary(pl.UTF-8):   GNU edytor liniowy
Summary(pt_BR.UTF-8):   Editor de linhas da GNU
Summary(ru.UTF-8):   Строчный редактор GNU
Summary(tr.UTF-8):   GNU satır düzenleyici
Summary(uk.UTF-8):   Рядковий редактор GNU
Name:		ed
Version:	0.2
Release:	36
License:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.gnu.org/pub/gnu/ed/%{name}-%{version}.tar.gz
# Source0-md5:	ddd57463774cae9b50e70cd51221281b
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	13a5459ddffbd7f04aa3d67fce0d2134
Patch0:		%{name}-info.patch
Patch1:		%{name}-autoconf.patch
Patch2:		%{name}-mkstemp.patch
Patch3:		%{name}-debian.patch
Patch4:		%{name}-configure.patch
Patch5:		%{name}-regex.patch
URL:		http://www.gnu.org/software/ed/
BuildRequires:	autoconf
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_bindir		/bin

%description
This is the GNU line editor. It is an implementation of one of the
first editors under *nix. Some programs rely on it, but in general you
probably don't *need* it.

%description -l de.UTF-8
Dies ist der GNU-Zeileneditor, eine Implementierung einer der ersten
Editoren unter *nix. Manche Programme verlassen sich darauf, i.a.
*brauchen* Sie ihn wahrscheinlich nicht.

%description -l es.UTF-8
Este es GNU editor de línea. Es un soporte a uno de los primeros
editores para *nix. Algunos de los programas cuentan con él, pero de
manera general, es muy probable que no lo *necesites*.

%description -l fr.UTF-8
Éditeur ligne de GNU. C'est une implantation de l'un des premiers
éditeurs d'*nix. Certains programmes en ont besoin, mais en général,
vous n'en aurez probablement pas l'utilité.

%description -l ja.UTF-8
ed は行指向のテキストエディタで、( 対話的でもシェルスクリプト経由でも
) テキストファイルの生成、表示、修正に用いられます。主な目的としては、
フルスクリーンエディタ ( 例えば emacs や vi ) によってなされている
通常の利用に ed を置き換えてきたことです。

ed は初期の Unix エディタで、いろいろなプログラムに使われてきました。
しかし、一般には多分インストールする必要はなく、
多分使いこなすこともないでしょう。

%description -l pl.UTF-8
Ed jest GNU implementacją standardowego, pierwszego edytora
uniksowego. Część starszych programów może jeszcze z niego korzystać,
ale większość już prawdopodobnie go nie potrzebuje.

%description -l pt_BR.UTF-8
Este é o GNU editor de linha. É uma implementação de um dos primeiros
editores para *nix. Alguns programas contam com ele, mas no geral você
provavelmente não irá *precisar* dele.

%description -l uk.UTF-8
Ed - це рядково-орієнтований текстовий редактор, що використовується
для створення, показу та модифікації текстових файлів (як
інтерактивно, так і зі скриптів). Для більшості цілей ed був замінений
повноекранними редакторами (наприклад, joe, vi, emacs).

%description -l tr.UTF-8
Bu paket UN*X'in en eski metin düzenleyicilerinden birini
içermektedir. Bazı yazılımlar hala bu programa gereksinim
duymaktadırlar.

%description -l ru.UTF-8
Ed - это строчно-ориентированный текстовый редактор, используемый для
создания, показа и модификации текстовых файлов (как интерактивно, так
и при помощи скриптов). Для большинства целей ed был заменен
полноэкранными редакторами (например, joe, vi, emacs).

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
chmod +w configure
%{__autoconf}
%configure

rm -f ed.info
rm -f stamp-h.in
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS POSIX README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
