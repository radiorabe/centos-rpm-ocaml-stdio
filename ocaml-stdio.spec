%define debug_package %{nil}

Name:           ocaml-stdio
Version:        0.11.0
Release:        0.2%{?dist}
Summary:        Standard IO library for OCaml

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# NOTE: The license changes to MIT at some point after the 0.11.0 tag
License:        Apache-2.0
URL:            https://github.com/janestreet/stdio/
Source0:        https://github.com/janestreet/stdio/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  jbuilder
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-findlib

%description
Stdio implements simple input/output functionalities for OCaml.
It re-exports the input/output functions of the OCaml standard
libraries using a more consistent API.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

# Generate debuginfo, or try to.
sed 's/ocamlc/ocamlc -g/g' -i Makefile
sed 's/ocamlopt/ocamlopt -g/g' -i Makefile

%build
%make_build

%install
# Currently stdio installs itself with ocamlfind.
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
dune install --prefix=$OCAMLFIND_DESTDIR --libdir=$OCAMLFIND_DESTDIR

%files
%doc README.org
%doc %{_libdir}/ocaml/doc/%{libname}
%license LICENSE.txt
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.ml
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license LICENSE.txt
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sat Aug  3 2019 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.2
- Fix dune libdir install

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.1
- Fix Fedora build by disabling debug package

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.0
- Initial build for pcre-ocaml package bump
