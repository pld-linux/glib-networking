Summary:	Networking support for GLib
Summary(pl.UTF-8):	Obsługa sieci dla GLiba
Name:		glib-networking
Version:	2.28.4
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib-networking/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	f5be1b48cac2c4c645368bf2cff6bea9
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnutls-devel >= 2.1.7
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libproxy-devel >= 0.3.1
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig
BuildRequires:	gsettings-desktop-schemas-devel
Requires(post,postun):	glib2 >= 1:2.28.0
Requires:	ca-certificates
Requires:	libproxy >= 0.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains a libproxy-based GProxyResolver
implementation and a gnutls-based GTlsConnection implementation.

%description -l pl.UTF-8
Ten pakiet zawiera moduły rozszerzające obsługę sieci w GIO, w
szczególności: implementację GProxyResolver opartą na libproxy oraz
implementację GTlsConnection opartą na gnutls.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-ca-certificates=/etc/certs/ca-certificates.crt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules || :

%postun
umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules || :

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/glib-pacrunner
%attr(755,root,root) %{_libdir}/gio/modules/libgiognutls.so
%attr(755,root,root) %{_libdir}/gio/modules/libgiolibproxy.so
%attr(755,root,root) %{_libdir}/gio/modules/libgiognomeproxy.so
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
