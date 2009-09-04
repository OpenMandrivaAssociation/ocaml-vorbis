Name:           ocaml-vorbis
Version:        0.5.0
Release:        %mkrel 1
Summary:        Ocaml bindings to Ogg/Vorbis
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-vorbis/ocaml-vorbis-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ogg-devel
BuildRequires:  libvorbis-devel

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
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/vorbis
make install

%clean
rm -rf %{buildroot}

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

