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
BuildRequires: kf5-kcrash-devel >= %{kf5_version}
Requires: qt5-qtquickcontrols2 >= %{qt5_version}
Requires: qt5-qtbase >= %{qt5_version}
Requires: kf5-ki18n >= %{kf5_version}
Requires: kf5-libksane >= %{kf5_version}
Requires: kf5-kirigami2 >= %{kf5_version}
Requires: kf5-plasma >= %{kf5_version}
Requires: kf5-kcrash >= %{kf5_version}

%description
Skanpage is a modern scanning application.

%prep
%setup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%files
%{_datadir}/applications/org.kde.skanpage.desktop
%{_datadir}/metainfo/org.kde.skanpage.appdata.xml
%{_datadir}/qlogging-categories5/skanpage.categories
%{_bindir}/skanpage
%{_datadir}/icons/hicolor/scalable/apps/skanpage.svg
%{_datadir}/icons/hicolor/48x48/apps/skanpage.png

%changelog
* Sun Feb 27 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 1.0
- Packaging of skanpage 1.0
