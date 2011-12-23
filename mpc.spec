Summary:	MPC, command-line client for MPD
Name:		mpc
Version:	0.21
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
URL:		http://www.musicpd.org/
Source:		http://downloads.sourceforge.net/musicpd/%{name}-%{version}.tar.bz2
# Requires:	mpd
BuildRequires:	libmpdclient-devel >= 2.2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
cp doc/mpc-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/mpc

rm -rf %{buildroot}%{_docdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING doc/*.sh
%{_sysconfdir}/bash_completion.d/mpc
%{_bindir}/%{name}
%{_mandir}/man1/*
