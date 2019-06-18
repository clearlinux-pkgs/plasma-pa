#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-pa
Version  : 5.16.1
Release  : 18
URL      : https://download.kde.org/stable/plasma/5.16.1/plasma-pa-5.16.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.16.1/plasma-pa-5.16.1.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.16.1/plasma-pa-5.16.1.tar.xz.sig
Summary  : Plasma applet for audio volume management using PulseAudio
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: plasma-pa-data = %{version}-%{release}
Requires: plasma-pa-lib = %{version}-%{release}
Requires: plasma-pa-license = %{version}-%{release}
Requires: plasma-pa-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : kdeclarative-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kirigami2-dev
BuildRequires : kpackage-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libcanberra-dev
BuildRequires : pkgconfig(gconf-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : plasma-framework-dev
BuildRequires : pulseaudio-dev

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
%setup -q -n plasma-pa-5.16.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560883297
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1560883297
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-pa
cp COPYING %{buildroot}/usr/share/package-licenses/plasma-pa/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/plasma-pa/COPYING.LIB
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/plasma-pa/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang kcm_pulseaudio
%find_lang plasma_applet_org.kde.plasma.volume

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kconf_update/disable_kmix.upd
/usr/share/kconf_update/plasmaVolumeDisableKMixAutostart.pl
/usr/share/kde4/apps/kconf_update/disable_kmix.upd
/usr/share/kde4/apps/kconf_update/plasmaVolumeDisableKMixAutostart.pl
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/Advanced.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/Applications.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/CardListItem.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/DefaultDeviceButton.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/DeviceComboBox.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/DeviceListItem.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/Devices.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/Header.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/ListItemSeperator.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/MuteButton.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/StreamListItem.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/VolumeSlider.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/main.qml
/usr/share/kpackage/kcms/kcm_pulseaudio/metadata.desktop
/usr/share/kpackage/kcms/kcm_pulseaudio/metadata.json
/usr/share/kservices5/kcm_pulseaudio.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.volume.desktop
/usr/share/metainfo/org.kde.plasma.volume.appdata.xml
/usr/share/plasma/plasmoids/org.kde.plasma.volume/contents.rcc
/usr/share/plasma/plasmoids/org.kde.plasma.volume/metadata.json

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/de/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/en/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/plasma-pa/index.docbook
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
/usr/share/doc/HTML/sv/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/plasma-pa/index.docbook
/usr/share/doc/HTML/uk/kcontrol/plasma-pa/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/plasma-pa/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcms/kcm_pulseaudio.so
/usr/lib64/qt5/qml/org/kde/plasma/private/volume/PulseObjectFilterModel.qml
/usr/lib64/qt5/qml/org/kde/plasma/private/volume/libplasma-volume-declarative.so
/usr/lib64/qt5/qml/org/kde/plasma/private/volume/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-pa/COPYING
/usr/share/package-licenses/plasma-pa/COPYING.LIB
/usr/share/package-licenses/plasma-pa/cmake_COPYING-CMAKE-SCRIPTS

%files locales -f kcm_pulseaudio.lang -f plasma_applet_org.kde.plasma.volume.lang
%defattr(-,root,root,-)

