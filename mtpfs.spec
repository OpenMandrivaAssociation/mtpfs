%define name	mtpfs
%define version	0.6
%define release	%mkrel 1

Summary:	FUSE filesystem that supports MTP devices
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL+
Group:		File tools
URL:		http://www.adebenham.com/mtpfs/
Source0:	http://www.adebenham.com/mtpfs/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libmtp-devel
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/%{name}
