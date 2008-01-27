# TODO
# - adjust arith and crop patches to apply on ljpeg
#
# Conditional build:
%bcond_with	arith	# arithmetic coding support (changes error codes in ABI, patent problems somewhere)
%bcond_with	crop	# lossless cropping support (changes error codes in ABI)
#
Summary:	Library for handling different JPEG files, including lossless
Summary(pl.UTF-8):	Biblioteka do manipulacji plikami w formacie JPEG włącznie z bezstratnymi
Name:		libljpeg
Version:	6b
Release:	27
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
# Source0-md5:	dbd5f3b47ed13132f04c685d608a7547
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/libjpeg-non-english-man-pages.tar.bz2
# Source1-md5:	d6342c015a489de275ada637a77dc2b0
Source2:	ftp://ftp.simplesystems.org/pub/ImageMagick/delegates/ljpeg-6b.tar.gz
# Source2-md5:	4f13107f5365803b0f2d1db1b33eb285
Patch0:		libjpeg-DESTDIR.patch
Patch1:		libjpeg-arm.patch
Patch2:		libjpeg-include.patch
Patch3:		libjpeg-c++.patch
Patch4:		libjpeg-libtool.patch
Patch5:		%{name}-libname.patch
Patch6:		%{name}-fix.patch
# from http://sylvana.net/jpeg-ari/jpeg-ari-28mar98.tar.gz
Patch7:		libjpeg-arith.patch
# from http://sylvana.net/jpegcrop/croppatch.tar.gz
Patch8:		libjpeg-crop.patch
URL:		http://www.ijg.org/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpeg package contains a library of functions for manipulating
JPEG images, including those with lossless compression.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do manipulacji plikami JPEG,
włącznie z kompresowanymi algorytmem bezstratnym.

%package devel
Summary:	Headers for developing programs using libljpeg
Summary(de.UTF-8):	Header zum Entwickeln von Programmen mit libljpeg
Summary(es.UTF-8):	Archivos de inclusión para desarrollar programas usando libljpeg
Summary(pl.UTF-8):	Pliki nagłówkowe libljpeg
Summary(pt_BR.UTF-8):	Arquivos de inclusão para desenvolver programas usando libljpeg
Summary(ru.UTF-8):	Хедеры для разработки программ, использующих libljpeg
Summary(tr.UTF-8):	libljpeg için geliştirme kitaplıkları ve başlık dosyaları
Summary(uk.UTF-8):	Хедери для розробки програм, що використовують libljpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libljpeg-devel package includes the header files necessary for
developing programs which will manipulate JPEG files using the libljpeg
library.

%description devel -l de.UTF-8
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von JPEG-Grafiken, einschließlich Dokumentation, zu
entwickeln.

%description devel -l es.UTF-8
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen imágenes JPEG, incluso documentación.

%description devel -l fr.UTF-8
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images JPEG, et comprend la documentation.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do programowania z wykorzystaniem
biblioteki libljpeg. Zawiera także dokumentację.

%description devel -l pt_BR.UTF-8
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens JPEG, incluindo documentação.

%description devel -l ru.UTF-8
В этом пакете содержится все необходимое для разработки программ,
которые работают с JPEG-изображениями включая документацию.

%description devel -l tr.UTF-8
Bu paket, JPEG resimlerini işleyen programlar geliştirmeniz için
gereken başlık dosyalarını, kitaplıkları ve ilgili yardım belgelerini
içerir.

%description devel -l uk.UTF-8
Цей пакет містить все необхідне для розробки програм, котрі працюють з
JPEG-зображеннями, включаючи документацію.

%package static
Summary:	Static library for developing programs using libljpeg
Summary(pl.UTF-8):	Biblioteka statyczna libljpeg
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libljpeg
Summary(ru.UTF-8):	Статическая библиотека для программирования с libljpeg
Summary(uk.UTF-8):	Статична бібліотека для програмування з libljpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for developing programs using libljpeg.

%description static -l pl.UTF-8
Statyczna biblioteka libljpeg.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libljpeg.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих libljpeg.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для написання
програм, що використовують libljpeg.

%package progs
Summary:	Simple clients for manipulating JPEG images
Summary(de.UTF-8):	Einfachen Clients zur Manipulation von JPEG
Summary(fr.UTF-8):	Clients simples pour manipuler des images JPEG
Summary(pl.UTF-8):	Kilka prostych programów do manipulowania na plikach JPEG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libjpeg-progs

%description progs
Simple clients for manipulating JPEG images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l de.UTF-8
Einfachen Clients zur Manipulation von JPEG.

%description progs -l fr.UTF-8
Clients simples pour manipuler des images JPEG.

%description progs -l pl.UTF-8
Kilka prostych programów do obróbki plików JPEG, w tym: cjpeg, djpeg,
jpegtran, rdjpgcom i wrjpgcom. djpeg dekompresuje plik JPEG do
zwykłego pliku obrazu, jpegtran potrafi wykonywać różne
przekształcenia na plikach JPEG. rdjpgcom wyświetla komentarze
tekstowe dołączone do pliku JPEG, a wrjpgcom wstawia takie komentarze.

%prep
%setup -q -n jpeg-%{version} -a2
%patch6 -p1
%{__patch} -s -p0 < ljpeg-6b.patch
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%{?with_arith:%patch6 -p1}
%{?with_crop:%patch7 -p1}

cp -f %{_datadir}/libtool/config.sub .

%build
%configure \
	--enable-shared \
	--enable-static

%{__make} \
	libdir=%{_libdir}

LD_PRELOAD=$PWD/.libs/%{name}.so \
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/ljpeg,%{_bindir},%{_mandir}/man1}

%{__make} install install-headers install-lib \
	libdir=%{_libdir} \
	includedir=%{_includedir}/ljpeg \
	DESTDIR=$RPM_BUILD_ROOT

# remove HAVE_STD{DEF,LIB}_H
# (not necessary but may generate warnings confusing autoconf)
(cd $RPM_BUILD_ROOT%{_includedir}/ljpeg
grep -v 'HAVE_STD..._H' jconfig.h > jconfig.h.new
mv -f jconfig.h.new jconfig.h
)

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README change.log %{?with_arith:README.arithmetic}
%attr(755,root,root) %{_libdir}/libljpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libljpeg.so.62

%files devel
%defattr(644,root,root,755)
%doc {libjpeg,structure}.doc
%attr(755,root,root) %{_libdir}/libljpeg.so
%{_libdir}/libljpeg.la
%{_includedir}/ljpeg

%files static
%defattr(644,root,root,755)
%{_libdir}/libljpeg.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cjpeg
%attr(755,root,root) %{_bindir}/djpeg
%attr(755,root,root) %{_bindir}/jpegtran
%attr(755,root,root) %{_bindir}/rdjpgcom
%attr(755,root,root) %{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*
%lang(fi) %{_mandir}/fi/man1/cjpeg.1*
%lang(pl) %{_mandir}/pl/man1/cjpeg.1*
%lang(pl) %{_mandir}/pl/man1/djpeg.1*
