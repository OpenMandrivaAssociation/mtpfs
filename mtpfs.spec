%define name	mtpfs
%define version	1.1
%define release	1

Summary:	FUSE filesystem that supports MTP devices
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		File tools
URL:		http://www.adebenham.com/mtpfs
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
