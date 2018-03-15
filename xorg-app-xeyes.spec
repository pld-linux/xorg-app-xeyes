Summary:	xeyes application - a follow the mouse X demo
Summary(pl.UTF-8):	Aplikacja xeyes - program demonstracyjny dla X obrazujący śledzenie myszy
Name:		xorg-app-xeyes
Version:	1.1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xeyes-%{version}.tar.bz2
# Source0-md5:	6f0543ec84283df5743eeafc173bea4a
Source1:	xeyes.desktop
Source2:	xeyes.png
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.4
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXrender >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xeyes application is a "follow the mouse" X demo, using the X SHAPE
extension.

%description -l pl.UTF-8
Aplikacja xeyes to program demonstracyjny dla X obrazujący śledzenie
myszy, wykorzystujący rozszerzenie X SHAPE.

%prep
%setup -q -n xeyes-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xeyes.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xeyes.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xeyes
%{_desktopdir}/xeyes.desktop
%{_pixmapsdir}/xeyes.png
%{_mandir}/man1/xeyes.1*
