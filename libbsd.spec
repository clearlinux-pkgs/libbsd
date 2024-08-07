#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0xB972BF3EA4AE57A3 (guillem@debian.org)
#
%define keepstatic 1
Name     : libbsd
Version  : 0.10.0
Release  : 14
URL      : https://libbsd.freedesktop.org/releases/libbsd-0.10.0.tar.xz
Source0  : https://libbsd.freedesktop.org/releases/libbsd-0.10.0.tar.xz
Source1  : https://libbsd.freedesktop.org/releases/libbsd-0.10.0.tar.xz.asc
Source2  : B972BF3EA4AE57A3.pkey
Summary  : Utility functions from BSD systems
Group    : Development/Tools
License  : BSD-3-Clause BSD-4-Clause
Requires: libbsd-lib = %{version}-%{release}
Requires: libbsd-license = %{version}-%{release}
Requires: libbsd-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libbsd - Utility functions from BSD systems
This library provides useful functions commonly found on BSD systems,
and lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%package dev
Summary: dev components for the libbsd package.
Group: Development
Requires: libbsd-lib = %{version}-%{release}
Provides: libbsd-devel = %{version}-%{release}
Requires: libbsd = %{version}-%{release}

%description dev
dev components for the libbsd package.


%package dev32
Summary: dev32 components for the libbsd package.
Group: Default
Requires: libbsd-lib32 = %{version}-%{release}
Requires: libbsd-dev = %{version}-%{release}

%description dev32
dev32 components for the libbsd package.


%package lib
Summary: lib components for the libbsd package.
Group: Libraries
Requires: libbsd-license = %{version}-%{release}

%description lib
lib components for the libbsd package.


%package lib32
Summary: lib32 components for the libbsd package.
Group: Default
Requires: libbsd-license = %{version}-%{release}

%description lib32
lib32 components for the libbsd package.


%package license
Summary: license components for the libbsd package.
Group: Default

%description license
license components for the libbsd package.


%package man
Summary: man components for the libbsd package.
Group: Default

%description man
man components for the libbsd package.


%package staticdev
Summary: staticdev components for the libbsd package.
Group: Default
Requires: libbsd-dev = %{version}-%{release}

%description staticdev
staticdev components for the libbsd package.


%package staticdev32
Summary: staticdev32 components for the libbsd package.
Group: Default
Requires: libbsd-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the libbsd package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) B972BF3EA4AE57A3' gpg.status
%setup -q -n libbsd-0.10.0
cd %{_builddir}/libbsd-0.10.0
pushd ..
cp -a libbsd-0.10.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719946270
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure     --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719946270
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libbsd
cp %{_builddir}/libbsd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libbsd/45d03b217a50eaa1c429fd65d492e05b9cd2d85b || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/bsd/bitstring.h
/usr/include/bsd/bsd.h
/usr/include/bsd/err.h
/usr/include/bsd/getopt.h
/usr/include/bsd/inttypes.h
/usr/include/bsd/libutil.h
/usr/include/bsd/md5.h
/usr/include/bsd/netinet/ip_icmp.h
/usr/include/bsd/nlist.h
/usr/include/bsd/readpassphrase.h
/usr/include/bsd/stdio.h
/usr/include/bsd/stdlib.h
/usr/include/bsd/string.h
/usr/include/bsd/stringlist.h
/usr/include/bsd/sys/bitstring.h
/usr/include/bsd/sys/cdefs.h
/usr/include/bsd/sys/endian.h
/usr/include/bsd/sys/param.h
/usr/include/bsd/sys/poll.h
/usr/include/bsd/sys/queue.h
/usr/include/bsd/sys/time.h
/usr/include/bsd/sys/tree.h
/usr/include/bsd/timeconv.h
/usr/include/bsd/unistd.h
/usr/include/bsd/vis.h
/usr/include/bsd/wchar.h
/usr/lib64/libbsd.so
/usr/lib64/pkgconfig/libbsd-ctor.pc
/usr/lib64/pkgconfig/libbsd-overlay.pc
/usr/lib64/pkgconfig/libbsd.pc
/usr/share/man/man3/LIST_EMPTY.3bsd
/usr/share/man/man3/LIST_ENTRY.3bsd
/usr/share/man/man3/LIST_FIRST.3bsd
/usr/share/man/man3/LIST_FOREACH.3bsd
/usr/share/man/man3/LIST_FOREACH_FROM.3bsd
/usr/share/man/man3/LIST_FOREACH_FROM_SAFE.3bsd
/usr/share/man/man3/LIST_FOREACH_SAFE.3bsd
/usr/share/man/man3/LIST_HEAD.3bsd
/usr/share/man/man3/LIST_HEAD_INITIALIZER.3bsd
/usr/share/man/man3/LIST_INIT.3bsd
/usr/share/man/man3/LIST_INSERT_AFTER.3bsd
/usr/share/man/man3/LIST_INSERT_BEFORE.3bsd
/usr/share/man/man3/LIST_INSERT_HEAD.3bsd
/usr/share/man/man3/LIST_NEXT.3bsd
/usr/share/man/man3/LIST_PREV.3bsd
/usr/share/man/man3/LIST_REMOVE.3bsd
/usr/share/man/man3/LIST_SWAP.3bsd
/usr/share/man/man3/RB_EMPTY.3bsd
/usr/share/man/man3/RB_ENTRY.3bsd
/usr/share/man/man3/RB_FIND.3bsd
/usr/share/man/man3/RB_FOREACH.3bsd
/usr/share/man/man3/RB_FOREACH_REVERSE.3bsd
/usr/share/man/man3/RB_GENERATE.3bsd
/usr/share/man/man3/RB_GENERATE_STATIC.3bsd
/usr/share/man/man3/RB_HEAD.3bsd
/usr/share/man/man3/RB_INIT.3bsd
/usr/share/man/man3/RB_INITIALIZER.3bsd
/usr/share/man/man3/RB_INSERT.3bsd
/usr/share/man/man3/RB_LEFT.3bsd
/usr/share/man/man3/RB_MAX.3bsd
/usr/share/man/man3/RB_MIN.3bsd
/usr/share/man/man3/RB_NEXT.3bsd
/usr/share/man/man3/RB_NFIND.3bsd
/usr/share/man/man3/RB_PARENT.3bsd
/usr/share/man/man3/RB_PREV.3bsd
/usr/share/man/man3/RB_PROTOTYPE.3bsd
/usr/share/man/man3/RB_PROTOTYPE_STATIC.3bsd
/usr/share/man/man3/RB_REMOVE.3bsd
/usr/share/man/man3/RB_RIGHT.3bsd
/usr/share/man/man3/RB_ROOT.3bsd
/usr/share/man/man3/SLIST_EMPTY.3bsd
/usr/share/man/man3/SLIST_ENTRY.3bsd
/usr/share/man/man3/SLIST_FIRST.3bsd
/usr/share/man/man3/SLIST_FOREACH.3bsd
/usr/share/man/man3/SLIST_FOREACH_FROM.3bsd
/usr/share/man/man3/SLIST_FOREACH_FROM_SAFE.3bsd
/usr/share/man/man3/SLIST_FOREACH_SAFE.3bsd
/usr/share/man/man3/SLIST_HEAD.3bsd
/usr/share/man/man3/SLIST_HEAD_INITIALIZER.3bsd
/usr/share/man/man3/SLIST_INIT.3bsd
/usr/share/man/man3/SLIST_INSERT_AFTER.3bsd
/usr/share/man/man3/SLIST_INSERT_HEAD.3bsd
/usr/share/man/man3/SLIST_NEXT.3bsd
/usr/share/man/man3/SLIST_REMOVE.3bsd
/usr/share/man/man3/SLIST_REMOVE_AFTER.3bsd
/usr/share/man/man3/SLIST_REMOVE_HEAD.3bsd
/usr/share/man/man3/SLIST_SWAP.3bsd
/usr/share/man/man3/SPLAY_EMPTY.3bsd
/usr/share/man/man3/SPLAY_ENTRY.3bsd
/usr/share/man/man3/SPLAY_FIND.3bsd
/usr/share/man/man3/SPLAY_FOREACH.3bsd
/usr/share/man/man3/SPLAY_GENERATE.3bsd
/usr/share/man/man3/SPLAY_HEAD.3bsd
/usr/share/man/man3/SPLAY_INIT.3bsd
/usr/share/man/man3/SPLAY_INITIALIZER.3bsd
/usr/share/man/man3/SPLAY_INSERT.3bsd
/usr/share/man/man3/SPLAY_LEFT.3bsd
/usr/share/man/man3/SPLAY_MAX.3bsd
/usr/share/man/man3/SPLAY_MIN.3bsd
/usr/share/man/man3/SPLAY_NEXT.3bsd
/usr/share/man/man3/SPLAY_PROTOTYPE.3bsd
/usr/share/man/man3/SPLAY_REMOVE.3bsd
/usr/share/man/man3/SPLAY_RIGHT.3bsd
/usr/share/man/man3/SPLAY_ROOT.3bsd
/usr/share/man/man3/STAILQ_CONCAT.3bsd
/usr/share/man/man3/STAILQ_EMPTY.3bsd
/usr/share/man/man3/STAILQ_ENTRY.3bsd
/usr/share/man/man3/STAILQ_FIRST.3bsd
/usr/share/man/man3/STAILQ_FOREACH.3bsd
/usr/share/man/man3/STAILQ_FOREACH_FROM.3bsd
/usr/share/man/man3/STAILQ_FOREACH_FROM_SAFE.3bsd
/usr/share/man/man3/STAILQ_FOREACH_SAFE.3bsd
/usr/share/man/man3/STAILQ_HEAD.3bsd
/usr/share/man/man3/STAILQ_HEAD_INITIALIZER.3bsd
/usr/share/man/man3/STAILQ_INIT.3bsd
/usr/share/man/man3/STAILQ_INSERT_AFTER.3bsd
/usr/share/man/man3/STAILQ_INSERT_HEAD.3bsd
/usr/share/man/man3/STAILQ_INSERT_TAIL.3bsd
/usr/share/man/man3/STAILQ_LAST.3bsd
/usr/share/man/man3/STAILQ_NEXT.3bsd
/usr/share/man/man3/STAILQ_REMOVE.3bsd
/usr/share/man/man3/STAILQ_REMOVE_AFTER.3bsd
/usr/share/man/man3/STAILQ_REMOVE_HEAD.3bsd
/usr/share/man/man3/STAILQ_SWAP.3bsd
/usr/share/man/man3/TAILQ_CONCAT.3bsd
/usr/share/man/man3/TAILQ_EMPTY.3bsd
/usr/share/man/man3/TAILQ_ENTRY.3bsd
/usr/share/man/man3/TAILQ_FIRST.3bsd
/usr/share/man/man3/TAILQ_FOREACH.3bsd
/usr/share/man/man3/TAILQ_FOREACH_FROM.3bsd
/usr/share/man/man3/TAILQ_FOREACH_FROM_SAFE.3bsd
/usr/share/man/man3/TAILQ_FOREACH_REVERSE.3bsd
/usr/share/man/man3/TAILQ_FOREACH_REVERSE_FROM.3bsd
/usr/share/man/man3/TAILQ_FOREACH_REVERSE_FROM_SAFE.3bsd
/usr/share/man/man3/TAILQ_FOREACH_REVERSE_SAFE.3bsd
/usr/share/man/man3/TAILQ_FOREACH_SAFE.3bsd
/usr/share/man/man3/TAILQ_HEAD.3bsd
/usr/share/man/man3/TAILQ_HEAD_INITIALIZER.3bsd
/usr/share/man/man3/TAILQ_INIT.3bsd
/usr/share/man/man3/TAILQ_INSERT_AFTER.3bsd
/usr/share/man/man3/TAILQ_INSERT_BEFORE.3bsd
/usr/share/man/man3/TAILQ_INSERT_HEAD.3bsd
/usr/share/man/man3/TAILQ_INSERT_TAIL.3bsd
/usr/share/man/man3/TAILQ_LAST.3bsd
/usr/share/man/man3/TAILQ_NEXT.3bsd
/usr/share/man/man3/TAILQ_PREV.3bsd
/usr/share/man/man3/TAILQ_REMOVE.3bsd
/usr/share/man/man3/TAILQ_SWAP.3bsd
/usr/share/man/man3/TIMESPEC_TO_TIMEVAL.3bsd
/usr/share/man/man3/TIMEVAL_TO_TIMESPEC.3bsd
/usr/share/man/man3/arc4random.3bsd
/usr/share/man/man3/arc4random_addrandom.3bsd
/usr/share/man/man3/arc4random_buf.3bsd
/usr/share/man/man3/arc4random_stir.3bsd
/usr/share/man/man3/arc4random_uniform.3bsd
/usr/share/man/man3/be16dec.3bsd
/usr/share/man/man3/be16enc.3bsd
/usr/share/man/man3/be32dec.3bsd
/usr/share/man/man3/be32enc.3bsd
/usr/share/man/man3/be64dec.3bsd
/usr/share/man/man3/be64enc.3bsd
/usr/share/man/man3/bit_alloc.3bsd
/usr/share/man/man3/bit_clear.3bsd
/usr/share/man/man3/bit_decl.3bsd
/usr/share/man/man3/bit_ffc.3bsd
/usr/share/man/man3/bit_ffs.3bsd
/usr/share/man/man3/bit_nclear.3bsd
/usr/share/man/man3/bit_nset.3bsd
/usr/share/man/man3/bit_set.3bsd
/usr/share/man/man3/bit_test.3bsd
/usr/share/man/man3/bitstr_size.3bsd
/usr/share/man/man3/bitstring.3bsd
/usr/share/man/man3/byteorder.3bsd
/usr/share/man/man3/closefrom.3bsd
/usr/share/man/man3/dehumanize_number.3bsd
/usr/share/man/man3/errc.3bsd
/usr/share/man/man3/expand_number.3bsd
/usr/share/man/man3/explicit_bzero.3bsd
/usr/share/man/man3/fgetln.3bsd
/usr/share/man/man3/fgetwln.3bsd
/usr/share/man/man3/flopen.3bsd
/usr/share/man/man3/fmtcheck.3bsd
/usr/share/man/man3/fparseln.3bsd
/usr/share/man/man3/fpurge.3bsd
/usr/share/man/man3/funopen.3bsd
/usr/share/man/man3/getbsize.3bsd
/usr/share/man/man3/getmode.3bsd
/usr/share/man/man3/getpeereid.3bsd
/usr/share/man/man3/getprogname.3bsd
/usr/share/man/man3/heapsort.3bsd
/usr/share/man/man3/humanize_number.3bsd
/usr/share/man/man3/le16dec.3bsd
/usr/share/man/man3/le16enc.3bsd
/usr/share/man/man3/le32dec.3bsd
/usr/share/man/man3/le32enc.3bsd
/usr/share/man/man3/le64dec.3bsd
/usr/share/man/man3/le64enc.3bsd
/usr/share/man/man3/md5.3bsd
/usr/share/man/man3/mergesort.3bsd
/usr/share/man/man3/nlist.3bsd
/usr/share/man/man3/pidfile.3bsd
/usr/share/man/man3/pidfile_close.3bsd
/usr/share/man/man3/pidfile_open.3bsd
/usr/share/man/man3/pidfile_remove.3bsd
/usr/share/man/man3/pidfile_write.3bsd
/usr/share/man/man3/queue.3bsd
/usr/share/man/man3/radixsort.3bsd
/usr/share/man/man3/readpassphrase.3bsd
/usr/share/man/man3/reallocarray.3bsd
/usr/share/man/man3/reallocf.3bsd
/usr/share/man/man3/setmode.3bsd
/usr/share/man/man3/setproctitle.3bsd
/usr/share/man/man3/setproctitle_init.3bsd
/usr/share/man/man3/setprogname.3bsd
/usr/share/man/man3/sl_add.3bsd
/usr/share/man/man3/sl_delete.3bsd
/usr/share/man/man3/sl_find.3bsd
/usr/share/man/man3/sl_free.3bsd
/usr/share/man/man3/sl_init.3bsd
/usr/share/man/man3/sradixsort.3bsd
/usr/share/man/man3/stringlist.3bsd
/usr/share/man/man3/strlcat.3bsd
/usr/share/man/man3/strlcpy.3bsd
/usr/share/man/man3/strmode.3bsd
/usr/share/man/man3/strnstr.3bsd
/usr/share/man/man3/strnunvis.3bsd
/usr/share/man/man3/strnvis.3bsd
/usr/share/man/man3/strtoi.3bsd
/usr/share/man/man3/strtonum.3bsd
/usr/share/man/man3/strtou.3bsd
/usr/share/man/man3/strunvis.3bsd
/usr/share/man/man3/strvis.3bsd
/usr/share/man/man3/strvisx.3bsd
/usr/share/man/man3/timeradd.3bsd
/usr/share/man/man3/timerclear.3bsd
/usr/share/man/man3/timercmp.3bsd
/usr/share/man/man3/timerisset.3bsd
/usr/share/man/man3/timersub.3bsd
/usr/share/man/man3/timespecadd.3bsd
/usr/share/man/man3/timespecclear.3bsd
/usr/share/man/man3/timespeccmp.3bsd
/usr/share/man/man3/timespecisset.3bsd
/usr/share/man/man3/timespecsub.3bsd
/usr/share/man/man3/timeval.3bsd
/usr/share/man/man3/tree.3bsd
/usr/share/man/man3/unvis.3bsd
/usr/share/man/man3/vis.3bsd
/usr/share/man/man3/wcslcat.3bsd
/usr/share/man/man3/wcslcpy.3bsd

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libbsd.so
/usr/lib32/pkgconfig/32libbsd-ctor.pc
/usr/lib32/pkgconfig/32libbsd-overlay.pc
/usr/lib32/pkgconfig/32libbsd.pc
/usr/lib32/pkgconfig/libbsd-ctor.pc
/usr/lib32/pkgconfig/libbsd-overlay.pc
/usr/lib32/pkgconfig/libbsd.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbsd.so.0
/usr/lib64/libbsd.so.0.10.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libbsd.so.0
/usr/lib32/libbsd.so.0.10.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libbsd/45d03b217a50eaa1c429fd65d492e05b9cd2d85b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/libbsd.7

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbsd-ctor.a
/usr/lib64/libbsd.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libbsd-ctor.a
/usr/lib32/libbsd.a
