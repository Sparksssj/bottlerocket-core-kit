Name: %{_cross_os}glibc
Version: 2.38
Release: 1%{?dist}
Epoch: 1
Summary: The GNU libc libraries
License: LGPL-2.1-or-later AND (LGPL-2.1-or-later WITH GCC-exception-2.0) AND GPL-2.0-or-later AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND BSD-3-Clause AND ISC
URL: http://www.gnu.org/software/glibc/
Source0: https://ftp.gnu.org/gnu/glibc/glibc-%{version}.tar.xz
Source1: glibc-tmpfiles.conf
Source2: ld.so.conf
Source3: ldconfig-service.conf
Source4: tz-utc.txt

# We include this patch as a source file to have more control over how it's
# applied and reverted during the build.
Source99: HACK-only-build-and-install-localedef.patch

# Upstream patches from 2.38 release branch:
# ```
# git checkout origin/release/2.38/master
# git format-patch --no-numbered glibc-2.38..
# ```
Patch0001: 0001-stdlib-Improve-tst-realpath-compatibility-with-sourc.patch
Patch0002: 0002-x86-Fix-for-cache-computation-on-AMD-legacy-cpus.patch
Patch0003: 0003-nscd-Do-not-rebuild-getaddrinfo-bug-30709.patch
Patch0004: 0004-x86-Fix-incorrect-scope-of-setting-shared_per_thread.patch
Patch0005: 0005-x86_64-Fix-build-with-disable-multiarch-BZ-30721.patch
Patch0006: 0006-i686-Fix-build-with-disable-multiarch.patch
Patch0007: 0007-malloc-Enable-merging-of-remainders-in-memalign-bug-.patch
Patch0008: 0008-malloc-Remove-bin-scanning-from-memalign-bug-30723.patch
Patch0009: 0009-sysdeps-tst-bz21269-fix-test-parameter.patch
Patch0010: 0010-sysdeps-tst-bz21269-handle-ENOSYS-skip-appropriately.patch
Patch0011: 0011-sysdeps-tst-bz21269-fix-Wreturn-type.patch
Patch0012: 0012-io-Fix-record-locking-contants-for-powerpc64-with-__.patch
Patch0013: 0013-libio-Fix-oversized-__io_vtables.patch
Patch0014: 0014-elf-Do-not-run-constructors-for-proxy-objects.patch
Patch0015: 0015-elf-Always-call-destructors-in-reverse-constructor-o.patch
Patch0016: 0016-elf-Remove-unused-l_text_end-field-from-struct-link_.patch
Patch0017: 0017-elf-Move-l_init_called_next-to-old-place-of-l_text_e.patch
Patch0018: 0018-NEWS-Add-the-2.38.1-bug-list.patch
Patch0019: 0019-CVE-2023-4527-Stack-read-overflow-with-large-TCP-res.patch
Patch0020: 0020-getaddrinfo-Fix-use-after-free-in-getcanonname-CVE-2.patch
Patch0021: 0021-iconv-restore-verbosity-with-unrecognized-encoding-n.patch
Patch0022: 0022-string-Fix-tester-build-with-fortify-enable-with-gcc.patch
Patch0023: 0023-manual-jobs.texi-Add-missing-item-EPERM-for-getpgid.patch
Patch0024: 0024-Fix-leak-in-getaddrinfo-introduced-by-the-fix-for-CV.patch
Patch0025: 0025-Document-CVE-2023-4806-and-CVE-2023-5156-in-NEWS.patch
Patch0026: 0026-Propagate-GLIBC_TUNABLES-in-setxid-binaries.patch
Patch0027: 0027-tunables-Terminate-if-end-of-input-is-reached-CVE-20.patch
Patch0028: 0028-Revert-elf-Remove-unused-l_text_end-field-from-struc.patch
Patch0029: 0029-Revert-elf-Always-call-destructors-in-reverse-constr.patch
Patch0030: 0030-Revert-elf-Move-l_init_called_next-to-old-place-of-l.patch
Patch0031: 0031-sysdeps-sem_open-Clear-O_CREAT-when-semaphore-file-i.patch
Patch0032: 0032-elf-Fix-wrong-break-removal-from-8ee878592c.patch
Patch0033: 0033-LoongArch-Delete-excessively-allocated-memory.patch
Patch0034: 0034-elf-Fix-TLS-modid-reuse-generation-assignment-BZ-290.patch
Patch0035: 0035-elf-Add-TLS-modid-reuse-test-for-bug-29039.patch
Patch0036: 0036-x86-64-Fix-the-dtv-field-load-for-x32-BZ-31184.patch
Patch0037: 0037-x86-64-Fix-the-tcb-field-load-for-x32-BZ-31185.patch
Patch0038: 0038-NEWS-Mention-bug-fixes-for-29039-30694-30709-30721.patch
Patch0039: 0039-NEWS-Mention-bug-fixes-for-30745-30843.patch
Patch0040: 0040-getaddrinfo-translate-ENOMEM-to-EAI_MEMORY-bug-31163.patch
Patch0041: 0041-libio-Check-remaining-buffer-size-in-_IO_wdo_write-b.patch
Patch0042: 0042-syslog-Fix-heap-buffer-overflow-in-__vsyslog_interna.patch
Patch0043: 0043-syslog-Fix-heap-buffer-overflow-in-__vsyslog_interna.patch
Patch0044: 0044-syslog-Fix-integer-overflow-in-__vsyslog_internal-CV.patch
Patch0045: 0045-x86_64-Optimize-ffsll-function-code-size.patch
Patch0046: 0046-S390-Fix-building-with-disable-mutli-arch-BZ-31196.patch
Patch0047: 0047-sparc-Fix-broken-memset-for-sparc32-BZ-31068.patch
Patch0048: 0048-sparc64-Remove-unwind-information-from-signal-return.patch
Patch0049: 0049-sparc-Fix-sparc64-memmove-length-comparison-BZ-31266.patch
Patch0050: 0050-sparc-Remove-unwind-information-from-signal-return-s.patch
Patch0051: 0051-arm-Remove-wrong-ldr-from-_dl_start_user-BZ-31339.patch
Patch0052: 0052-malloc-Use-__get_nprocs-on-arena_get2-BZ-30945.patch
Patch0053: 0053-S390-Do-not-clobber-r7-in-clone-BZ-31402.patch
Patch0054: 0054-linux-Use-rseq-area-unconditionally-in-sched_getcpu-.patch
Patch0055: 0055-LoongArch-Correct-__ieee754-_-_scalb-__ieee754-_-_sc.patch
Patch0056: 0056-Add-HWCAP2_MOPS-from-Linux-6.5-to-AArch64-bits-hwcap.patch
Patch0057: 0057-AArch64-Add-support-for-MOPS-memcpy-memmove-memset.patch
Patch0058: 0058-AArch64-Cleanup-ifuncs.patch
Patch0059: 0059-AArch64-Cleanup-emag-memset.patch
Patch0060: 0060-AArch64-Add-memset_zva64.patch
Patch0061: 0061-AArch64-Remove-Falkor-memcpy.patch
Patch0062: 0062-aarch64-correct-CFI-in-rawmemchr-bug-31113.patch
Patch0063: 0063-aarch64-fix-check-for-SVE-support-in-assembler.patch
Patch0064: 0064-AArch64-Check-kernel-version-for-SVE-ifuncs.patch
Patch0065: 0065-powerpc-Fix-ld.so-address-determination-for-PCREL-mo.patch
Patch0066: 0066-iconv-ISO-2022-CN-EXT-fix-out-of-bound-writes-when-w.patch
Patch0067: 0067-sparc-Remove-64-bit-check-on-sparc32-wordsize-BZ-275.patch
Patch0068: 0068-login-Check-default-sizes-of-structs-utmp-utmpx-last.patch
Patch0069: 0069-login-structs-utmp-utmpx-lastlog-_TIME_BITS-independ.patch
Patch0070: 0070-nptl-Fix-tst-cancel30-on-kernels-without-ppoll_time6.patch
Patch0071: 0071-i386-ulp-update-for-SSE2-disable-multi-arch-configur.patch
Patch0072: 0072-CVE-2024-33599-nscd-Stack-based-buffer-overflow-in-n.patch
Patch0073: 0073-CVE-2024-33600-nscd-Do-not-send-missing-not-found-re.patch
Patch0074: 0074-CVE-2024-33600-nscd-Avoid-null-pointer-crashes-after.patch
Patch0075: 0075-CVE-2024-33601-CVE-2024-33602-nscd-netgroup-Use-two-.patch
Patch0076: 0076-elf-Also-compile-dl-misc.os-with-rtld-early-cflags.patch
Patch0077: 0077-nscd-Use-time_t-for-return-type-of-addgetnetgrentX.patch
Patch0078: 0078-resolv-Fix-some-unaligned-accesses-in-resolver-BZ-30.patch
Patch0079: 0079-Force-DT_RPATH-for-enable-hardcoded-path-in-tests.patch
Patch0080: 0080-i386-Disable-Intel-Xeon-Phi-tests-for-GCC-15-and-abo.patch
Patch0081: 0081-misc-Add-support-for-Linux-uio.h-RWF_NOAPPEND-flag.patch
Patch0082: 0082-s390x-Fix-segfault-in-wcsncmp-BZ-31934.patch
Patch0083: 0083-nptl-fix-potential-merge-of-__rseq_-relro-symbols.patch
Patch0084: 0084-elf-Make-dl-rseq-symbols-Linux-only.patch
Patch0085: 0085-Linux-Make-__rseq_size-useful-for-feature-detection-.patch
Patch0086: 0086-resolv-Allow-short-error-responses-to-match-any-quer.patch
Patch0087: 0087-resolv-Do-not-wait-for-non-existing-second-DNS-respo.patch
Patch0088: 0088-resolv-Track-single-request-fallback-via-_res._flags.patch
Patch0089: 0089-linux-Update-the-mremap-C-implementation-BZ-31968.patch
Patch0090: 0090-mremap-Update-manual-entry.patch
Patch0091: 0091-Add-mremap-tests.patch
Patch0092: 0092-Update-syscall-lists-for-Linux-6.5.patch
Patch0093: 0093-resolv-Fix-tst-resolv-short-response-for-older-GCC-b.patch
Patch0094: 0094-Fix-name-space-violation-in-fortify-wrappers-bug-320.patch
Patch0095: 0095-x86-Fix-bug-in-strchrnul-evex512-BZ-32078.patch
Patch0096: 0096-support-Add-FAIL-test-failure-helper.patch
Patch0097: 0097-stdio-common-Add-test-for-vfscanf-with-matches-longe.patch
Patch0098: 0098-Make-tst-ungetc-use-libsupport.patch
Patch0099: 0099-ungetc-Fix-uninitialized-read-when-putting-into-unus.patch
Patch0100: 0100-ungetc-Fix-backup-buffer-leak-on-program-exit-BZ-278.patch
Patch0101: 0101-posix-Use-support-check.h-facilities-in-tst-truncate.patch
Patch0102: 0102-nptl-Use-support-check.h-facilities-in-tst-setuid3.patch
Patch0103: 0103-libio-Attempt-wide-backup-free-only-for-non-legacy-c.patch
Patch0104: 0104-Add-crt1-2.0.o-for-glibc-2.0-compatibility-tests.patch
Patch0105: 0105-elf-Change-ldconfig-auxcache-magic-number-bug-32231.patch
Patch0106: 0106-nptl-initialize-rseq-area-prior-to-registration.patch
Patch0107: 0107-nptl-initialize-cpu_id_start-prior-to-rseq-registrat.patch

# Fedora patches
Patch1001: glibc-cs-path.patch

# Local patches
Patch9001: 9001-move-ldconfig-cache-to-ephemeral-storage.patch

%description
%{summary}.

%package devel
Summary: Files for development using the GNU libc libraries.
Requires: %{name}

%description devel
%{summary}.

%prep
%autosetup -Sgit -n glibc-%{version} -p1

%global glibc_configure %{shrink: \
BUILDFLAGS="-O2 -g -Wp,-D_GLIBCXX_ASSERTIONS -fstack-clash-protection" \
CFLAGS="${BUILDFLAGS}" CPPFLAGS="" CXXFLAGS="${BUILDFLAGS}" \
../configure \
  --prefix="%{_cross_prefix}" \
  --sysconfdir="%{_cross_sysconfdir}" \
  --localstatedir="%{_cross_localstatedir}" \
  --enable-bind-now \
  --enable-fortify-source \
  --enable-multi-arch \
  --enable-shared \
  --enable-stack-protector=strong \
  --disable-build-nscd \
  --disable-crypt \
  --disable-nscd \
  --disable-profile \
  --disable-systemtap \
  --disable-timezone-tools \
  --without-gd \
  --without-selinux
  %{nil}}

%build

# First build the host tools we need, namely `localedef`. Apply a patch from
# Buildroot that allows us to build just this program and not everything.
patch -p1 < %{S:99}

mkdir build
pushd build
%glibc_configure
make %{?_smp_mflags} -O -r locale/others
mv locale/localedef %{_builddir}/localedef
popd

# Remove the previous build, revert the patch, and verify that the tree is
# clean, since we don't want to contaminate our target build.
rm -rf build
patch -p1 -R < %{S:99}
git diff --quiet

# Now build for the target. This is what will end up in the package, except
# for the C.UTF-8 locale, which we need `localedef` to generate.
mkdir build
pushd build
%glibc_configure \
  --target="%{_cross_target}" \
  --host="%{_cross_target}" \
  --build="%{_build}" \
  --with-headers="%{_cross_includedir}" \
  --enable-kernel="5.10.0"
make %{?_smp_mflags} -O -r
popd

%install
pushd build
make -j1 install_root=%{buildroot} install
# By default, LOCALEDEF refers to the target binary, and is invoked by the
# dynamic linker that was just built for the target. Neither will run on a
# build host with a different architecture. The locale format is compatible
# across architectures but not across glibc versions, so we can't rely on
# the binary in the SDK and must use the one we built earlier.
make -j1 install_root=%{buildroot} install-files-C.UTF-8/UTF-8 -C ../localedata objdir="$(pwd)" \
  LOCALEDEF="I18NPATH=. GCONV_PATH=$(pwd)/../iconvdata LC_ALL=C %{_builddir}/localedef"
popd

install -d %{buildroot}%{_cross_tmpfilesdir}
install -d %{buildroot}%{_cross_factorydir}%{_cross_sysconfdir}
install -d %{buildroot}%{_cross_unitdir}/ldconfig.service.d

install -p -m 0644 %{S:1} %{buildroot}%{_cross_tmpfilesdir}/glibc.conf
install -p -m 0644 %{S:2} %{buildroot}%{_cross_factorydir}%{_cross_sysconfdir}/ld.so.conf
install -p -m 0644 %{S:3} %{buildroot}%{_cross_unitdir}/ldconfig.service.d/ldconfig.conf

truncate -s 0 %{buildroot}%{_cross_libdir}/gconv/gconv-modules
chmod 644 %{buildroot}%{_cross_libdir}/gconv/gconv-modules
truncate -s 0 %{buildroot}%{_cross_libdir}/gconv/gconv-modules.cache
chmod 644 %{buildroot}%{_cross_libdir}/gconv/gconv-modules.cache

truncate -s 0 %{buildroot}%{_cross_datadir}/locale/locale.alias
chmod 644 %{buildroot}%{_cross_datadir}/locale/locale.alias

install -d %{buildroot}%{_cross_datadir}/zoneinfo
base64 --decode %{S:4} > %{buildroot}%{_cross_datadir}/zoneinfo/UTC

%files
%license COPYING COPYING.LIB LICENSES
%{_cross_attribution_file}
%{_cross_tmpfilesdir}/glibc.conf
%exclude %{_cross_sysconfdir}/rpc

%{_cross_bindir}/getconf
%{_cross_bindir}/getent
%exclude %{_cross_bindir}/gencat
%exclude %{_cross_bindir}/iconv
%exclude %{_cross_bindir}/ld.so
%exclude %{_cross_bindir}/ldd
%exclude %{_cross_bindir}/locale
%exclude %{_cross_bindir}/localedef
%exclude %{_cross_bindir}/makedb
%exclude %{_cross_bindir}/mtrace
%exclude %{_cross_bindir}/pldd
%exclude %{_cross_bindir}/pcprofiledump
%exclude %{_cross_bindir}/sotruss
%exclude %{_cross_bindir}/sprof
%exclude %{_cross_bindir}/xtrace

%{_cross_sbindir}/ldconfig
%exclude %{_cross_sbindir}/iconvconfig
%exclude %{_cross_sbindir}/sln

%dir %{_cross_libexecdir}/getconf
%{_cross_libexecdir}/getconf/*

%{_cross_libdir}/ld-linux-*.so.*
%{_cross_libdir}/libBrokenLocale.so.*
%{_cross_libdir}/libanl.so.*
%{_cross_libdir}/libc.so.*
%{_cross_libdir}/libdl.so.*
%{_cross_libdir}/libm.so.*
%{_cross_libdir}/libnss_dns.so.*
%{_cross_libdir}/libnss_files.so.*
%{_cross_libdir}/libpthread.so.*
%{_cross_libdir}/libresolv.so.*
%{_cross_libdir}/librt.so.*
%{_cross_libdir}/libthread_db.so.*
%{_cross_libdir}/libutil.so.*
%{_cross_libdir}/libmvec.so.*
%exclude %{_cross_libdir}/audit/sotruss-lib.so
%exclude %{_cross_libdir}/libc_malloc_debug.so.*
%exclude %{_cross_libdir}/libmemusage.so
%exclude %{_cross_libdir}/libpcprofile.so
%exclude %{_cross_libdir}/libnsl.so.*
%exclude %{_cross_libdir}/libnss_compat.so.*
%exclude %{_cross_libdir}/libnss_db.so.*
%exclude %{_cross_libdir}/libnss_hesiod.so.*

%dir %{_cross_libdir}/gconv
%dir %{_cross_libdir}/gconv/gconv-modules.d
%{_cross_libdir}/gconv/gconv-modules
%{_cross_libdir}/gconv/gconv-modules.cache
%exclude %{_cross_libdir}/gconv/*.so
%exclude %{_cross_libdir}/gconv/gconv-modules.d/*.conf

%dir %{_cross_libdir}/locale
%dir %{_cross_libdir}/locale/C.utf8
%{_cross_libdir}/locale/C.utf8/LC_*

%dir %{_cross_datadir}/i18n
%dir %{_cross_datadir}/i18n/charmaps
%dir %{_cross_datadir}/i18n/locales
%dir %{_cross_datadir}/locale
%{_cross_datadir}/locale/locale.alias
%dir %{_cross_datadir}/zoneinfo
%{_cross_datadir}/zoneinfo/UTC
%exclude %{_cross_datadir}/i18n/charmaps/*
%exclude %{_cross_datadir}/i18n/locales/*
%exclude %{_cross_datadir}/locale/*
%exclude %{_cross_localstatedir}/db/Makefile

%dir %{_cross_factorydir}
%{_cross_factorydir}%{_cross_sysconfdir}/ld.so.conf

%dir %{_cross_unitdir}/ldconfig.service.d
%{_cross_libdir}/systemd/system/ldconfig.service.d/ldconfig.conf

%files devel
%{_cross_libdir}/*.a
%{_cross_libdir}/*.o
%{_cross_libdir}/libBrokenLocale.so
%{_cross_libdir}/libanl.so
%{_cross_libdir}/libc.so
%{_cross_libdir}/libm.so
%{_cross_libdir}/libresolv.so
%{_cross_libdir}/libthread_db.so
%{_cross_libdir}/libmvec.so
%exclude %{_cross_libdir}/libc_malloc_debug.so
%exclude %{_cross_libdir}/libnss_compat.so
%exclude %{_cross_libdir}/libnss_db.so
%exclude %{_cross_libdir}/libnss_hesiod.so

%dir %{_cross_includedir}/arpa
%dir %{_cross_includedir}/bits
%dir %{_cross_includedir}/gnu
%dir %{_cross_includedir}/net
%dir %{_cross_includedir}/netinet
%dir %{_cross_includedir}/netipx
%dir %{_cross_includedir}/netiucv
%dir %{_cross_includedir}/netpacket
%dir %{_cross_includedir}/netrose
%dir %{_cross_includedir}/nfs
%dir %{_cross_includedir}/protocols
%dir %{_cross_includedir}/rpc
%dir %{_cross_includedir}/scsi
%dir %{_cross_includedir}/sys
%dir %{_cross_includedir}/netash
%dir %{_cross_includedir}/netatalk
%dir %{_cross_includedir}/netax25
%dir %{_cross_includedir}/neteconet
%dir %{_cross_includedir}/netrom
%{_cross_includedir}/*.h
%{_cross_includedir}/*/*

%changelog
