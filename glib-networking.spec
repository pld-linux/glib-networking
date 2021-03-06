Summary:	Networking support for GLib
Summary(pl.UTF-8):	Obsługa sieci dla GLiba
Name:		glib-networking
Version:	2.68.1
Release:	1
License:	LGPL v2.1+ with OpenSSL exception
Group:		Libraries
Source0:	https://download.gnome.org/sources/glib-networking/2.68/%{name}-%{version}.tar.xz
# Source0-md5:	182ae3263763160a2cf0bd4f854448c3
URL:		https://www.gnome.org/
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	glib2-devel >= 1:2.67.0
BuildRequires:	gnutls-devel >= 3.7
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	libproxy-devel >= 0.3.1
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.67.0
Requires:	ca-certificates
Requires:	glib2 >= 1:2.67.0
Requires:	gnutls-libs >= 3.7
Requires:	libproxy >= 0.3.1
Suggests:	gsettings-desktop-schemas
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
%meson build \
	-Dca_certificates_path=/etc/certs/ca-certificates.crt \
	-Dinstalled_tests=false

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc LICENSE_EXCEPTION NEWS README
%attr(755,root,root) %{_libexecdir}/glib-pacrunner
%attr(755,root,root) %{_libdir}/gio/modules/libgiognutls.so
%attr(755,root,root) %{_libdir}/gio/modules/libgiolibproxy.so
%attr(755,root,root) %{_libdir}/gio/modules/libgiognomeproxy.so
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
%{systemduserunitdir}/glib-pacrunner.service
