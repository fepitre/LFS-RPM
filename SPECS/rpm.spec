#TARBALL:	ftp.rpm.org/releases/rpm-4.14.x/rpm-4.14.2.1.tar.bz2
#TARBALL:	http://download.oracle.com/berkeley-db/db-6.0.20.tar.gz
#MD5SUM:	fdb8b8857f103b087b6aed5b78dd9b4f;SOURCES/rpm-4.14.2.1.tar.bz2
#MD5SUM:	f73afcb308aefde7e6ece4caa87b22a9;SOURCES/db-6.0.20.tar.gz
#-----------------------------------------------------------------------------
Summary:	Package manager
Name:		rpm
Version:	4.14.2.1
Release:	1
License:	GPLv2
URL:		http://rpm.org
Group:		LFS/BASE
Vendor:	Elizabeth

Source0:	http://ftp.rpm.org/releases/rpm-4.14.x/%{name}-%{version}.tar.bz2
Source1:	http://download.oracle.com/berkeley-db/db-6.0.20.tar.gz
Source2:	macros
Requires:	filesystem
%description
Package manager
#-----------------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}
%setup -q -T -D -a 1 -n %{name}-%{version}
sed -i 's/--srcdir=$db_dist/--srcdir=$db_dist --with-pic/' db3/configure
%build
	ln -vs db-6.0.20 db
	./configure \
		--prefix=%{_prefix} \
		--program-prefix= \
		--sysconfdir=/etc \
		--with-crypto=openssl \
		--with-cap \
		--with-acl \
		--without-external-db \
		--without-archive \
		--without-lua \
		--disable-dependency-tracking \
		--disable-silent-rules \
		--disable-rpath \
		--disable-plugins \
		--disable-inhibit-plugin
	make %{?_smp_mflags}
%install
	make DESTDIR=%{buildroot} install
	install -vdm 755	%{buildroot}/etc/rpm
	install -vm  644	%{_sourcedir}/macros %{buildroot}/etc/rpm
#-----------------------------------------------------------------------------
#	Copy license/copying file 
	install -D -m644 COPYING %{buildroot}%{_datarootdir}/licenses/%{name}-%{version}/COPYING
	install -D -m644 INSTALL %{buildroot}%{_datarootdir}/licenses/%{name}-%{version}/INSTALL
#-----------------------------------------------------------------------------
#	Create file list
#	rm  %{buildroot}%{_infodir}/dir
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
	sed -i '/man\/man/d' filelist.rpm
	sed -i '/\/usr\/share\/info/d' filelist.rpm
	sed -i '/man\/fr/d' filelist.rpm
	sed -i '/man\/pl/d' filelist.rpm
	sed -i '/man\/sk/d' filelist.rpm
	sed -i '/man\/ko/d' filelist.rpm
	sed -i '/man\/ja/d' filelist.rpm
	sed -i '/man\/ru/d' filelist.rpm	
#-----------------------------------------------------------------------------
%files -f filelist.rpm
	%defattr(-,root,root)
	%{_mandir}/man1/*
	%{_mandir}/man8/*
	%{_mandir}/fr/man8/*
	%{_mandir}/ja/man8/*
	%{_mandir}/ko/man8/*
	%{_mandir}/pl/man1/*
	%{_mandir}/pl/man8/*
	%{_mandir}/ru/man8/*
	%{_mandir}/sk/man8/*
#-----------------------------------------------------------------------------
%changelog
*	Wed Sep 26 2018 baho-utot <baho-utot@columbus.rr.com> 4.14.1-2
*	Sat Jul 28 2018 baho-utot <baho-utot@columbus.rr.com> 4.14.1-1
*	Sat Mar 10 2018 baho-utot <baho-utot@columbus.rr.com> 4.14.0-4
-	Added acl and cap Removed plugins and disabled python
*	Tue Feb 20 2018 baho-utot <baho-utot@columbus.rr.com> 4.14.0-3
-	Added python bindings for rpmlint
*	Mon Jan 01 2018 baho-utot <baho-utot@columbus.rr.com> 4.14.0-1
-	LFS-8.1
/
