#TARBALL:	http://download.savannah.gnu.org/releases/libpipeline/libpipeline-1.5.1.tar.gz
#MD5SUM:	4c8fe6cd85422baafd6e060f896c61bc;SOURCES/libpipeline-1.5.1.tar.gz
#-----------------------------------------------------------------------------
Summary:	The Libpipeline package contains a library for manipulating pipelines of subprocesses in a flexible and convenient way.
Name:		libpipeline
Version:	1.5.1
Release:	1
License:	GPLv3
URL:		Any
Group:		LFS/Base
Vendor:	Elizabeth
Source0:	%{name}-%{version}.tar.gz
Requires:	filesystem
%description
The Libpipeline package contains a library for manipulating pipelines of subprocesses in a flexible and convenient way.
#-----------------------------------------------------------------------------
%prep
%setup -q -n %{NAME}-%{VERSION}
%build
	PKG_CONFIG_PATH=/tools/lib/pkgconfig \
	./configure --prefix=%{_prefix}
	make %{?_smp_mflags}
%install
	make DESTDIR=%{buildroot} install
#-----------------------------------------------------------------------------
#	Copy license/copying file
	install -D -m644 COPYING %{buildroot}/usr/share/licenses/%{name}/LICENSE
#-----------------------------------------------------------------------------
#	Create file list
#	rm  %{buildroot}%{_infodir}/dir
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
	sed -i '/man\/man/d' filelist.rpm
	sed -i '/\/usr\/share\/info/d' filelist.rpm
#-----------------------------------------------------------------------------
%files -f filelist.rpm
	%defattr(-,root,root)
#	%%{_infodir}/*
	%{_mandir}/man3/*
#-----------------------------------------------------------------------------
%changelog
*	Sat Apr 06 2019 baho-utot <baho-utot@columbus.rr.com> 1.5.1-1
-	LFS-8.4
*	Tue Jan 09 2018 baho-utot <baho-utot@columbus.rr.com> 1.5.0-1
-	Initial build.	First version
