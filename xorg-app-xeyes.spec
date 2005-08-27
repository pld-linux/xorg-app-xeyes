# $Rev: 3383 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xeyes application
Summary(pl):	Aplikacja xeyes
Name:		xorg-app-xeyes
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xeyes-%{version}.tar.bz2
# Source0-md5:	894bc468bc8281ba7a58d52d3cf48ed1
Patch0:		xeyes-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xeyes-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xeyes application.

%description -l pl
Aplikacja xeyes.


%prep
%setup -q -n xeyes-%{version}
%patch0 -p1


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


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
