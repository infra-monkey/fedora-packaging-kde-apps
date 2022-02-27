%global kf5_version 5.81.0
%global qt5_version 5.15.0
Name:     plasmatube
Version:  22.02
Release:  1%{?dist}
Summary:  KDE Plasma scanning application
License:  GPLv3+
URL:      https://invent.kde.org/plasma-mobile/%{name}
Source0:   https://invent.kde.org/plasma-mobile/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires: cmake >= 3.16
BuildRequires: qt5-qtquickcontrols2-devel  >= %{qt5_version}
BuildRequires: qt5-qtbase-devel  >= %{qt5_version}
BuildRequires: qt5-qtmultimedia-devel  >= %{qt5_version}
BuildRequires: qt5-qtsvg-devel >= %{qt5_version}
BuildRequires: kf5-ki18n-devel >= %{kf5_version}
BuildRequires: kf5-rpm-macros >= %{kf5_version}
BuildRequires: kf5-kirigami2-devel >= %{kf5_version}
BuildRequires: kf5-plasma-devel >= %{kf5_version}
Requires: qt5-qtquickcontrols2 >= %{qt5_version}
Requires: qt5-qtbase >= %{qt5_version}
Requires: qt5-qtsvg >= %{qt5_version}
Requires: qt5-qtmultimedia >= %{qt5_version}
Requires: kf5-ki18n >= %{kf5_version}
Requires: kf5-kirigami2 >= %{kf5_version}
Requires: kf5-plasma >= %{kf5_version}

%description
PlasmaTube is KDE Plasma native youtube viewer.

%prep
%setup -n %{name}-v%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%files
%{_datadir}/applications/org.kde.plasmatube.desktop
%{_datadir}/metainfo/org.kde.plasmatube.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.plasmatube.svg
%{_bindir}/plasmatube

%changelog
* Sun Feb 27 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 22.02
- Packaging of plasmatube 22.02
