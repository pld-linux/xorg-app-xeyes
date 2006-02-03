Summary:	xeyes application
Summary(pl):	Aplikacja xeyes
Name:		xorg-app-xeyes
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/app/xeyes-%{version}.tar.bz2
# Source0-md5:	033f14f7c4e30d1f4edbb22d5ef86883
Source1:	xeyes.desktop
Source2:	xeyes.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xeyes application.

%description -l pl
Aplikacja xeyes.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/xeyes.desktop
%{_pixmapsdir}/xeyes.png
%{_mandir}/man1/*.1x*
