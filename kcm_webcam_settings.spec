%global kf5_version 5.85.0
%global qt5_version 5.15.2
Name:     kcm_webcam_settings
Version:  0.0.6
Release:  1
Summary:  KDE Plasma system-settings module to configure your webcam
License:  GPLv3+
URL:      https://github.com/infra-monkey/kcm_webcam_settings
Source0:   https://github.com/infra-monkey/kcm_webcam_settings/archive/refs/tags/%{version}.tar.gz
BuildRequires: cmake >= 3.16
BuildRequires: kf5-ki18n-devel >= %{kf5_version}
BuildRequires: kf5-kcmutils-devel >= %{kf5_version}
BuildRequires: kf5-kdeclarative-devel >= %{kf5_version}
BuildRequires: qt5-qtsvg-devel >= %{qt5_version}
BuildRequires: kf5-plasma-devel >= %{kf5_version}
BuildRequires: qt5-qtmultimedia-devel >= %{qt5_version}
BuildRequires: kf5-rpm-macros >= %{kf5_version}
Requires: v4l-utils
Requires: kf5-ki18n >= %{kf5_version}
Requires: kf5-kcmutils >= %{kf5_version}
Requires: kf5-kdeclarative >= %{kf5_version}
Requires: qt5-qtsvg >= %{qt5_version}
Requires: kf5-plasma >= %{kf5_version}
Requires: qt5-qtmultimedia >= %{qt5_version}

%description
This module for systemsettings in KDE Plasma 5.23+ allows to configure Video4Linux (Webcam devices) settings such as brightness, saturation, auto-focus or even absolute zomm when the controles are exposed by the device. The default resolution and pixel format can also be adjusted. Note that not all software will respect the resolution and format.

%prep
%setup -n %{name}-%{version}

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
* Fri Jul 29 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 0.0.6
- Seg fault since update to KF5.93

* Mon Feb 24 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 0.0.5
- Optimze code when loading the v4l2 controls

* Mon Feb 20 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 0.0.4
- Enhancement: allow preview of the webcam output in the ui
- Bug: Digital Zoom not applicable in some cases
- Enhancement: Add FR internationalization

* Mon Feb 15 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 0.0.3
- Enhancement: add settings for autofocus and focus
- Enhancement: move the device selection from a dropdown menu to a listview.
- Enhancement: add device information.
- Fix: some resolutions are duplicated in the format selection menu.
- Fix: spec file uses hardcoded path for the %files section

* Mon Feb 09 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 0.0.2
- Fix: systemsettings would crash if no webcam is connected
- Enhancement: update v4l2 controls on the fly when the cursor is moved
- Enhancement: enable packaging on multiple architectures/versions in fedora copr

* Mon Feb 07 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 0.0.1
- Initial version of the package