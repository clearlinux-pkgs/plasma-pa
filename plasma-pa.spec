#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-pa
Version  : 6.2.0
Release  : 106
URL      : https://download.kde.org/stable/plasma/6.2.0/plasma-pa-6.2.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.2.0/plasma-pa-6.2.0.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.2.0/plasma-pa-6.2.0.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: plasma-pa-data = %{version}-%{release}
Requires: plasma-pa-lib = %{version}-%{release}
Requires: plasma-pa-license = %{version}-%{release}
Requires: plasma-pa-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : kirigami-addons-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : libcanberra-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pulseaudio-qt-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the plasma-pa package.
Group: Data

%description data
data components for the plasma-pa package.


%package doc
Summary: doc components for the plasma-pa package.
Group: Documentation

%description doc
doc components for the plasma-pa package.


%package lib
Summary: lib components for the plasma-pa package.
Group: Libraries
Requires: plasma-pa-data = %{version}-%{release}
Requires: plasma-pa-license = %{version}-%{release}

%description lib
lib components for the plasma-pa package.


%package license
Summary: license components for the plasma-pa package.
Group: Default

%description license
license components for the plasma-pa package.


%package locales
Summary: locales components for the plasma-pa package.
Group: Default

%description locales
locales components for the plasma-pa package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n plasma-pa-6.2.0
cd %{_builddir}/plasma-pa-6.2.0
pushd ..
cp -a plasma-pa-6.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728613469
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728613469
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-pa
cp %{_builddir}/plasma-pa-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-pa/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-pa/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-pa/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-pa/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-pa/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/plasma-pa/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-pa/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-pa/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-pa/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-pa/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-pa-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-pa/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-pa-%{version}/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/plasma-pa/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcm_pulseaudio
%find_lang plasma_applet_org.kde.plasma.volume
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_pulseaudio.desktop
/usr/share/metainfo/org.kde.plasma.volume.appdata.xml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/DeviceListItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/HorizontalStackView.qml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/ListItemBase.qml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/SmallToolButton.qml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/StreamListItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/VolumeSlider.qml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/metadata.json

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/de/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/en/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/es/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/id/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/id/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/it/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/nl/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/pt/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/ru/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/sl/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/sl/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/sv/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/tr/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/tr/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/uk/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/plasma-pa/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libplasma-volume.so.6.2.0
/V3/usr/lib64/qt6/plugins/kf6/kded/audioshortcutsservice.so
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_pulseaudio.so
/V3/usr/lib64/qt6/qml/org/kde/plasma/private/volume/libplasma-volume-declarative.so
/usr/lib64/libplasma-volume.so.6
/usr/lib64/libplasma-volume.so.6.2.0
/usr/lib64/qt6/plugins/kf6/kded/audioshortcutsservice.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_pulseaudio.so
/usr/lib64/qt6/qml/org/kde/plasma/private/volume/PulseObjectFilterModel.qml
/usr/lib64/qt6/qml/org/kde/plasma/private/volume/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/plasma/private/volume/libplasma-volume-declarative.so
/usr/lib64/qt6/qml/org/kde/plasma/private/volume/plasma-volume-declarative.qmltypes
/usr/lib64/qt6/qml/org/kde/plasma/private/volume/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-pa/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/plasma-pa/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/plasma-pa/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/plasma-pa/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-pa/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/plasma-pa/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/plasma-pa/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-pa/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/plasma-pa/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/plasma-pa/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f kcm_pulseaudio.lang -f plasma_applet_org.kde.plasma.volume.lang
%defattr(-,root,root,-)

