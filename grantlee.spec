Summary:	A string template engine
Name:		grantlee
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://downloads.grantlee.org/%{name}-%{version}.tar.gz
# Source0-md5:	195763a3238f51f8885881fc8012cd83
URL:		http://www.gitorious.org/grantlee/pages/Home
BuildRequires:	QtGui-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtTest-devel
BuildRequires:	cmake
BuildRequires:	qt-build
BuildRequires:	qt-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grantlee is a string template engine based on the Django template
system and written in Qt.

%package devel
Summary:	Header files for grantlee
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for grantlee.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgrantlee_core.so.?
%attr(755,root,root) %ghost %{_libdir}/libgrantlee_gui.so.?
%attr(755,root,root) %{_libdir}/libgrantlee_core.so.*.*.*
%attr(755,root,root) %{_libdir}/libgrantlee_gui.so.*.*.*

%dir %{_libdir}/grantlee
%dir %{_libdir}/grantlee/0.3
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_defaultfilters.so
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_defaulttags.so
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_i18ntags.so
%attr(755,root,root) %{_libdir}/grantlee/0.3/grantlee_loadertags.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgrantlee_core.so
%attr(755,root,root) %{_libdir}/libgrantlee_gui.so
%{_includedir}/%{name}
%{_includedir}/*.h
%{_libdir}/cmake/grantlee

