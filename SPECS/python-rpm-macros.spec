Name:           python-rpm-macros
Version:        1
Release:        %mkrel 2
Summary:        The unversioned Python RPM macros
License:        MIT
Group:          Development/Python
Source0:        pybytecompile.macros
Source1:        python2.macros
Source2:        python3.macros

BuildArch:      noarch


%description
This package contains RPM macro py_byte_compile to enable specfiles
to selectively byte-compile individual files and paths with different
Python runtimes as necessary.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.


%package -n python2-rpm-macros
Summary:        RPM macros for building Python 2 packages
Group:          Development/Python


%description -n python2-rpm-macros
RPM macros for building Python 2 packages.


%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
Group:          Development/Python


%description -n python3-rpm-macros
RPM macros for building Python 3 packages.


%prep


%build


%install
mkdir -p %{buildroot}/%{_sysconfdir}/rpm/macros.d/
install -m 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} \
  %{buildroot}/%{_sysconfdir}/rpm/macros.d/


%files
%{_sysconfdir}/rpm/macros.d/pybytecompile.macros


%files -n python2-rpm-macros
%{_sysconfdir}/rpm/macros.d/python2.macros


%files -n python3-rpm-macros
%{_sysconfdir}/rpm/macros.d/python3.macros

