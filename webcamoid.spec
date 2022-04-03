%global qt5_version 5.15.2
Name:     webcamoid
Version:  9.0.0
Release:  1%{?dist}
Summary:  Virtual Webcam Application
License:  GPLv3+
URL:      https://github.com/%{name}/%{name}
Source0:   https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires: cmake >= 3.16
BuildRequires: alsa-lib-devel
BuildRequires: ccache
BuildRequires: clang
BuildRequires: ffmpeg-devel
BuildRequires: file
BuildRequires: gcc-c++
BuildRequires: gstreamer1-plugins-base
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gstreamer1-plugins-good
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: kmod-devel
BuildRequires: libv4l-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: pipewire-devel >= 0.3.0
BuildRequires: pulseaudio-libs-devel
BuildRequires: qt5-linguist >= %{qt5_version}
BuildRequires: qt5-qtdeclarative-devel >= %{qt5_version}
BuildRequires: qt5-qtquickcontrols2-devel >= %{qt5_version}
BuildRequires: qt5-qtsvg-devel >= %{qt5_version}
BuildRequires: qt5-qttools-devel >= %{qt5_version}
BuildRequires: qt5-qtwayland >= %{qt5_version}
BuildRequires: vlc-core
BuildRequires: vlc-devel
BuildRequires: which
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: xorg-x11-xauth
BuildRequires: dbus-libs
BuildRequires: fontconfig
BuildRequires: libX11-xcb
BuildRequires: libXext
BuildRequires: libXrender
BuildRequires: libglvnd-glx
BuildRequires: libxcb
BuildRequires: libxkbcommon
BuildRequires: libxkbcommon-x11
Requires: qt5-linguist >= %{qt5_version}
Requires: qt5-qtdeclarative >= %{qt5_version}
Requires: qt5-qtquickcontrols2 >= %{qt5_version}
Requires: qt5-qtsvg >= %{qt5_version}
Requires: qt5-qttools >= %{qt5_version}
Requires: qt5-qtwayland >= %{qt5_version}
Requires: vlc
Requires: ffmpeg >= 4.2
Requires: gstreamer1 >= 1.6
Requires: pipewire >= 0.3.0
Requires: v4l-utils
Requires: libv4l
Requires: v4l2loopback

%description
Webcamoid: Virtual Webcam Application

%prep
%setup
mkdir %{_builddir}/%{name}-%{version}/redhat-linux-build

%build
%cmake -B redhat-linux-build -S . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DQT_QMAKE_EXECUTABLE=qmake-qt5
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libavkys.so.%{version}
%{_libdir}/libavkys.so.9
%{_libdir}/libavkys.so
%{_libdir}/avkys/libACapsConvert.so
%{_libdir}/avkys/libAudioDevice.so
%{_libdir}/avkys/libAudioDevice_pulseaudio.so
%{_libdir}/avkys/libAudioDevice_alsa.so
%{_libdir}/avkys/libAudioDevice_jack.so
%{_libdir}/avkys/libAudioGen.so
%{_libdir}/avkys/libDesktopCapture.so
%{_libdir}/avkys/libDesktopCapture_qtscreen.so
%{_libdir}/avkys/libDesktopCapture_pipewire.so
%{_libdir}/avkys/libMultiplex.so
%{_libdir}/avkys/libMultiSink.so
%{_libdir}/avkys/libMultiSink_ffmpeg.so
%{_libdir}/avkys/libMultiSink_gstreamer.so
%{_libdir}/avkys/libMultiSrc.so
%{_libdir}/avkys/libMultiSrc_ffmpeg.so
%{_libdir}/avkys/libMultiSrc_gstreamer.so
%{_libdir}/avkys/libMultiSrc_vlc.so
%{_libdir}/avkys/libVideoCapture.so
%{_libdir}/avkys/libVideoCapture_v4l2sys.so
%{_libdir}/avkys/libVideoCapture_v4lutils.so
%{_libdir}/avkys/libVideoCapture_generic.so
%{_libdir}/avkys/libVideoCapture_ffmpeg.so
%{_libdir}/avkys/libVideoCapture_gstreamer.so
%{_libdir}/avkys/libVirtualCamera.so
%{_libdir}/avkys/libVirtualCamera_akvcam.so
%{_libdir}/avkys/libVirtualCamera_v4l2lb.so
%{_libdir}/avkys/libAdjustHSL.so
%{_libdir}/avkys/libAging.so
%{_libdir}/avkys/libAspectRatio.so
%{_libdir}/avkys/libBlur.so
%{_libdir}/avkys/libCartoon.so
%{_libdir}/avkys/libChangeHSL.so
%{_libdir}/avkys/libCharify.so
%{_libdir}/avkys/libCinema.so
%{_libdir}/avkys/libColorFilter.so
%{_libdir}/avkys/libColorReplace.so
%{_libdir}/avkys/libColorTap.so
%{_libdir}/avkys/libColorTransform.so
%{_libdir}/avkys/libContrast.so
%{_libdir}/avkys/libConvolve.so
%{_libdir}/avkys/libDelayGrab.so
%{_libdir}/avkys/libDenoise.so
%{_libdir}/avkys/libDice.so
%{_libdir}/avkys/libDistort.so
%{_libdir}/avkys/libDizzy.so
%{_libdir}/avkys/libEdge.so
%{_libdir}/avkys/libEmboss.so
%{_libdir}/avkys/libEqualize.so
%{_libdir}/avkys/libFaceDetect.so
%{_libdir}/avkys/libFaceTrack.so
%{_libdir}/avkys/libFalseColor.so
%{_libdir}/avkys/libFire.so
%{_libdir}/avkys/libFlip.so
%{_libdir}/avkys/libFrameOverlap.so
%{_libdir}/avkys/libGamma.so
%{_libdir}/avkys/libGrayScale.so
%{_libdir}/avkys/libHalftone.so
%{_libdir}/avkys/libHypnotic.so
%{_libdir}/avkys/libImplode.so
%{_libdir}/avkys/libInvert.so
%{_libdir}/avkys/libLife.so
%{_libdir}/avkys/libMatrix.so
%{_libdir}/avkys/libMatrixTransform.so
%{_libdir}/avkys/libNervous.so
%{_libdir}/avkys/libNormalize.so
%{_libdir}/avkys/libOilPaint.so
%{_libdir}/avkys/libOtsu.so
%{_libdir}/avkys/libPhotocopy.so
%{_libdir}/avkys/libPixelate.so
%{_libdir}/avkys/libPrimariesColors.so
%{_libdir}/avkys/libQuark.so
%{_libdir}/avkys/libRadioactive.so
%{_libdir}/avkys/libRipple.so
%{_libdir}/avkys/libScale.so
%{_libdir}/avkys/libScanLines.so
%{_libdir}/avkys/libScroll.so
%{_libdir}/avkys/libShagadelic.so
%{_libdir}/avkys/libSwapRB.so
%{_libdir}/avkys/libSwirl.so
%{_libdir}/avkys/libTemperature.so
%{_libdir}/avkys/libVignette.so
%{_libdir}/avkys/libWarhol.so
%{_libdir}/avkys/libWarp.so
%{_libdir}/avkys/libWave.so
%{_bindir}/webcamoid
%{_datadir}/icons/hicolor/128x128/apps/webcamoid.png
%{_datadir}/icons/hicolor/16x16/apps/webcamoid.png
%{_datadir}/icons/hicolor/22x22/apps/webcamoid.png
%{_datadir}/icons/hicolor/256x256/apps/webcamoid.png
%{_datadir}/icons/hicolor/32x32/apps/webcamoid.png
%{_datadir}/icons/hicolor/48x48/apps/webcamoid.png
%{_datadir}/icons/hicolor/64x64/apps/webcamoid.png
%{_datadir}/icons/hicolor/8x8/apps/webcamoid.png
%{_datadir}/icons/hicolor/scalable/apps/webcamoid.svg
%{_datadir}/man/webcamoid.1.gz
%{_datadir}/licenses/webcamoid/COPYING
%{_datadir}/applications/webcamoid.desktop


%changelog
* Sun Apr 03 2022 Antoine Gatineau <antoine.gatineau@infra-monkey.com> - 9.0.0
- Packaging of webcamoid 9.0.0
