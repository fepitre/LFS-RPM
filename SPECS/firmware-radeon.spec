#MD5SUM:	55e7c8cf8bca4fbb738be885266a2dc4;SOURCES/firmware-radeon-1.00.tar.gz
#-----------------------------------------------------------------------------
Summary:	Firmware for radeon graphics cards
Name:		firmware-radeon
Version:	1.00
Release:	1
License:	Any
URL:		Any
Group:		LFS/Base
Vendor:	Elizabeth
Source:	%{name}-%{version}.tar.gz
Requires:	filesystem
%description
Firmware for radeon graphics cards
#-----------------------------------------------------------------------------
%prep
%build
	cd %{_builddir}
	tar xzf %{_sourcedir}/%{name}-%{version}.tar.gz
%install
	install -vdm 755 %{buildroot}/lib/firmware/radeon
	cp -var %{_builddir}/radeon/* %{buildroot}/lib/firmware/radeon
#-----------------------------------------------------------------------------
#	Copy license/copying file
	install -D -m644 %{_builddir}/LICENSE.radeon  %{buildroot}/usr/share/licenses/%{name}/LICENSE
#-----------------------------------------------------------------------------
#	Create file list
#	rm  %{buildroot}%{_infodir}/dir
#	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
#	sed -i '/man\/man/d' filelist.rpm
#	sed -i '/\/usr\/share\/info/d' filelist.rpm
#-----------------------------------------------------------------------------
%files -f filelist.rpm
	%defattr(-,root,root)
#	%%{_infodir}/*
#	%%{_mandir}/man1/*
#-----------------------------------------------------------------------------
%changelog
*	Sun Jul 29 2018 baho-utot <baho-utot@columbus.rr.com> 1.00-1
-	Initial build.	First version
