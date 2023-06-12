#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-hatchling
Version  : 1.18.0
Release  : 52
URL      : https://files.pythonhosted.org/packages/e3/57/87da2c5adc173950ebe9f1acce4d5f2cd0a960783992fd4879a899a0b637/hatchling-1.18.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e3/57/87da2c5adc173950ebe9f1acce4d5f2cd0a960783992fd4879a899a0b637/hatchling-1.18.0.tar.gz
Summary  : Modern, extensible Python build backend
Group    : Development/Tools
License  : MIT
Requires: pypi-hatchling-bin = %{version}-%{release}
Requires: pypi-hatchling-license = %{version}-%{release}
Requires: pypi-hatchling-python = %{version}-%{release}
Requires: pypi-hatchling-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(trove_classifiers)
BuildRequires : pypi-pathspec
BuildRequires : pypi-pluggy
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Hatchling
<div align="center">
<img src="https://raw.githubusercontent.com/pypa/hatch/master/docs/assets/images/logo.svg" alt="Hatch logo" width="500" role="img">

%package bin
Summary: bin components for the pypi-hatchling package.
Group: Binaries
Requires: pypi-hatchling-license = %{version}-%{release}

%description bin
bin components for the pypi-hatchling package.


%package license
Summary: license components for the pypi-hatchling package.
Group: Default

%description license
license components for the pypi-hatchling package.


%package python
Summary: python components for the pypi-hatchling package.
Group: Default
Requires: pypi-hatchling-python3 = %{version}-%{release}

%description python
python components for the pypi-hatchling package.


%package python3
Summary: python3 components for the pypi-hatchling package.
Group: Default
Requires: python3-core
Provides: pypi(hatchling)
Requires: pypi(editables)
Requires: pypi(packaging)
Requires: pypi(pathspec)
Requires: pypi(pluggy)
Requires: pypi(trove_classifiers)
Requires: pypi-hatch_fancy_pypi_readme
Requires: pypi-hatch_nodejs_version
Requires: pypi-hatch_requirements_txt
Requires: pypi-hatch_vcs

%description python3
python3 components for the pypi-hatchling package.


%prep
%setup -q -n hatchling-1.18.0
cd %{_builddir}/hatchling-1.18.0
pushd ..
cp -a hatchling-1.18.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686582978
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hatchling
cp %{_builddir}/hatchling-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-hatchling/597acb03a5ab8ad933e0aa297418aa8e6ffe61b2 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hatchling

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hatchling/597acb03a5ab8ad933e0aa297418aa8e6ffe61b2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
