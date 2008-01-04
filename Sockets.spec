#
# TODO:
#	- pass CFLAGS
#	- package docs
#	- build shared library
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	C++ Sockets Library
Summary(pl.UTF-8):	Biblioteka gniazd C++
Name:		Sockets
Version:	2.1.8
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.alhem.net/Sockets/%{name}-%{version}.tar.gz
# Source0-md5:	f285cfcd3558e83f4c2b2c5b114d98d8
Source1:	http://www.alhem.net/Sockets/%{name}-%{version}-doxygendocs.tar.gz
# Source1-md5:	d2b4427f6cb10a7f15c3c34edb386ba7
Source2:	http://www.alhem.net/Sockets/tutorial/%{name}-tutorial.tar.gz
# Source2-md5:	86a6c9cb22d06ffacd65cd953398da84
URL:		http://www.alhem.net/Sockets/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ class library wrapping the Berkeley sockets C API. Features
include, but are not limited to, SSL support, IPv6 support, TCP and
UDP sockets, SCTP sockets, HTTP protocol, highly customizable error
handling.

%description -l pl.UTF-8
Biblioteka klas C++ obudowująca berkeleyowskie API C gniazd.
Możliwości obejmują m.in. obsługę SSL, obsługę IPv6, gniazda TCP i
UDP, gniazda SCTP, protokół HTTP, elastyczną obsługę błędów.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/Sockets
%{_libdir}/lib*.a
%{_examplesdir}/%{name}-%{version}
