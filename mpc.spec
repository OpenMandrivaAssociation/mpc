Summary:	Command-line client for MPD
Name:		mpc
Version:	0.27
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://www.musicpd.org/
Source0:	http://www.musicpd.org/download/mpc/0/%{name}-%{version}.tar.xz
# Requires:	mpd
BuildRequires:	libmpdclient-devel >= 2.2

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
%makeinstall_std

install -m644 doc/mpc-completion.bash -D %{buildroot}%{_sysconfdir}/bash_completion.d/mpc

rm -rf %{buildroot}%{_docdir}/%{name}/

%files
%doc README AUTHORS doc/*.sh
%{_sysconfdir}/bash_completion.d/mpc
%{_bindir}/%{name}
%{_mandir}/man1/*
