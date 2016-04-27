Name:           python-rpm-macros
Version:        3
Release:        %mkrel 2
Summary:        The unversioned Python RPM macros
License:        MIT
Group:          Development/Python
Source0:        macros.python
Source1:        macros.python-srpm
Source2:        macros.python2
Source3:        macros.python3
# Mga stuff?
Source10:       macros.pybytecompile

BuildArch:      noarch


%description
This package contains RPM macro py_byte_compile to enable specfiles
to selectively byte-compile individual files and paths with different
Python runtimes as necessary.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package -n python-srpm-macros
Summary:        RPM macros for building Python source packages

%description -n python-srpm-macros
RPM macros for building Python source packages.

%package -n python2-rpm-macros
Summary:        RPM macros for building Python 2 packages
Group:          Development/Python
Conflicts:      python < 2.7.11-5
# (tv) it use macros such as %%py_setup from that sub package:
Requires:	python-rpm-macros

%description -n python2-rpm-macros
RPM macros for building Python 2 packages.


%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
Group:          Development/Python
Conflicts:      python3 < 3.5.1-3
# (tv) it use macros such as %%py_setup from that sub package:
Requires:	python-rpm-macros

%description -n python3-rpm-macros
RPM macros for building Python 3 packages.


%prep


%build


%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -m 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} \
  %{SOURCE10} \
  %{buildroot}/%{_rpmconfigdir}/macros.d/


%files
%{_rpmconfigdir}/macros.d/macros.python
%{_rpmconfigdir}/macros.d/macros.pybytecompile

%files -n python-srpm-macros
%{_rpmconfigdir}/macros.d/macros.python-srpm

%files -n python2-rpm-macros
%{_rpmconfigdir}/macros.d/macros.python2

%files -n python3-rpm-macros
%{_rpmconfigdir}/macros.d/macros.python3

