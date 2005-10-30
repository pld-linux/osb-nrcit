#
Summary:	GTK-Webcore Core library
Name:		osb-nrcit
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gtk-webcore/%{name}-%{version}.tar.gz
# Source0-md5:	b02f4a0dcaac722ad7cdc112db964df4
Patch0:	%{name}-const.patch
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	osb-jscore-devel
BuildRequires:	osb-nrcore-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Webcore Core library

%package devel
Summary:	Development libraries and header files for osb-nrcit library
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libraries and header
files for osb-nrcit.

%package static
Summary:	Static osb-nrcit library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static osb-nrcit library.

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
%{_includedir}/osb/*.h
%{_libdir}/libnrcit.la
%{_libdir}/libnrcit.so
%{_libdir}/pkgconfig/osb-nrcit.pc

%files static
%{_libdir}/libnrcit.a
