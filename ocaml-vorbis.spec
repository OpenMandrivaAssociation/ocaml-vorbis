Name:           ocaml-vorbis
Version:        0.5.1
Release:        2
Summary:        Ocaml bindings to Ogg/Vorbis
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-vorbis/ocaml-vorbis-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ogg-devel
BuildRequires:  pkgconfig(vorbis)

%description
This OCaml library interfaces the vorbis C library. It can be used to
decode from or encode to the Ogg Vorbis compressed audio format as well
as to get informations about an Ogg Vorbis file.

Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
make all opt
make doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/vorbis
make install

%files
%defattr(-,root,root)
%doc CHANGES COPYING README
%dir %{_libdir}/ocaml/vorbis
%{_libdir}/ocaml/vorbis/META
%{_libdir}/ocaml/vorbis/*.cma
%{_libdir}/ocaml/vorbis/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%doc examples
%{_libdir}/ocaml/vorbis/*.a
%{_libdir}/ocaml/vorbis/*.cmxa
%{_libdir}/ocaml/vorbis/*.cmx
%{_libdir}/ocaml/vorbis/*.mli



%changelog
* Tue Jan 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.1-1mdv2010.1
+ Revision: 496518
- update to new version 0.5.1

* Fri Sep 04 2009 Florent Monnier <blue_prawn@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 430796
- import ocaml-vorbis

