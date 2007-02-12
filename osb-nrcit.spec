Summary:	OSB HTML Rendering engine library
Summary(pl.UTF-8):   Biblioteka OSB silnika renderującego HTML
Name:		osb-nrcit
Version:	0.5.0
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtk-webcore/%{name}-%{version}.tar.gz
# Source0-md5:	b02f4a0dcaac722ad7cdc112db964df4
Patch0:		%{name}-const.patch
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	osb-jscore-devel
BuildRequires:	osb-nrcore-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSB HTML Rendering engine library.

%description -l pl.UTF-8
Biblioteka OSB silnika renderującego HTML.

%package devel
Summary:	Header files for osb-nrcit library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki osb-nrcit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	gtk+2-devel >= 2:2.2.0
Requires:	libxml2-devel >= 1:2.6.0
Requires:	osb-jscore-devel
Requires:	osb-nrcore-devel

%description devel
This is the package containing the header files for osb-nrcit.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki osb-nrcit.

%package static
Summary:	Static osb-nrcit library
Summary(pl.UTF-8):   Statyczna biblioteka osb-nrcit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static osb-nrcit library.

%description static -l pl.UTF-8
Statyczna biblioteka osb-nrcit.

%prep
%setup -q
%patch0 -p1 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libnrcit.so.0.0.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnrcit.so
%{_libdir}/libnrcit.la
%{_includedir}/osb/*.h
%{_pkgconfigdir}/osb-nrcit.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnrcit.a
