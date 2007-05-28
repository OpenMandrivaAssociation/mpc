Summary:	MPC, command-line client for MPD
Name:		mpc
Version:	0.12.1
Release:	%mkrel 1
License:	GPL
Group:		Sound
URL:		http://www.musicpd.org/
Source:		http://www.musicpd.org/uploads/files/%{name}-%{version}.tar.bz2
Requires:	mpd
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A command line tool to interface MPD. Scriptable !
Features:
* Bash tab completion
* Can pipe output of other commands into mpc

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_docdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog doc/*.sh doc/mpc-bashrc
%{_bindir}/%{name}
%{_mandir}/man1/*
