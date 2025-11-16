%define major 2024
# Intentionally versioned to not clash with piper-tts
%define libname %mklibname piper %{major}
%define devname %mklibname piper%{major} -d

Name:		libpiper
Version:	2024.11.27
Release:	1
Source0:	https://github.com/rhasspy/piper/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Fork of the Piper TTS system used by Proton
URL:		https://github.com/shaunren/piper/tree/library
License:	MIT
Group:		System/Libraries
BuildSystem:	cmake
BuildOption:	-DCMAKE_INSTALL_LIBDIR=%{_lib}
BuildOption:	-DCMAKE_INSTALL_INCLUDEDIR=include
BuildRequires:	%mklibname -d piper_phonemize
BuildRequires:	pkgconfig(spdlog)
BuildRequires:	pkgconfig(espeak-ng)

%patchlist
# From https://github.com/shaunren/piper/tree/library
https://github.com/rhasspy/piper/commit/9d06b74959570772e8bcbe7a3f696664d2421167.patch
libpiper-2024.11.27-system-libs.patch
libpiper-2024.11.27-soname.patch
libpiper-2024.11.27-install.patch

%description
Fork of the Piper TTS system used by Proton

%package -n %{libname}
Summary:	Fork of the Piper TTS system used by Proton
Group:		System/Libraries

%description -n %{libname}
Fork of the Piper TTS system used by Proton

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Fork of the Piper TTS system used by Proton

%install -a
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/piper %{buildroot}%{_bindir}/

%files
%{_bindir}/piper

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
