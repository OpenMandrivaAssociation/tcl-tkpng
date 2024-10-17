%define oname tkpng

Summary:	PNG support for Tcl/Tk
Name:		tcl-%{oname}
Version:	0.9
Release:	2
License:	TCL
Group:		System/Libraries
Url:		https://www.muonics.com/FreeStuff/TkPNG/
Source0:	http://downloads.sourceforge.net/tkpng/%{oname}%{version}.tgz
Provides:	%{oname} = %{EVRD}
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(zlib)

%description
TkPNG is an open source package that adds PNG photo image support to Tcl/Tk. 
Although other extensions such as Img also add support for PNG images, this 
package was designed to be lightweight, not depending on libpng nor 
implementing other image formats, and suitable for inclusion in the Tk core. 
Tk does not currently have native support for any image formats that allow 
for alpha (partial-transparency) channels, although it does have support for 
alpha blending internally.

%files
%doc README license.terms ChangeLog
%{tcl_sitearch}/%{oname}%{version}/
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}%{version}
find . -perm 0640 | xargs chmod 0644

%build
%configure2_5x \
%ifarch x86_64
	--enable-64bit
%endif

%make LIBS="-lm -lz"

%install
%makeinstall_std
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{oname}%{version} %{buildroot}%{tcl_sitearch}/%{oname}%{version}

ln -s tcl%{tcl_version}/%{oname}%{version}/lib%{oname}%{version}.so %{buildroot}%{_libdir}/lib%{oname}%{version}.so

