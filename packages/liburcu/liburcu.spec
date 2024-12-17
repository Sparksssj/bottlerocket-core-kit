Name: %{_cross_os}liburcu
Version: 0.14.1
Release: 1%{?dist}
Epoch: 1
Summary: Library for userspace RCU
License: LGPL-2.1-only AND GPL-2.0-or-later AND MIT
URL: http://liburcu.org
Source0: http://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2
Source1: http://lttng.org/files/urcu/userspace-rcu-%{version}.tar.bz2.asc
Source2: gpgkey-2A0B4ED915F2D3FA45F5B16217280A9781186ACF.asc

BuildRequires: %{_cross_os}glibc-devel

%description
%{summary}.

%package devel
Summary: Files for development using the library for userspace RCU
Requires: %{name}

%description devel
%{summary}.

%prep
%{gpgverify} --data=%{S:0} --signature=%{S:1} --keyring=%{S:2}
%autosetup -n userspace-rcu-%{version}

%build
%cross_configure --disable-static

%force_disable_rpath

%make_build

%install
%make_install

%files
%license LICENSE gpl-2.0.txt lgpl-relicensing.txt lgpl-2.1.txt
%{_cross_attribution_file}

%{_cross_libdir}/liburcu.so.8*
%{_cross_libdir}/liburcu-common.so.8*

%exclude %{_cross_libdir}/liburcu-bp.so.8*
%exclude %{_cross_libdir}/liburcu-cds.so.8*
%exclude %{_cross_libdir}/liburcu-mb.so.8*
%exclude %{_cross_libdir}/liburcu-memb.so.8*
%exclude %{_cross_libdir}/liburcu-qsbr.so.8*
%exclude %{_cross_libdir}/liburcu-signal.so.8*
%exclude %{_cross_docdir}

%files devel
%{_cross_includedir}/*
%{_cross_libdir}/liburcu-common.so
%{_cross_libdir}/liburcu.so
%{_cross_libdir}/pkgconfig/liburcu.pc

%exclude %{_cross_libdir}/pkgconfig/liburcu-bp.pc
%exclude %{_cross_libdir}/pkgconfig/liburcu-cds.pc
%exclude %{_cross_libdir}/pkgconfig/liburcu-mb.pc
%exclude %{_cross_libdir}/pkgconfig/liburcu-memb.pc
%exclude %{_cross_libdir}/pkgconfig/liburcu-qsbr.pc
%exclude %{_cross_libdir}/pkgconfig/liburcu-signal.pc
%exclude %{_cross_libdir}/liburcu-bp.so
%exclude %{_cross_libdir}/liburcu-cds.so
%exclude %{_cross_libdir}/liburcu-common.so
%exclude %{_cross_libdir}/liburcu-mb.so
%exclude %{_cross_libdir}/liburcu-memb.so
%exclude %{_cross_libdir}/liburcu-qsbr.so
%exclude %{_cross_libdir}/liburcu-signal.so
