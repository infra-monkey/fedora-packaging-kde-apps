%global kf5_version 5.87.0
%global qt5_version 5.15.2
Name:     skanpage
Version:  1.0
Release:  1%{?dist}
Summary:  KDE Plasma scanning application
License:  GPLv3+
URL:      https://invent.kde.org/utilities/%{name}
Source0:   https://invent.kde.org/utilities/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake >= 3.16
BuildRequires: qt5-qtquickcontrols2-devel  >= %{qt5_version}
BuildRequires: qt5-qtbase-devel  >= %{qt5_version}
BuildRequires: kf5-ki18n-devel >= %{kf5_version}
BuildRequires: kf5-rpm-macros >= %{kf5_version}
BuildRequires: kf5-libksane-devel >= %{kf5_version}
BuildRequires: kf5-kirigami2-devel >= %{kf5_version}
BuildRequires: kf5-plasma-devel >= %{kf5_version}
Requires: qt5-qtquickcontrols2 >= %{qt5_version}
Requires: qt5-qtbase >= %{qt5_version}
Requires: kf5-ki18n >= %{kf5_version}
Requires: kf5-libksane >= %{kf5_version}
Requires: kf5-kirigami2 >= %{kf5_version}
Requires: kf5-plasma >= %{kf5_version}

%description
Skanpage is a modern scanning application.

%prep
#{{{ git_dir_setup_macro }}}
%setup

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
* Mon Feb 27 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 1.0
- Packaging of skapage 1.0