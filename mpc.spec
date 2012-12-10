Summary:	MPC, command-line client for MPD
Name:		mpc
Version:	0.22
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://www.musicpd.org/
Source0:	http://downloads.sourceforge.net/musicpd/%{name}-%{version}.tar.bz2
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
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
cp doc/mpc-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/mpc

rm -rf %{buildroot}%{_docdir}/%{name}/

%files
%doc README AUTHORS COPYING doc/*.sh
%{_sysconfdir}/bash_completion.d/mpc
%{_bindir}/%{name}
%{_mandir}/man1/*


%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.22-1
+ Revision: 778134
- version update 0.22

* Fri Dec 23 2011 Andrey Bondrov <abondrov@mandriva.org> 0.21-1
+ Revision: 744729
- New version 0.21, update BuildRequires

* Sun Aug 08 2010 Rémy Clouard <shikamaru@mandriva.org> 0.19-3mdv2011.0
+ Revision: 567660
- rebuild for new libmpdclient

* Mon Dec 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.19-1mdv2010.1
+ Revision: 474310
- update to 0.19

* Fri Dec 04 2009 Jérôme Brenier <incubusss@mandriva.org> 0.18-1mdv2010.1
+ Revision: 473215
- new version 0.18
- fix license tag
- BuildRequires : libmpdclient-devel

* Fri Aug 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.17-1mdv2010.0
+ Revision: 416370
- update to new version 0.17

* Thu May 28 2009 Frederik Himpe <fhimpe@mandriva.org> 0.16-1mdv2010.0
+ Revision: 380612
- Update to new version 0.16

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 0.15-1mdv2009.1
+ Revision: 336553
- new version 0.15

* Sat Jan 03 2009 Jérôme Soyer <saispo@mandriva.org> 0.14-1mdv2009.1
+ Revision: 323880
- New upstream release

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.12.1-4mdv2009.0
+ Revision: 252957
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.12.1-2mdv2008.1
+ Revision: 136608
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 20 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.12.1-2mdv2008.0
+ Revision: 53811
- install bash-completion
- mpc can command mpd on a different host, so it doesn't requires to have mpd on the same host

* Mon May 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.12.1-1mdv2008.0
+ Revision: 32100
- new version
- requires mpd
- spec file clean
- Import mpc

