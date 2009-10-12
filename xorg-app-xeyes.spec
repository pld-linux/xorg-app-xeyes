Summary:	xeyes application
Summary(pl.UTF-8):	Aplikacja xeyes
Name:		xorg-app-xeyes
Version:	1.0.991
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xeyes-%{version}.tar.bz2
# Source0-md5:	ba1b886bd6104018fe78ab431d83ce4d
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

%description -l pl.UTF-8
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
%attr(755,root,root) %{_bindir}/xeyes
%{_desktopdir}/xeyes.desktop
%{_pixmapsdir}/xeyes.png
%{_mandir}/man1/xeyes.1x*
