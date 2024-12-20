%global rpmver 3.11.0
%global srcver 3_11_0

Name: %{_cross_os}libnl
Version: %{rpmver}
Release: 1%{?dist}
Summary: Convenience library for netlink
License: LGPL-2.1-only
URL: https://github.com/thom311/libnl
Source0: https://github.com/thom311/libnl/releases/download/libnl%{srcver}/libnl-%{version}.tar.gz
Source1: https://github.com/thom311/libnl/releases/download/libnl%{srcver}/libnl-%{version}.tar.gz.sig
Source2: gpgkey-49EA7C670E0850E7419514F629C2366E4DFC5728.asc
BuildRequires: %{_cross_os}glibc-devel

%description
%{summary}.

%package devel
Summary: Files for development using the convenience library for netlink
Requires: %{name}

%description devel
%{summary}.

%prep
%{gpgverify} --data=%{S:0} --signature=%{S:1} --keyring=%{S:2}
%autosetup -n libnl-%{version} -p1

%build
autoreconf -fi
%cross_configure \
  --enable-static \
  --disable-cli \

%force_disable_rpath

%make_build

%install
%make_install

%files
%license COPYING
%{_cross_attribution_file}
%{_cross_libdir}/*.so.*
%exclude %{_cross_mandir}
%exclude %{_cross_sysconfdir}

%files devel
%{_cross_libdir}/*.a
%{_cross_libdir}/*.so
%dir %{_cross_includedir}/libnl3
%{_cross_includedir}/libnl3
%{_cross_pkgconfigdir}/*.pc
%exclude %{_cross_libdir}/*.la

%changelog
