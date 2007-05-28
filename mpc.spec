%define name 	mpc
%define version 0.11.2
%define release	1mdk

Summary:		MPC, command-line client for MPD
Name:			%name
Version:		%version
Release:		%release
License:		GPL
Group:			Sound
URL:			http://www.musicpd.org/
Source:			%{name}-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot

%description
A command line tool to interface MPD. Scriptable !
Features:
* Bash tab completion
* Can pipe output of other commands into mpc

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog doc/*.sh doc/mpc-bashrc
%{_bindir}/%name
%{_mandir}/man1/*
