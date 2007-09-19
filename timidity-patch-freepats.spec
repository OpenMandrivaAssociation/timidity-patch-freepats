%define version 20060219
%define release %mkrel 6

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
Summary:	Free patch set for MIDI audio synthesis
Group:		Sound
License:	GPL
URL:		http://freepats.opensrc.org/
Source0:	http://freepats.opensrc.org/freepats-%{version}.tar.bz2
Source1:	timidity-freepats.cfg.bz2
Source2:	freepats.cfg.bz2
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
bzip2 -dc %{SOURCE1} > %{buildroot}%{_sysconfdir}/timidity/timidity-freepats.cfg
bzip2 -dc %{SOURCE2} > %{buildroot}%{_sysconfdir}/timidity/freepats/freepats.cfg

%clean
rm -rf %{buildroot}

%post
%{_sbindir}/update-alternatives --install %{_sysconfdir}/timidity/timidity.cfg timidity.cfg %{_sysconfdir}/timidity/timidity-freepats.cfg 20

%preun
if [ "$?" = "0" ]; then
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
