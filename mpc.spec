Summary:	Command-line client for MPD
Name:	mpc
Version:	0.35
Release:	2
License:	GPLv2+
Group:	Sound
Url:		https://www.musicpd.org/
Source0:	http://www.musicpd.org/download/mpc/0/%{name}-%{version}.tar.xz
Source100:	mpc.rpmlintrc
Patch0:	mpc-0.35-add-status-currenttimems.patch
Patch1:	mpc-0.35-fix-no_status.patch
Patch2:	mpc-0.35-add-status-updateid.patch
Patch3:	mpc-0.35-add-command-tags.patch
BuildRequires:	meson
BuildRequires:	python3dist(sphinx)
BuildRequires:	rsync
BuildRequires:	libmpdclient-devel >= 2.21

%description
A command line tool to interface MPD. Scriptable!
Features:
* Bash tab completion.
* Can pipe output of other commands into mpc.

%files
%doc README.rst AUTHORS COPYING
%{_sysconfdir}/bash_completion.d/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
cp contrib/mpc-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

rm -rf %{buildroot}%{_docdir}/%{name}/
