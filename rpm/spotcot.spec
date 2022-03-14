Name:           spotcot
Version:        0.0.1
Release:        1%{?dist}
Summary:        Spotcot RPM
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       python3

%description
spotcot RPM

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install

%clean
rm -rf $RPM_BUILD_ROOT

%files

%changelog
* Mon Mar  14 2022 Ritesh Agarwal <riteshja88@gmail.com> - 0.0.1
- First version being packaged
