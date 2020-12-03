Summary:	Command-line client for MPD
Name:		mpc
Version:	0.33
Release:	2
License:	GPLv2+
Group:		Sound
URL:		http://www.musicpd.org/
Source0:	http://www.musicpd.org/download/mpc/0/%{name}-%{version}.tar.xz
# Requires:	mpd
BuildRequires:  meson
BuildRequires:	libmpdclient-devel
BuildRequires:  python3dist(sphinx)

%description
A command line tool to interface MPD. Scriptable !
Features:
* Bash tab completion
* Can pipe output of other commands into mpc

%prep
%setup -q

%build
%meson
%meson_build

%meson_install

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
cp contrib/mpc-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/mpc

rm -rf %{buildroot}%{_docdir}/%{name}/

%files
%doc README.rst AUTHORS COPYING
%{_sysconfdir}/bash_completion.d/mpc
%{_bindir}/%{name}
%{_mandir}/man1/*
