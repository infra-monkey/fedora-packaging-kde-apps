%global kf5_version 5.91.0
%global qt5_version 5.15.2
Name:     {{{ git_dir_name }}}
Version:  1.0.0
Release:  1%{?dist}
Summary:  KDE Plasma scanning application
License:  GPLv3+
URL:      https://invent.kde.org/utilities/skanpage
Source:   {{{ git_dir_pack }}}
#BuildArch: x86_64
BuildRequires: cmake >= 3.16
BuildRequires: kf5-ki18n-devel >= %{kf5_version}
BuildRequires: kf5-kcmutils-devel >= %{kf5_version}
BuildRequires: kf5-kdeclarative-devel >= %{kf5_version}
BuildRequires: qt5-qtsvg-devel >= %{qt5_version}
BuildRequires: kf5-plasma-devel >= %{kf5_version}
BuildRequires: qt5-qtmultimedia-devel >= %{qt5_version}
BuildRequires: kf5-rpm-macros >= %{kf5_version_min}
Requires: kf5-ki18n >= %{kf5_version}
Requires: kf5-kcmutils >= %{kf5_version}
Requires: kf5-kdeclarative >= %{kf5_version}
Requires: qt5-qtsvg >= %{qt5_version}
Requires: kf5-plasma >= %{kf5_version}
Requires: qt5-qtmultimedia >= %{qt5_version}

%description
Skanpage is a modern scanning application.

%prep
{{{ git_dir_setup_macro }}}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%files
%{_datadir}/polkit-1/actions/kcm.webcam.settings.udevhelper.policy
%{_kf5_libexecdir}/kauth/udevhelper
%{_datadir}/dbus-1/system.d/kcm.webcam.settings.udevhelper.conf
%{_datadir}/dbus-1/system-services/kcm.webcam.settings.udevhelper.service
%{_qt5_plugindir}/kcms/kcm_webcam_settings.so
%{_datadir}/kservices5/kcm_webcam_settings.desktop
%{_datadir}/kpackage/kcms/kcm_webcam_settings
%{_datadir}/kpackage/kcms/kcm_webcam_settings/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_webcam_settings/contents
%{_datadir}/kpackage/kcms/kcm_webcam_settings/contents/ui
%{_datadir}/kpackage/kcms/kcm_webcam_settings/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_webcam_settings/metadata.json
%{_datadir}/locale/fr
%{_datadir}/locale/fr/LC_MESSAGES
%{_datadir}/locale/fr/LC_MESSAGES/kcm_webcam_settings.mo

%changelog
* Mon Feb 27 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 1.0.0
- Packaging of skapage 1.0.0