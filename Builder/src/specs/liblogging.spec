%define _unpackaged_files_terminate_build 0

%global realversion 1.0.5
%global rpmversion <rpm.version>
%global packager <ericsson.rstate>
%global realname liblogging

Name:	  EXTRlitpliblogging_CXP9032141
Version:  %{rpmversion}
Release:  1%{?dist}
Summary:  LibLogging stdlog library
License:  2-clause BSD
Group:	  System Environment/Libraries
URL:	  http://www.ericsson.com
Source0:  http://download.rsyslog.com/%{realname}/%{realname}-%{realversion}.tar.gz 
Packager: %{packager}
Provides: %{realname} = %{realversion}

BuildRoot:      %{_tmppath}/%{realname}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
LibLogging stdlog library
Libstdlog component is used for standard logging (syslog replacement)
purposes via multiple channels (driver support is planned)

%package devel
Summary:  Development files for LibLogging stdlog library
Group:	  Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libee-devel%{?_isa} 
Requires: libestr-devel%{?_isa}
Requires: pkgconfig

%description devel
The liblogging-devel package includes header files, libraries necessary for
developing programs which use liblogging library.

%prep
%setup -q -n %{realname}-%{realversion}

%build
%configure --enable-stdlog  --disable-journal --enable-rfc3195
V=1 make

%install
make install INSTALL="install -p" DESTDIR="$RPM_BUILD_ROOT"
rm -f %{buildroot}%{_libdir}/*.{a,la}
#../dependency/chrpath-0.13/build/bin/chrpath -d %{buildroot}%{_libdir}/%{realname}-stdlog.so.0.0.0
chrpath -d %{buildroot}%{_libdir}/%{realname}-stdlog.so.0.0.0

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun
if [ "$1" = "0" ] ; then
    /sbin/ldconfig
fi

%files
%defattr(0755, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{realname}-stdlog.so.*
%{_bindir}/stdlogctl
%{_mandir}/*/*

%files devel
%{_libdir}/%{realname}-stdlog.so
%{_includedir}/%{realname}/*.h
%{_libdir}/pkgconfig/%{realname}-stdlog.pc


%changelog

* Tue Dec 09 2014 Florian Riedl
- New RPMs for 1.0.5

* Wed Mar 02 2014 Andre Lorbach
- New RPMs for 1.0.4

* Tue Feb 04 2014 Andre Lorbach
- New RPMs for 1.0.1

* Tue Jan 21 2014 Andre Lorbach
- Initial Version
