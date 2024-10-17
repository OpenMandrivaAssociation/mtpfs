%define name	mtpfs
%define version	1.1
%define release	2

Summary:	FUSE filesystem that supports MTP devices
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		File tools
URL:		https://www.adebenham.com/mtpfs
Source0:	http://www.adebenham.com/debian/%{name}-%{version}.tar.gz
BuildRequires:	libmtp-devel >= 0.3.0
BuildRequires:	fuse-devel
BuildRequires:	libmad-devel
BuildRequires:	id3tag-devel
BuildRequires:	glib2-devel
Requires:	fuse

%description
MTPfs is a FUSE filesystem that supports reading and writing from any
MTP device supported by libmtp.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%{_bindir}/%{name}


%changelog
* Wed Feb 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1
+ Revision: 781466
- version update 1.1

* Wed Feb 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0-1
+ Revision: 774396
- version update 1.0

* Wed Oct 26 2011 Götz Waschk <waschk@mandriva.org> 0.9-3
+ Revision: 707257
- rebuild for new libmtp

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-2mdv2011.0
+ Revision: 612949
- the mass rebuild of 2010.1 packages

* Mon Jan 11 2010 Jérôme Brenier <incubusss@mandriva.org> 0.9-1mdv2010.1
+ Revision: 489971
- new version 0.9
- drop Patch0 (merged upstream)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jul 18 2008 Funda Wang <fwang@mandriva.org> 0.7-1mdv2009.0
+ Revision: 238256
- New version 0.7
- add patch to build against libmtp 0.3.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 27 2007 Funda Wang <fwang@mandriva.org> 0.6-3mdv2008.1
+ Revision: 102623
- Rebuild for new libmtp

* Sat Sep 08 2007 Adam Williamson <awilliamson@mandriva.org> 0.6-2mdv2008.0
+ Revision: 82302
- Import mtpfs

