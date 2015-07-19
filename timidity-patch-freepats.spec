%define version 20060219
%define release 23

#
# NOTE:
#
# 1. When big change is involved (e.g. timidity.cfg change location),
# so that new timidity binray and old patch RPM won't work together,
# increment this number by 1 for all timidity related RPMs
#
# 2. Current config is hand merged from freepats.cfg and crude.cfg,
# so if new version is available, please merge both config, and make
# sure all patch files listed in config file do exist.
#
%define patch_pkg_version 2

Name:		timidity-patch-freepats
Version:	%{version}
Release:	%{release}
Summary:	Patch set for MIDI audio synthesis
Group:		Sound
License:	GPL
URL:		http://freepats.opensrc.org/
Source0:	http://freepats.opensrc.org/freepats-%{version}.tar.bz2
Source1:	timidity-freepats.cfg
Source2:	freepats.cfg
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Provides:	timidity-instruments = %{patch_pkg_version}
Obsoletes:	timidity-instruments <= 1.0-19mdk

%description
Freepats is a project to create a free and open set of GUS
compatible patches that can be used with softsynths such as
Timidity and WildMidi. They are verified to contain no non-free
restriction. Freepats is distributed under GPL v2 or later, with
the follow exception clause about the relation of MIDI composition
and patches:

=========================================================
As a special exception, if you create a composition which uses
these patches, and mix these patches or unaltered portions of
these patches into the composition, these patches do not by
themselves cause the resulting composition to be covered by the
GNU General Public License. This exception does not however
invalidate any other reasons why the document might be covered
by the GNU General Public License. If you modify these patches,
you may extend this exception to your version of the patches,
but you are not obligated to do so. If you do not wish to do so,
delete this exception statement from your version.
==========================================================

This patch set is of limited quality, because some instruments are
still missing. For personal use, feel free to use other patch sets
(such as eawpatches which has excellent quality, but the site is
no more), or other free soundfonts.


%prep
%setup -q -n freepats

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/timidity/freepats
cp -a Drum_000 Tone_000 %{buildroot}%{_datadir}/timidity/freepats/

mkdir -p %{buildroot}%{_sysconfdir}/timidity/freepats
install %{SOURCE1} %{buildroot}%{_sysconfdir}/timidity/timidity-freepats.cfg
install %{SOURCE2} %{buildroot}%{_sysconfdir}/timidity/freepats/freepats.cfg

%clean
rm -rf %{buildroot}

%post
%{_sbindir}/update-alternatives --install %{_sysconfdir}/timidity/timidity.cfg timidity.cfg %{_sysconfdir}/timidity/timidity-freepats.cfg 20

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/update-alternatives --remove timidity.cfg %{_sysconfdir}/timidity/timidity-freepats.cfg
fi

%triggerpostun -- TiMidity++ <= 2.13.2-1mdk
%{_sbindir}/update-alternatives --install %{_sysconfdir}/timidity/timidity.cfg timidity.cfg %{_sysconfdir}/timidity/timidity-freepats.cfg 20

%files
%defattr(-,root,root)
%doc README COPYING
%config(noreplace) %{_sysconfdir}/timidity/timidity-freepats.cfg
%config(noreplace)  %{_sysconfdir}/timidity/freepats
%{_datadir}/timidity/freepats


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 20060219-15mdv2011.0
+ Revision: 670696
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 20060219-14mdv2011.0
+ Revision: 607997
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 20060219-13mdv2010.1
+ Revision: 524229
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 20060219-12mdv2010.0
+ Revision: 427377
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 20060219-11mdv2009.1
+ Revision: 351469
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 20060219-10mdv2009.0
+ Revision: 265765
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 20060219-9mdv2009.0
+ Revision: 206574
- add dir command for configure file, otherwise it will confuse wildmidi
- bunzip the configure files

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 20060219-8mdv2008.1
+ Revision: 171143
- rebuild

* Fri Jan 04 2008 Götz Waschk <waschk@mandriva.org> 20060219-7mdv2008.1
+ Revision: 144833
- fix alternatives uninstallation

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060219-6mdv2008.1
+ Revision: 128453
- kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Oden Eriksson <oeriksson@mandriva.com> 20060219-6mdv2008.0
+ Revision: 90839
- update to new version

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 20060219-5mdv2008.0
+ Revision: 90338
- rebuild

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 20060219-4mdv2008.0
+ Revision: 73491
- bump release

* Mon Jun 25 2007 Thierry Vignaud <tv@mandriva.org> 20060219-3mdv2008.0
+ Revision: 44025
- bump release

* Mon Jun 25 2007 Thierry Vignaud <tv@mandriva.org> 20060219-2mdv2008.0
+ Revision: 44003
- add "noreplace" flag

* Sat Apr 28 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 20060219-1mdv2008.0
+ Revision: 18981
- update to new release: 20060220


* Tue Mar 20 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 20040611-3mdv2007.1
+ Revision: 146933
- bump release

  + Pixel <pixel@mandriva.com>
    - fix typo making alternatives break (#29527)

* Wed Feb 28 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 20040611-2mdv2007.1
+ Revision: 126852
- bump

* Wed Feb 28 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 20040611-1mdv2007.1
+ Revision: 126842
- add #extension in config files to avoid old timidity used by SDL_mixer
  gets syntax errors
- %%mkrel
- Import timidity-patch-freepats

* Thu Feb 17 2005 Abel Cheung <deaddog@mandrake.org> 20040611-1mdk
- First package for Mandrakelinux

