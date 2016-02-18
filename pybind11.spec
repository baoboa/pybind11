Name: pybind11		
Version: 1.2	
Release: 	1%{?dist}
Summary: Seamless operability between C++11 and Python

Group:	 python	
License: BSD	
URL:	 https://github.com/wjakob/pybind11	
Source0: https://github.com/wjakob/%{name}/archive/%{name}-%{version}.tgz	

BuildRequires: gcc-c++ gcc glibc-devel python-libs python-devel	cmake
Requires: gcc-c++	

%description
pybind11 is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code.

%prep
%setup -q


%build
%cmake .
make %{?_smp_mflags}

%check

%install
%make_install


%files
%doc LICENSE MANIFEST.in README.md
/usr/include/pybind11/



%changelog
* Thu Feb 18 2016 baoboa <baobabdev@gmail.com> 1.2-1
- new package built with tito, add cmake dependency

* Thu Feb 18 2016 baoboa <baoboa@fedorapeople.org> - 1.2-1
- First build
