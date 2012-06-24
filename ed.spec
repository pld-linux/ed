Summary:	GNU Line Editor
Summary(de):	GNU-Zeileneditor
Summary(fr):	�diteur ligne de GNU
Summary(ja):	GNU �饤�󥨥ǥ�����
Summary(pl):	GNU edytor liniowy
Summary(tr):	GNU sat�r d�zenleyici
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
�diteur ligne de GNU. C'est une implantation de l'un des premiers
�diteurs d'*nix. Certains programmes en ont besoin, mais en g�n�ral,
vous n'en aurez probablement pas l'utilit�.

%description -l ja
ed �ϹԻظ��Υƥ����ȥ��ǥ����ǡ�( ����Ū�Ǥ⥷���륹����ץȷ�ͳ�Ǥ�
) �ƥ����ȥե������������ɽ�����������Ѥ����ޤ��������Ū�Ȥ��Ƥϡ�
�ե륹���꡼�󥨥ǥ��� ( �㤨�� emacs �� vi ) �ˤ�äƤʤ���Ƥ���
�̾�����Ѥ� ed ���֤������Ƥ������ȤǤ���

ed �Ͻ���� Unix ���ǥ����ǡ�������ʥץ����˻Ȥ��Ƥ��ޤ�����
�����������̤ˤ�¿ʬ���󥹥ȡ��뤹��ɬ�פϤʤ���
¿ʬ�Ȥ����ʤ����Ȥ�ʤ��Ǥ��礦��

%description -l pl
Ed jest GNU implementacj� standardowego, pierwszego edytora
uniksowego. Cz�� starszych program�w mo�e jeszcze z niego korzysta�,
ale wi�kszo�� ju� prawdopodobnie go nie potrzebuje.

%description -l tr
Bu paket UN*X'in en eski metin d�zenleyicilerinden birini
i�ermektedir. Baz� yaz�l�mlar hala bu programa gereksinim
duymaktad�rlar.

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
